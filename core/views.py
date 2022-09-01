from .models import Task, Mark, Module
from .serializers import TaskSerializer, MarkSerializer, ModuleSerializer
from .util import get_task_class, get_grader_class
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
import rest_framework.exceptions as exceptions
import json


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_result(self, request, *args, **kwargs):
        task_orm = self.get_object()
        task = get_task_class(task_orm)(task_orm.condition)
        correct_answers = task.answers
        try:
            student_answers = [
                type(answer)(**answer_data)
                for answer, answer_data
                in zip(correct_answers, json.loads(request.data['answer']))
            ]
        except KeyError:
            return exceptions.ParseError
        return get_grader_class(task_orm).grade(correct_answers, student_answers)

    @action(detail=True, methods=['post'])
    def turn_in_idle(self, request, *args, **kwargs):
        return Response(self.get_result(request, *args, **kwargs))
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def turn_in(self, request, *args, **kwargs):
        result = self.get_result(request, *args, **kwargs)
        Mark.objects.create(user=request.user, task=self.get_object(), mark=result[0])
        return Response(status=status.HTTP_201_CREATED)

    @action(detail=True)
    def schema(self, request, *args, **kwargs):
        return Response(get_task_class(self.get_object()).answer_schema())


class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer
    queryset = Mark.objects.all()


class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()

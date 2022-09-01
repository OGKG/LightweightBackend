from .models import Task, Mark, Module
from .serializers import TaskSerializer, MarkSerializer, ModuleSerializer
from .util import get_task_class
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from CGTasks.graham.grader import GrahamGrader
import json


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @action(detail=True, methods=['post'])
    def turn_in(self, request, *args, **kwargs):
        task_orm = self.get_object()
        task = get_task_class(task_orm)(task_orm.condition)
        correct_answers = task.answers
        student_answers = [
            type(answer)(**answer_data)
            for answer, answer_data
            in zip(correct_answers, json.loads(request.data['answer']))
        ]
        return Response(GrahamGrader.grade(correct_answers, student_answers))


class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer
    queryset = Mark.objects.all()


class ModuleViewSet(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()


class TaskSchemaAPIView(APIView):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        # model_type = Task.mapping.get(task.type)
        return Response(get_task_class(task).answer_schema())


class AnswerAPIView(APIView):
    pass
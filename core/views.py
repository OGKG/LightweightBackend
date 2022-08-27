from .models import Task
from .serializers import TaskSerializer
from .util import get_task_class
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskSchemaAPIView(APIView):
    def get(self, request, id):
        task = Task.objects.get(id=id)
        # model_type = Task.mapping.get(task.type)
        return Response(get_task_class(task).answer_schema())


class AnswerAPIView(APIView):
    pass
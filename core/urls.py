from django.urls import path, include
from .views import TaskViewSet, TaskSchemaAPIView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:id>/schema', TaskSchemaAPIView.as_view())
]
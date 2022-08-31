from django.urls import path, include
from .views import TaskViewSet, TaskSchemaAPIView, MarkViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('marks', MarkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:id>/schema', TaskSchemaAPIView.as_view())
]
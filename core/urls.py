from django.urls import path, include
from .views import TaskViewSet, MarkViewSet, ModuleViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('marks', MarkViewSet)
router.register('modules', ModuleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
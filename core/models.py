from django.db import models
from CGTasks.graham.task import GrahamTask
from CGTasks.kd_tree.task import KdTreeTask
from CGTasks.quickhull.task import QuickhullTask


mapping = {
    "graham": GrahamTask,
    "kd tree": KdTreeTask,
    "quickhull": QuickhullTask,
}

class Task(models.Model):
    """Lightweigth repr of task"""
    condition = models.JSONField("Condition")
    type = models.TextField(choices=list(zip(mapping.keys(), mapping.keys())))

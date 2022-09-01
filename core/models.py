from django.db import models
from django.contrib.auth import get_user_model
from CGTasks import task_types


mapping = {tt.__name__.lower()[:-4]: tt for tt in task_types}

class Task(models.Model):
    """Lightweigth repr of task"""
    condition = models.JSONField("Condition")
    type = models.TextField(choices=list(zip(mapping.keys(), mapping.keys())))
    users = models.ManyToManyField(get_user_model(), 'tasks', through="Mark")

    def mark_of(self, user):
        return Mark.objects.get(user=user, task=self)


class Mark(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE, 'marks')
    task = models.ForeignKey(Task, models.CASCADE, 'marks')
    mark = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'task'], name="%(app_label)s_%(class)s_unique")
        ]


class Module(models.Model):
    tasks = models.ManyToManyField(Task, 'modules')
    name = models.TextField(null=False, blank=False)

    def mark_of(self, user):
        return sum(task.mark_of(user).mark for task in self.tasks.all())
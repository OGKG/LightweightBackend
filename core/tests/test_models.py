from core.models import *
from django.db import transaction
from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()


class ModelTest(TestCase):
    def setUp(self):
        u = User.objects.create(username='user', password='123123123')
        t = Task.objects.create(type='graham', condition={
            "point_list": [
                {
                    "x": 6.0,
                    "y": 4.0
                },
                {
                    "x": 4.0,
                    "y": 2.0
                },
                {
                    "x": 4.0,
                    "y": 0.0
                },
                {
                    "x": 1.0,
                    "y": 0.0
                },
                {
                    "x": 3.0,
                    "y": 2.0
                },
                {
                    "x": 2.0,
                    "y": 4.0
                }
            ]
        })
        Mark.objects.create(task = t, user = u, mark=1)
        Module.objects.create(name='module').tasks.add(t)

    def test_mark_of_user(self):
        mod = Module.objects.get(id=1)
        u = User.objects.get(id=1)
        self.assertEqual(mod.mark_of(u), 1)

    def test_unique_mark_contraint(self):
        from django.db.utils import IntegrityError
        def create_two_marks():
            with transaction.atomic():
                Mark.objects.create(task_id = 1, user_id = 1, mark=1)
                Mark.objects.create(task_id = 1, user_id = 1, mark=1)
        self.assertRaises(IntegrityError, create_two_marks)

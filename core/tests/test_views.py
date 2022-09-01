import json
from django.test import TestCase, Client
from core.models import Task, Mark
from core.tests.answer import correct_answer
from django.contrib.auth import get_user_model
from rest_framework.exceptions import NotAuthenticated
User = get_user_model()


class ViewTest(TestCase):
    def setUp(self) -> None:
        t = Task.objects.create(type='graham', condition=
        {
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
        self.credentials = {"username": "user", "password": "123123123"}
        u = User.objects.create(username="user")
        u.set_password("123123123")
        u.save()

    
    def test_task_turn_in(self):
        c = Client(HTTP_USER_AGENT='Mozilla/5.0')

        def call():
            return c.post('/tasks/1/turn_in/', {})
        self.assertEqual(call().status_code, 403)

        def call_correct_payload():
            return c.post('/tasks/1/turn_in_idle/', {'answer': json.dumps(correct_answer)})
        self.assertEqual(call_correct_payload().status_code, 200)
        c.login(**self.credentials)

        def call_not_idle():
            return c.post('/tasks/1/turn_in/', {'answer': json.dumps(correct_answer)})
        call_not_idle()
        try:
            Mark.objects.get(user_id=1, task_id=1).mark
            self.assertEqual(Mark.objects.get(user_id=1, task_id=1).mark, 2)
        except:
            self.fail()

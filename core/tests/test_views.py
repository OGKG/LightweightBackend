from django.test import TestCase, Client
from core.models import Task


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
    def test_task_turn_in(self):
        c = Client(HTTP_USER_AGENT='Mozilla/5.0')
        import json
        # def call():
        #     c.post('/tasks/1/turn_in/', {})
        # self.assertRaises(TypeError, call)
        def call_correct_payload():
            return c.post('/tasks/1/turn_in/', {'answer': json.dumps(
            [
    {
        "x": 4.666666666666667,
        "y": 2.0
    },
    {
        "points": [
            {
                "x": 4.0,
                "y": 0.0
            },
            {
                "x": 6.0,
                "y": 4.0
            },
            {
                "x": 2.0,
                "y": 4.0
            },
            {
                "x": 4.0,
                "y": 2.0
            },
            {
                "x": 3.0,
                "y": 2.0
            },
            {
                "x": 1.0,
                "y": 0.0
            }
        ]
    },
    {
        "x": 4.0,
        "y": 0.0
    },
    {
        "rows": [
            {
                "cells": [
                    {
                        "content": [
                            {
                                "x": 4.0,
                                "y": 0.0
                            },
                            {
                                "x": 6.0,
                                "y": 4.0
                            },
                            {
                                "x": 2.0,
                                "y": 4.0
                            }
                        ]
                    },
                    {
                        "content": "less"
                    },
                    {
                        "content": {
                            "x": 6.0,
                            "y": 4.0
                        }
                    },
                    {
                        "content": "yes"
                    }
                ]
            },
            {
                "cells": [
                    {
                        "content": [
                            {
                                "x": 6.0,
                                "y": 4.0
                            },
                            {
                                "x": 2.0,
                                "y": 4.0
                            },
                            {
                                "x": 4.0,
                                "y": 2.0
                            }
                        ]
                    },
                    {
                        "content": "less"
                    },
                    {
                        "content": {
                            "x": 2.0,
                            "y": 4.0
                        }
                    },
                    {
                        "content": "yes"
                    }
                ]
            },
            {
                "cells": [
                    {
                        "content": [
                            {
                                "x": 2.0,
                                "y": 4.0
                            },
                            {
                                "x": 4.0,
                                "y": 2.0
                            },
                            {
                                "x": 3.0,
                                "y": 2.0
                            }
                        ]
                    },
                    {
                        "content": "more"
                    },
                    {
                        "content": {
                            "x": 4.0,
                            "y": 2.0
                        }
                    },
                    {
                        "content": "no"
                    }
                ]
            },
            {
                "cells": [
                    {
                        "content": [
                            {
                                "x": 6.0,
                                "y": 4.0
                            },
                            {
                                "x": 2.0,
                                "y": 4.0
                            },
                            {
                                "x": 3.0,
                                "y": 2.0
                            }]
                    },
                    {
                        "content": "less"
                    },
                    {
                        "content": {
                            "x": 2.0,
                            "y": 4.0
                        }
                    },
                    {
                        "content": "yes"
                    }
                ]
            },
            {
                "cells": [
                    {
                        "content": [
                            {
                                "x": 2.0,
                                "y": 4.0
                            },
                            {
                                "x": 3.0,
                                "y": 2.0
                            },
                            {
                                "x": 1.0,
                                "y": 0.0
                            }
                        ]
                    },
                    {
                        "content": "more"
                    },
                    {
                        "content": {
                            "x": 3.0,
                            "y": 2.0
                        }
                    },
                    {
                        "content": "no"
                    }
                ]
            },
            {
                "cells": [
                    {
                        "content": [
                            {
                                "x": 6.0,
                                "y": 4.0
                            },
                            {
                                "x": 2.0,
                                "y": 4.0
                            },
                            {
                                "x": 1.0,
                                "y": 0.0
                            }
                        ]
                    },
                    {
                        "content": "less"
                    },
                    {
                        "content": {
                            "x": 2.0,
                            "y": 4.0
                        }
                    },
                    {
                        "content": "yes"
                    }
                ]
            },
            {
                "cells": [
                    {
                        "content": [
                            {
                                "x": 2.0,
                                "y": 4.0
                            },
                            {
                                "x": 1.0,
                                "y": 0.0
                            },
                            {
                                "x": 4.0,
                                "y": 0.0
                            }
                        ]
                    },
                    {
                        "content": "less"
                    },
                    {
                        "content": {
                            "x": 1.0,
                            "y": 0.0
                        }
                    },
                    {
                        "content": "yes"
                    }
                ]
            }
        ],
        "headers": [
            "",
            "",
            "",
            ""
        ]
    }
            ])})
        self.assertEqual(call_correct_payload().status_code, 200)
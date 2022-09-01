import CGTasks


def get_task_class(task):
    return {
        cls.__name__.replace('Task', '').lower(): cls 
        for cls 
        in CGTasks.task_types
}.get(task.type)

def get_grader_class(task):
    return {
        cls.__name__.replace('Grader', '').lower(): cls 
        for cls 
        in CGTasks.grader_types
}.get(task.type)
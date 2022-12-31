from celery import shared_task
from time import sleep
from todo.views import DeleteTask

@shared_task
def deleteTask():
    DeleteTask
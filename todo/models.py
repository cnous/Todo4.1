from django.db import models
from accounts.models import User


# Create your models here.
from django.urls import reverse


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("task_list")

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = "user"

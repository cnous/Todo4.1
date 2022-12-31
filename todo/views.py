from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskUpdateForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/list_task.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy("todo:task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)


class UpdateTask(UpdateView, LoginRequiredMixin):
    UpdateView.model = Task
    UpdateView.fields = ("title",)
    form_class = TaskUpdateForm
    success_url = reverse_lazy("todo:task_list")


class CompleteTask(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("todo:task_list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.success_url)


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("todo:task_list")

    #
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

# def delet_task():
#     deleteTask.delay()
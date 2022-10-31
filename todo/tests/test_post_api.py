import pytest
from django.urls import reverse
from datetime import datetime
from accounts.models import User
from ..models import Task
import json

from rest_framework.test import APIClient

@pytest.fixture
def api_client():
    client = APIClient()
    return client

@pytest.fixture
def common_user():
    user = User.objects.create_user(email='sin@s.com', password='241195ali')
    return user

@pytest.fixture
def create_task():
    task = Task.objects.create(title='test', complete=False, created_date=datetime.now())
    return task

@pytest.mark.django_db
class TestPostApi:

    def test_get_task_resoponse_200(self, api_client,common_user):
        url = reverse('todo:api-v1:task-list-list')
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_task_forbiden_response_401(self, api_client, common_user):
        url = reverse('todo:api-v1:task-list-list')
        data = {
            'title': 'test',
            'complete': False,
            'created_date': datetime.now()
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 401
    #
    def test_create_post_task_response_201(self,api_client,common_user):
        url = reverse('todo:api-v1:task-list-list')
        data = {
            'pk': '20',
            'title': 'test',
            'complete': False,
            'created_date': datetime.now()
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_task_response_400(self,api_client,common_user):
        url = reverse('todo:api-v1:task-list-list')
        data = {

            'complete': False,
            'created_date': datetime.now()
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400

    def test_put_task_response_200(self, api_client, common_user, create_task):
        url = reverse('todo:api-v1:task-list-detail', kwargs={'pk': '1'})
        data = {
            'title': 'test1',
            'complete': True,
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.put(url, data=data)
        assert response.status_code == 200

    def test_delete_post_task_204(self, api_client, common_user, create_task):
        url = reverse('todo:api-v1:task-list-detail', kwargs={'pk': '1'})
        user = common_user
        api_client.force_authenticate(user)
        response = api_client.delete(url)
        assert response.status_code == 204

    def test_put_invalid_task_response_200(self, api_client, common_user, create_task):
        url = reverse('todo:api-v1:task-list-detail', kwargs={'pk': '1'})
        data = {

        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.put(url, data=data)
        assert response.status_code == 400

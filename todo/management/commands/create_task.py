from django.core.management import BaseCommand
from faker import Faker
from accounts.models import User
from todo.models import Task
from datetime import datetime
import random

class Command(BaseCommand):
    help = 'python manage.py create_task'

    def __init__(self):
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(), password='test@123', is_active=False)

        for _ in range(5):
            Task.objects.create(
                user=user,
                title=self.fake.paragraph(nb_sentences=1),
                created_date=datetime.now(),
                complete=random.choice([True,False])
            )
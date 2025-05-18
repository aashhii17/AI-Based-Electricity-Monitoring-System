from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create admin user with specified credentials'

    def handle(self, *args, **kwargs):
        username = 'admin@example.com'
        password = 'Aashi'
        contact_number = '9874563210'

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING('Admin user already exists.'))
        else:
            user = User.objects.create_superuser(username=username, email=username, password=password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Admin user created with username: {username} and password: {password}'))

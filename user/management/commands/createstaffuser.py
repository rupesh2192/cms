from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    help = 'Creates Staff User'

    def handle(self, *args, **options):
        try:
            user = User.objects.create_user(username="john", email="john@example.com", password="test", is_staff=True,
                             first_name="John", last_name="Doe")
            user.is_active = True
            user.save()
        except Exception as e:
            pass
        self.stdout.write(self.style.SUCCESS('Successfully created user "john"'))

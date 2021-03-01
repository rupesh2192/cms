from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    help = 'Creates Admin User'

    def handle(self, *args, **options):
        try:
            user = User.objects.create_superuser(username="admin", email="admin@example.com", password="admin",
                                                 first_name="Test")
            user.is_active = True
            user.save()
        except Exception as e:
            pass
        self.stdout.write(self.style.SUCCESS('Successfully created user "admin"'))

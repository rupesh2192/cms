from random import choice

from django.conf import settings
from django.core.management import BaseCommand
import csv

from customer.models import Customer
from user.models import User

TEMP = [
    {"notes": "Customer asked to call back", "requires_callback": True, "interaction_mode": "P"},
    {"notes": "Customer asked to send product details over the email", "requires_callback": True,
     "interaction_mode": "P"},
    {"notes": "Sent product details over the email", "requires_callback": True, "interaction_mode": "E"},
    {"notes": "Customer liked the product and requested product demo.", "requires_callback": True,
     "interaction_mode": "P"},
    {"notes": "Customer purchased the product and gave a positive feedback.", "requires_callback": False,
     "interaction_mode": "P"},
]

from random import randrange
from datetime import timedelta, datetime


def random_date(start=datetime.today() - timedelta(days=100), end=datetime.today()):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


class Command(BaseCommand):
    help = 'Generates random Customer interaction records'

    def handle(self, *args, **options):
        try:
            customer = Customer.objects.first()
            customer.interactions.all().delete()
            for i in TEMP:
                customer.interactions.create(**i, created_by=customer.created_by)
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(e))
            return
        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(TEMP)} interactions for {customer.first_name} with id {customer.id}'))

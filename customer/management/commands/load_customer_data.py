from random import choice

from django.conf import settings
from django.core.management import BaseCommand
import csv

from customer.models import Customer
from user.models import User


class Command(BaseCommand):
    help = 'Loads Customer data from CSV file'

    def handle(self, *args, **options):
        try:
            customer_info = csv.DictReader(open(f"{settings.BASE_DIR}/us-500.csv"))
            customers = []
            Customer.objects.all().delete()
            for customer in customer_info:
                c = Customer(
                    first_name=customer["first_name"],
                    last_name=customer["last_name"],
                    country="USA",
                    city=customer["city"],
                    phone=customer["phone1"].replace("-", ""),
                    email=customer["email"],
                    created_by_id=choice([2, 3, 4])
                )
                customers.append(c)
            Customer.objects.bulk_create(customers)
        except Exception as e:
            print(e)
            pass
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(customers)} customer records'))

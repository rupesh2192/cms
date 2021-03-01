from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from customer.models import Customer
from user.models import User


class CustomerTests(APITestCase):

    def setUp(self) -> None:
        user = User.objects.create_superuser("admin", "admin@example.com", "admin")
        user.is_active = True
        user.save()
        Customer.objects.create(first_name="Test",email="test@test.com",phone="9999888801")
        self.client.force_login(user=User.objects.last())

    def test_create_customer(self):
        """
        Ensure we can create a new customer object.
        """
        url = reverse('customer-list')
        data = {"first_name": "Test1", "email": "test1@test.com", "phone": "9999888802"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)
        self.assertEqual(Customer.objects.filter(email="test1@test.com").count(), 1)

    def test_update_customer(self):
        """
        Ensure we can update a customer object.
        """
        cid = Customer.objects.last().id
        url = reverse('customer-detail', args=[cid])
        data = {"first_name": "Test2"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.last().first_name, 'Test2')

    def test_delete_customer(self):
        """
        Ensure we can delete a customer object.
        """
        cid = Customer.objects.last().id
        url = reverse('customer-detail', args=[cid])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)
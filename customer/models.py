from django.db import models

# Create your models here.
from user.models import User


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Customer(BaseModel):
    GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("O", "Other"))

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=True, default=None)
    email = models.EmailField(null=False, unique=True, db_index=True)
    phone = models.CharField(max_length=10, null=False, unique=True, db_index=True)
    gender = models.CharField(max_length=1, null=True, default=None)
    age = models.IntegerField(null=True, default=None)
    country = models.CharField(max_length=255, null=True, default=None)
    city = models.CharField(max_length=255, null=True, default=None)
    created_by = models.ForeignKey(User, null=True, related_name="prospects", on_delete=models.SET_NULL)

    class Meta:
        ordering = ["-created_at"]

    def get_interactions(self):
        return self.interactions.all()


class CustomerInteraction(BaseModel):
    INTERACTION_MODE_CHOICES = (("E", "E-Mail"), ("P", "Phone"))

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="interactions")
    created_by = models.ForeignKey(User, null=True, related_name="customer_interactions", on_delete=models.SET_NULL)
    call_duration = models.IntegerField(null=True, default=None)
    interaction_mode = models.CharField(choices=INTERACTION_MODE_CHOICES, null=False, max_length=1)
    notes = models.TextField(null=True)
    requires_callback = models.BooleanField(default=True)

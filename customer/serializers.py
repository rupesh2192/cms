from rest_framework import serializers

from customer.models import Customer, CustomerInteraction
from user.serializers import UserSerializer


class CustomerSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(required=False)

    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["created_by"] = validated_data.get("created_by", user)
        return super(CustomerSerializer, self).create(validated_data)


class CustomerInteractionSerializer(serializers.ModelSerializer):
    created_by_user = UserSerializer(read_only=True, source="created_by")
    customer_data = CustomerSerializer(read_only=True, source="customer")
    interaction_type = serializers.CharField(source="get_interaction_mode_display", read_only=True)
    interaction_mode = serializers.CharField(write_only=True)
    message = serializers.SerializerMethodField()

    class Meta:
        model = CustomerInteraction
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["created_by"] = validated_data.get("created_by", user)
        return super(CustomerInteractionSerializer, self).create(validated_data)

    def get_message(self, obj):
        return f"{obj.created_at.strftime('%a %D %T')}:{obj.created_by.first_name} contacted " \
               f"{obj.customer.first_name} via {obj.get_interaction_mode_display()}"

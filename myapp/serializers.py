from rest_framework import serializers
from .models import Address, ClassificationInsType, ClassificationProdType, ClosedAccount, ConsCommDetails

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ClassificationInsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationInsType
        fields = '__all__'

class ClassificationProdTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationProdType
        fields = '__all__'

class ClosedAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosedAccount
        fields = '__all__'

class ConsCommDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsCommDetails
        fields = '__all__'

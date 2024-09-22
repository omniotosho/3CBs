from rest_framework import viewsets
from .models import Address, ClassificationInsType, ClassificationProdType, ClosedAccount, ConsCommDetails
from .serializers import AddressSerializer, ClassificationInsTypeSerializer, ClassificationProdTypeSerializer, ClosedAccountSerializer, ConsCommDetailsSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ClassificationInsTypeViewSet(viewsets.ModelViewSet):
    queryset = ClassificationInsType.objects.all()
    serializer_class = ClassificationInsTypeSerializer

class ClassificationProdTypeViewSet(viewsets.ModelViewSet):
    queryset = ClassificationProdType.objects.all()
    serializer_class = ClassificationProdTypeSerializer

class ClosedAccountViewSet(viewsets.ModelViewSet):
    queryset = ClosedAccount.objects.all()
    serializer_class = ClosedAccountSerializer

class ConsCommDetailsViewSet(viewsets.ModelViewSet):
    queryset = ConsCommDetails.objects.all()
    serializer_class = ConsCommDetailsSerializer

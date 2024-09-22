from fastapi import FastAPI
from pydantic import BaseModel
from django.core.management import execute_from_command_line
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from myapp.models import Address, ClassificationInsType, ClassificationProdType, ClosedAccount, ConsCommDetails
from myapp.serializers import (
    AddressSerializer, ClassificationInsTypeSerializer, ClassificationProdTypeSerializer,
    ClosedAccountSerializer, ConsCommDetailsSerializer
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/addresses")
def get_addresses():
    addresses = Address.objects.all()
    serializer = AddressSerializer(addresses, many=True)
    return serializer.data

@app.get("/classification_ins_types")
def get_classification_ins_types():
    ins_types = ClassificationInsType.objects.all()
    serializer = ClassificationInsTypeSerializer(ins_types, many=True)
    return serializer.data

@app.get("/classification_prod_types")
def get_classification_prod_types():
    prod_types = ClassificationProdType.objects

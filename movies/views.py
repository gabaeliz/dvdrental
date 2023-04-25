from django.shortcuts import render
from rest_framework import generics
from .pagination import CustomPagination



from .models import (
    Actor, 
    Film, 
    Rental, 
    Payment, 
    Inventory
    )

from .serializers import (
    ActorSerializer, 
    FilmSerializer, 
    RentalSerializer, 
    PaymentSerializer, 
    InventorySerializer
    )

#Post,get    
class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

#CRUD
class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

#get, post
class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    pagination_class = CustomPagination    

#CRUD
class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

#get,post
class RentalList(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    pagination_class = CustomPagination

#CRUD
class RentalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

#GET, POST
class PaymentList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = CustomPagination


#CRUD
class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

#GET,POST
class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    #pagination_class = CustomPagination

#CRUD
class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

   







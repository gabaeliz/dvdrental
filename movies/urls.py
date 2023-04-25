from django.urls import path

from .views import (
    ActorList,
    ActorDetail,
    FilmList,
    FilmDetail,
    RentalList,
    PaymentList,
    RentalDetail,
    PaymentDetail,
    InventoryList,
    InventoryDetail,
)

urlpatterns = [
    path('actor/', ActorList.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetail.as_view(), name='actor_detail'),
    path('film/', FilmList.as_view(), name='film_list'),
    path('film/<int:pk>/', FilmDetail.as_view(), name='film_detail'),
    path('rental/', RentalList.as_view(), name='rental_list'),
    path('rental/<int:pk>/', RentalDetail.as_view(), name='rental_detail'),
    path('payment/', PaymentList.as_view(), name='payment_list'),
    path('payment/<int:pk>/', PaymentDetail.as_view(), name='payment_detail'),
    path('inventory/', InventoryList.as_view(), name='inventory_list'),
    path('inventory/<int:pk>/', InventoryDetail.as_view(), name='inventory_detail'),

]
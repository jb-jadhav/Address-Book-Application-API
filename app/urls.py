from django.urls import path
from app import views

urlpatterns = [
    path('',views.AddressBook.as_view()),
    path('<int:pk>/',views.AddressBook.as_view())
]

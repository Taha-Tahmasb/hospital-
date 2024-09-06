from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome),
    path('appointment/', views.appointmentList.as_view()),
    path('transaction/', views.Transaction.as_view()),
    path('service/', views.Service.as_view()),
]
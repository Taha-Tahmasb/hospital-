from .models import *
from django.http.response import JsonResponse
from .serializer import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
def welcome(requset):
    return JsonResponse("Welcoem to hospitall" , safe=False)
class Login(TokenObtainPairView):
    pass
class Logout(TokenRefreshView):
    pass
class Refresh(TokenRefreshView):
    pass
class appointmentList(ListCreateAPIView):
    queryset = appointment.objects.all()
    serializer_class = appointmentserializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['__all__']
    
class Transaction(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['__all__']
def add_service(request):
    if request.method == "Post":
        new_service = request.POST.get("service")
        Service.objects.create(new_service)
def edit_appoinmenrt(request):
    if request.mothod == "POST":
        edited_service_name = request.POST.get("edited_appointment_name")
        appoinment = appointment.objects.get(Service__id = "id")
        new_date = request.POST.get("new_time")
        appoinment.time = new_date
        appoinment.name = edited_service_name
        edited_service_name.save()







from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .models import UserAddress, UserFavourite
from .serializers import UserAddressSerialzier, UserFavouriteSerialzier
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from config.paginatior import MyPaginator
# Create your views here.


class UserAddressListCreateApiView(ListCreateAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerialzier
    permission_classes = [IsAuthenticated]
    pagination_class = MyPaginator
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


    def create(self, request):
        self.request.data['user'] = self.request.user.id
        return super().create(self.request)
    

class UserAddressDestorApiView(DestroyAPIView):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerialzier
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            return super().perform_destroy(instance)
        return False


class UserFavouriteListCreateApiView(ListCreateAPIView):
    queryset = UserFavourite.objects.all()
    serializer_class = UserFavouriteSerialzier
    permission_classes = [IsAuthenticated]
    pagination_class = MyPaginator
    
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def create(self, request):
        self.request.data['user'] = self.request.user.id
        return super().create(self.request)
    

class UserFavouriteDestorApiView(DestroyAPIView):
    queryset = UserFavourite.objects.all()
    serializer_class = UserFavouriteSerialzier
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            return super().perform_destroy(instance)
        return False

from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

from .models import Mixin
from .serialzers import MixinSerializer
# Create your views here.

class MixinView(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                GenericAPIView): # 
    
    queryset = Mixin.objects.all()
    serializer_class = MixinSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     print('cоздаеттся книга')

    #     self.response = super().create(request, *args, **kwargs)
    #     return self.response 
    
    # def perform_create(self, serializer):
    #     serializer.save()

    # def perform_create(self, serializer):
    #     serializer.save(title=self.request.user)


    
class MixinDetailView(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                GenericAPIView): # 
    
    queryset = Mixin.objects.all()
    serializer_class = MixinSerializer

    def get(self, request, *args, **kwargs): # kwargs = pk
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    
from django.urls import path
from .views import MixinDetailView, MixinView

urlpatterns = [
    path('', MixinView.as_view(), name='mixin-list'),
    path('<int:pk>/', MixinDetailView.as_view(), name='mixin-detail')
]


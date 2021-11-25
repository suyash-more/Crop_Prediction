from django.urls import path
from .views import crop_detail_view, resultpage

urlpatterns = [
    path('', crop_detail_view, name="crop_detail_view"),
    path('result/', resultpage, name="resultpage"),
]

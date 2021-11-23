from django.urls import path
from .views import crop_detail_view, index, resultpage

urlpatterns = [
    path('', index, name="index_page"),
    path('crop', crop_detail_view, name="crop_detail_view"),
    path('result', resultpage, name="result_view")
]

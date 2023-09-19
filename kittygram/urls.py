from django.urls import path

from cats.views import CatList, CatDetail, APICat, APICatDetail

urlpatterns = [
    path('cats/', CatList.as_view()),
    path('cats/<int:pk>/', CatDetail.as_view()),
    path('api/v1/posts/', APICat.as_view()),
    path('api/v1/posts/<int:pk>/', APICatDetail.as_view()),
]
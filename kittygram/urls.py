from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cats.views import CatList, CatDetail, APICat, APICatDetail, CatViewSet

router = DefaultRouter()
router.register('cats_vs', CatViewSet, basename='tiger')

urlpatterns = [
    path('', include(router.urls)),
    path('cats/', CatList.as_view()),
    path('cats/<int:pk>/', CatDetail.as_view()),
    path('api/v1/posts/', APICat.as_view()),
    path('api/v1/posts/<int:pk>/', APICatDetail.as_view()),

]


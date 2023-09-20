from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from cats.views import (
    CatList,
    CatDetail,
    APICat,
    APICatDetail,
    CatViewSet,
    OwnerViewSet
)

router = DefaultRouter()
router.register('api/v3/cats', CatViewSet)
router.register('api/v3/owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/cats/', CatList.as_view()),
    path('api/v1/cats/<int:pk>/', CatDetail.as_view()),
    path('api/v2/cats/', APICat.as_view()),
    path('api/v2/cats/<int:pk>/', APICatDetail.as_view()),
    path('admin', admin.site.urls),
]


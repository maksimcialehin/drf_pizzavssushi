from django.urls import path
from .views import PizzeriaListAPIVIEW, PizzeriaRetrieveAPIAPIView


urlpatterns = [
    path('', PizzeriaListAPIVIEW.as_view(), name='pizzeria_list'),
    path('<int:id>', PizzeriaRetrieveAPIAPIView.as_view(), name='pizzeria_detail'),
]

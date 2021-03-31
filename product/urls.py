from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.ProductRegister.as_view()),
    path('', views.ProductList.as_view()),
    path('<int:pk>/', views.ProductDetailView.as_view()),
    path('api/', views.ProductListApi.as_view()),
    path('api/<int:pk>/', views.ProductDetailApi.as_view()),
]
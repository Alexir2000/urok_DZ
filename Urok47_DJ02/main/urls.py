from django.urls import path
from . import views

urlpatterns = [
    path('', views.func_index, name='index'),
    path('new/', views.func_new, name='new'),
    path('data/', views.func_data, name='data'),
    path('test/', views.func_test, name='test')
]
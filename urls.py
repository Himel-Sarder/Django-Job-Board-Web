from django.contrib import admin
from django.urls import path
from Project1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:first_name>/', views.hello, name='hello'),
    path('Sum/<int:num1>/<int:num2>/', views.Sum, name='Sum'),
]

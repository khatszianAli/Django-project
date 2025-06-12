from django.urls import path
from .import views

urlpatterns = [
    path('', views.lists, name='list'),
    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userloginout, name='logout'),
    path('mark/', views.mark, name='mark'),
    path('table/', views.table, name='table'),
    path('<str:slot>', views.Detail.as_view(), name='detail'),
    path('<str:slot>/delete', views.BookingDeleteView.as_view(), name='booking_delete'),
]
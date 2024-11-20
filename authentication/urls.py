from django.urls import path
from authentication.views import login, logout
from authentication.views import login, register  # Tambahkan register di baris ini


app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
from django.urls import path
from . import views



app_name = 'management'

urlpatterns = [
path('user-list/', views.user_list, name='user-list'),
]
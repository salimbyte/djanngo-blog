from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('edit/', profile_update, name='profile-update'),
    path('dp-update/', update_profile_picture, name='dp-update'),
]

from django.urls import path
from .views import coach_signup
from .views import signup
from .views import home

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', home, name='home'),
    path('signup/coach/', coach_signup, name='signup_coach'),
    
]
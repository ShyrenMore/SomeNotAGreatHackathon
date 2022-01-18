from django.urls import path
from .views import main, expenditure, reminders, categories, goals, authentication

## rest imports
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ## auth
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', authentication.register, name='register'),
    # path('auth/logout/', authentication.logout, name='logout'),

]

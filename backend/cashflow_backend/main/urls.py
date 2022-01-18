from django.urls import path
from .views import main, expenditure, categories, authentication

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
    
    # expenditures
    path("main/", main.main, name="main"),
    path("allexpenditures/", expenditure.all_expenditures, name="allexpenditures"),
    path("get-n-expenditures/<int:exp_count>/", expenditure.get_n_expenditures, name="get_n_expenditures"),
    path("add-expenditure/", expenditure.add_expenditure, name="add_expenditure"),
    path("update-expenditure/<int:expenditure_id>", expenditure.update_expenditure, name="update_expenditure"),
    path("detect-expenditure/", expenditure.detect_expenditure, name="detect_expenditure"),
    path("expenditure-heatmap/", expenditure.expenditure_heatmap, name="expenditure_heatmap"),
]

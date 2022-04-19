from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .api.views.register_view import RegisterView
from .api.views.user_info_view import UserInfoView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', UserInfoView.as_view())
]

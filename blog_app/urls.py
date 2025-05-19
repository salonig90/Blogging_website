from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework_simplejwt.views import TokenVerifyView



router = DefaultRouter()
router.register('blog',views.BlogPostViewSet,basename='blog')
router.register('comment',views.CommentViewSet,basename='comment')
urlpatterns = [

    path('',include(router.urls)),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('demo/', views.DemoView.as_view(), name='demo'),

    path('register/', views.RegisterView.as_view(), name='register'),
]
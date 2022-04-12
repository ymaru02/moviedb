"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

###################################################
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Tony API",
      default_version='v1',
      description="todo를 생성하고 삭제하는 등, 할 일을 관리하는 api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="tony@tony.com"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
###################################################

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
# )
from .serializers import (
    MyTokenObtainPairView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls')),
    path('swagger/', schema_view.with_ui('swagger')),
    path('api/token/', MyTokenObtainPairView.as_view()),
]


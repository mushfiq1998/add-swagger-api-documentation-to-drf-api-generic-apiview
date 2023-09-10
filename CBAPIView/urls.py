from django.contrib import admin
from django.urls import path
from api import views

# For swagger
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="Student name register",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@xyz.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_list/', views.StudentList.as_view()),
    path('student_create/', views.StudentCreate.as_view()),
    path('student_retrieve/<int:pk>/', views.StudentRetrieve.as_view()),
    path('student_update/<int:pk>/', views.StudentUpdate.as_view()),
    path('student_delete/<int:pk>/', views.StudentDestroy.as_view()),

    # For swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), 
         name='schema-swagger-ui'),
]
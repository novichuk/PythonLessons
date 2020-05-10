from django.contrib import admin
from django.urls import path

from students import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello-world/', views.hello_world),

    path('students/', views.students),
]

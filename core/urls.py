from django.contrib import admin
from django.urls import path
from tracker.views import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', profile_view, name='profile'),
]

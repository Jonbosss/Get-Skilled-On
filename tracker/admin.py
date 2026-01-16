from django.contrib import admin
from .models import Profile  # <--- Check this matches models.py

admin.site.register(Profile)

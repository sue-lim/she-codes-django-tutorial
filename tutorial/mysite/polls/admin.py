from django.contrib import admin

# Register your models here.
from .models import Question
#linking models.py

admin.site.register(Question)


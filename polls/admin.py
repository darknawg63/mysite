from django.contrib import admin

from .models import Choice, Question
# Registers the Question model in the admin app.
admin.site.register(Choice)
admin.site.register(Question)

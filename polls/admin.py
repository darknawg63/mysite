from django.contrib import admin

from .models import Question
# Registers the Question model in the admin app.
admin.site.register(Question)

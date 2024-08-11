from django.contrib import admin
from . models import Task
from . models import Label

admin.site.register(Task)
admin.site.register(Label)

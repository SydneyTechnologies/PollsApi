from django.contrib import admin
from .models import Poll, Option, Vote

# Register your models here.
admin.site.register(Poll)
admin.site.register(Option)
admin.site.register(Vote)

from django.contrib import admin
from .models import Clip, ClipVote, Category

# Register your models here.
admin.site.register(Clip)
admin.site.register(Category)
admin.site.register(ClipVote)
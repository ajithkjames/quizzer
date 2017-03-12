from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)
admin.site.register(School)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Attempt)
admin.site.register(TestEntries)
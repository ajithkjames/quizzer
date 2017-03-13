from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profile)
admin.site.register(School)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Attempt)
admin.site.register(TestEntries)
admin.site.register(City)
admin.site.register(Standard)



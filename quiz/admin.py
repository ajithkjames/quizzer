from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin
# Register your models here.



class CityResource(resources.ModelResource):

    class Meta:
        model = City

class CityAdmin(ImportExportModelAdmin):
    resource_class = CityResource

class QuestionResource(resources.ModelResource):

    class Meta:
        model = Question

class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource

class ChoiceResource(resources.ModelResource):

    class Meta:
        model = Choice

class ChoiceAdmin(ImportExportModelAdmin):
    resource_class = ChoiceResource

admin.site.register(City,CityAdmin)
admin.site.register(Profile)
admin.site.register(School)
admin.site.register(Quiz)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice,ChoiceAdmin)
admin.site.register(Attempt)
admin.site.register(TestEntries)
admin.site.register(Standard)
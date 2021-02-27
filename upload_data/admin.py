from django.contrib import admin
from .models import ParticipantData, Certificate
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.

class ParticipantResouce(resources.ModelResource):
    class Meta:
        model = ParticipantData
        fields = ('id', 'Full_Name', 'Event_Name', "Description")

class ParticipantDataAdmin(ImportExportActionModelAdmin):
    resource_class = ParticipantResouce



admin.site.register(ParticipantData, ParticipantDataAdmin)
admin.site.register(Certificate)
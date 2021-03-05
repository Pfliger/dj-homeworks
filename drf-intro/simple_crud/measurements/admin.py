from django.contrib import admin
from measurements.models import Project, Measurement


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass
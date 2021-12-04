from django.contrib import admin
from .models import State,District,Child,File
# Register your models here.



@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display=("state_name","id")

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display=("district_name","state_id")

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display=("name","sex","dob")

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display=("imageName","mimeType")
from django.contrib import admin
from .models import User, Patient, Staff

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_display_links = ('username',)
    
class PatientAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_display_links = ('username',)

admin.site.register(User, UserAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Staff, StaffAdmin)

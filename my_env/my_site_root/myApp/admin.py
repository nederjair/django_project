from django.contrib import admin
from .models import AppModel
# Register your models here.
class AppAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )

admin.site.register(AppModel, AppAdmin)
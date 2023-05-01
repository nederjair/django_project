from django.contrib import admin
from .models  import PageModel
# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'update_date')
    ordering = ('title', )
    search_fields = ('title', )

admin.site.register(PageModel, PageAdmin)
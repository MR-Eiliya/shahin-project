from django.contrib import admin
from mainapp.models import Contact, NewsLetter

class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ["name","lastname","phone","created_date"]
    search_fields = ["name","message"]
    
    
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(NewsLetter)
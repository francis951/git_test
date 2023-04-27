from django.contrib import admin
from .models import Candidate, Carrier
# Register your models here.

class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'carrier']
    search_fields = ['name', 'phone', 'email']
    list_per_page = 10


admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Carrier)
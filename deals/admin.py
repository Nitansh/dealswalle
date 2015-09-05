from django.contrib import admin
from .models import CustomerQuery

class CustomerQueryAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomerQuery, CustomerQueryAdmin)
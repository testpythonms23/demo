from django.contrib import admin
from .models import Branch,Customer
# Register your models here.

class BranchAdmin(admin.ModelAdmin):
    list_display = ['district','slug']
    prepopulated_fields = {'slug':('district',)}
admin.site.register(Branch,BranchAdmin)

admin.site.register(Customer)


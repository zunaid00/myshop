from django.contrib import admin
from . models import category,product
# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}


class productAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','price','stock','available','created','updated']
    list_filter = ['available','created','updated','category']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(category,categoryAdmin)
admin.site.register(product,productAdmin)
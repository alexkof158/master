from django.contrib import admin
from .models import CategoriaPro, Producto

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
admin.site.register(CategoriaPro, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
from django.contrib import admin

from . import models

#admin.site.register(models.ProductoCategoria)
@admin.register(models.ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre","descripcion")
    #list_display_links = ("nombre",)
    list_filter = ("nombre",)
    #list_editable = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)
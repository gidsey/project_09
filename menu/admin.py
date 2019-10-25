from django.contrib import admin
from .models import Menu, Item, Ingredient

admin.site.site_header = 'Soda Fountian Admin Aresa'


class MenuAdmin(admin.ModelAdmin):
    list_display = ['season', 'created_date', 'expiration_date']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'chef', 'created_date', 'standard']
    ordering = ['-name']


class IngredientAdmin(admin.ModelAdmin):
    ordering = ['-name']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Ingredient, IngredientAdmin)

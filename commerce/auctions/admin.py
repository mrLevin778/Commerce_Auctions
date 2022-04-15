from django.contrib import admin
from .models import Category, Auction


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class AuctionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['start_price', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Auction, AuctionAdmin)

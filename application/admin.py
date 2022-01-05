from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import *


class ImageGalleryInline(GenericTabularInline):

    model = ImageGallery
    readonly_fields = ('image_url',)


class ProductAdmin(admin.ModelAdmin):

    inlines = [ImageGalleryInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(ImageGallery)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Order)
from django.contrib import admin
from products.models import (
    Brand,Category,
)

admin.site.register(Brand)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    raw_id_fields = ['brand',]

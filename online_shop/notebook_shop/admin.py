from django.contrib import admin

from .models import Goods


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'type', 'description', 'image')


# admin.site.register(Good, GoodsAdmin)

from django.contrib import admin
from .models import Wish, CustomUser, WishList

class WishListAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_public', 'created_at')
    list_filter = ('is_public', 'created_at')
    search_fields = ('name', 'user__username', 'description')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Wish)
admin.site.register(CustomUser)
admin.site.register(WishList, WishListAdmin)
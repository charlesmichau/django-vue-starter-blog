from django.contrib import admin
from . import models

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name',
                    'last_name', 'email', 'date_joined')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'is_published', 'is_featured', 'created_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_approved', 'created_at')


admin.site.register(models.Site)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)

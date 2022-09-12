from django.contrib import admin
from .models import Product, Comment
# Register your models here.


"""
we can use StackedInline or TabularInline
"""
class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active']
    extra = 0

@admin.register(Product)
class CustomProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'active')

    inlines = [
        CommentsInline,
               ]

@admin.register(Comment)
class CustomComment(admin.ModelAdmin):
    list_display = ('product', 'author', 'body', 'stars', 'active')
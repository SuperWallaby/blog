from django.contrib import admin
from .models import Article, Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'article', 'date_comment', 'active')
    list_filter = ('active', 'date_comment')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        
admin.site.register(Article)

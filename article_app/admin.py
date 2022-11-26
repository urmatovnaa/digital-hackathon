from django.contrib import admin
from article_app.models import Article


@admin.register(Article)
class ContactsAdmin(admin.ModelAdmin):
    pass

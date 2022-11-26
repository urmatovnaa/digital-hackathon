from django.contrib import admin
from event_app.models import Category, Speaker, Event


@admin.register(Category)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(Speaker)
class ContactsAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class ContactsAdmin(admin.ModelAdmin):
    pass

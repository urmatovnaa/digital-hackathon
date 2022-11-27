from django.contrib import admin
from event_app.models import Category, Speaker, Event


@admin.register(Category)
class Contacts1Admin(admin.ModelAdmin):
    pass


@admin.register(Speaker)
class Contacts2Admin(admin.ModelAdmin):
    pass


@admin.register(Event)
class Contacts3Admin(admin.ModelAdmin):
    pass

from django.contrib import admin

from django.contrib.admin.options import TabularInline

from question_app.models import Question, Answer


class AnswerAdminInline(TabularInline):
    extra = 1
    model = Answer


@admin.register(Question)
class MainModelAdmin(admin.ModelAdmin):
    inlines = (AnswerAdminInline,)


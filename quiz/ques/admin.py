from django.contrib import admin
from .models import questions, choice

# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'qid')

admin.site.register(questions, QuestionAdmin)
admin.site.register(choice)

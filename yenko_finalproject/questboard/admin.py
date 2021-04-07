from django.contrib import admin

from .models import Questboard


class QuestboardAdmin(admin.ModelAdmin):
    model = Questboard


admin.site.register(Questboard, QuestboardAdmin)
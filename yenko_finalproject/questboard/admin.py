from django.contrib import admin

from .models import QuestCard


class QuestCardAdmin(admin.ModelAdmin):
    model = QuestCard


admin.site.register(QuestCard, QuestCardAdmin)
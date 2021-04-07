from django.contrib import admin

from .models import QuestBoard, QuestCard


class QuestBoardAdmin(admin.ModelAdmin):
    model = QuestBoard


class QuestCardAdmin(admin.ModelAdmin):
    model = QuestCard


admin.site.register(QuestBoard, QuestBoardAdmin)
admin.site.register(QuestCard, QuestCardAdmin)
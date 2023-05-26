from django.contrib import admin
from .models import Note
# Register your models here.


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
	list_display = ['body', 'update', 'created']
	list_filter = ['created', 'update']
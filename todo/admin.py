from django.contrib import admin
from .models import Todo, Tag

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)
admin.site.register(Tag)
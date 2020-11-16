from django.contrib import admin

from .models import Topic, Group, Student


def reset_likes(modeladmin, request, queryset):
    queryset.update(likes=0)


class GroupAdmin(admin.ModelAdmin):
    list_display = ['topic']
    ordering = ['topic']
    actions = [reset_likes]


admin.site.register(Topic)
admin.site.register(Group, GroupAdmin)
admin.site.register(Student)

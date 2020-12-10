from django.contrib import admin
from .models import Artwork, WrittenPiece


def reset_likes(queryset):
    queryset.update(likes=0)


def change_group_jaguars(querryset):
    for i in querryset:
        i.group.class_name = "Jaguars"
        i.save()


def change_group_iguanas(querryset):
    for i in querryset:
        i.group.class_name = "Iguanas"
        i.save()


class LikesAdmin(admin.ModelAdmin):
    actions = [reset_likes]


class StudentAdmin(admin.ModelAdmin):
    actions = [change_group_jaguars, change_group_iguanas]


admin.site.register(Artwork, LikesAdmin)
admin.site.register(WrittenPiece, LikesAdmin)

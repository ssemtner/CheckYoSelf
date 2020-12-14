from django.contrib import admin

from .models import Artwork, WrittenPiece, ArtworkComment


def reset_likes(queryset):
    queryset.update(likes=0)


def change_group_jaguars(queryset):
    for i in queryset:
        i.group.class_name = "Jaguars"
        i.save()


def change_group_iguanas(queryset):
    for i in queryset:
        i.group.class_name = "Iguanas"
        i.save()


class LikesAdmin(admin.ModelAdmin):
    actions = [reset_likes]


class StudentAdmin(admin.ModelAdmin):
    actions = [change_group_jaguars, change_group_iguanas]


admin.site.register(Artwork, LikesAdmin)
admin.site.register(WrittenPiece, LikesAdmin)
admin.site.register(ArtworkComment)

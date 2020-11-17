from django.contrib import admin
from .models import Artwork, WrittenPiece


def reset_likes(queryset):
    queryset.update(likes=0)


class LikesAdmin(admin.ModelAdmin):
    actions = [reset_likes]


admin.site.register(Artwork, LikesAdmin)
admin.site.register(WrittenPiece, LikesAdmin)

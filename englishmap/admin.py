from django.contrib import admin
from .models import Topic, Comment, Reply, LayoutRow, LayoutRow1

admin.site.register(Topic)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(LayoutRow)
admin.site.register(LayoutRow1)
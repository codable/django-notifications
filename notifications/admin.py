# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('actor',
                    'level', 'target', 'public')
    list_filter = ('level', 'public', 'timestamp', )

admin.site.register(Notification, NotificationAdmin)

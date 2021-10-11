# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'User'

    def ready(self):
        from User import signals

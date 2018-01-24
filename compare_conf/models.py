# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class test(models.Model):
    env_name = models.CharField(max_length=32)
    display_name = models.CharField(max_length=32)
    url_link = models.URLField(unique=True)

    def __str__(self):
        return self.env_name

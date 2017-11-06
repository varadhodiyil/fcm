# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Devices(models.Model):
	device_id = models.CharField(max_length=100,primary_key=True)
	token = models.CharField(max_length=250)
	updated_at = models.DateTimeField(auto_now=True)

class EventLog(models.Model):
	event = models.CharField(max_length=100)
	ip_address = models.GenericIPAddressField()
	updated_at = models.DateTimeField(auto_now=True)
	device = models.ForeignKey(Devices,on_delete=models.CASCADE)

class NotificationEvents(models.Model):
	"""Class which saves meta of notifications to be sent """
	id = models.AutoField(primary_key=True)
	event = models.CharField(max_length=100)

class Notified(models.Model):
	event = models.ForeignKey(NotificationEvents,on_delete=models.CASCADE)
	device = models.ForeignKey(Devices,on_delete=models.CASCADE)
	updated_at = models.DateTimeField(auto_now_add=False,auto_now=True)
	is_clicked = models.BooleanField(default=False)
	clicked_time = models.DateTimeField(default=None,null=True)
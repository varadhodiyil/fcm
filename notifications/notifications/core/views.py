# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from notifications.core import serializers
from rest_framework.parsers import JSONParser, FormParser
from notifications.core.models import Devices , Notified
from notifications.core.resoures import send_notification
from django.utils import timezone

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class Register(GenericAPIView):
	serializer_class = serializers.RegistrationSerializer
	parser_classes = (JSONParser,FormParser)
	def post(self,request,*args,**kwargs):
		data = request.data
		s = serializers.RegistrationSerializer(data=data)
		result = dict()
		if s.is_valid():
			s.save()
			result['status'] = True
		else:
			result['errors'] = s.errors
			result['status'] = False
		return Response(result)

class EventLog(GenericAPIView):
	serializer_class = serializers.EventLogSerializer
	parser_classes = (JSONParser,FormParser)
	def post(self,request,*args,**kwargs):
		data = request.data.copy()
		data['ip_address'] = get_client_ip(request)
		s = serializers.EventLogSerializer(data=data)
		result = dict()
		if s.is_valid():
			s.save()
			result['status'] = True
		else:
			result['errors'] = s.errors
			result['status'] = False
		return Response(result)

class Notify(GenericAPIView):
	serializer_class = serializers.NotifySerializer
	parser_classes = (JSONParser,FormParser)
	def post(self,request,*args,**kwargs):
		data = request.data
		
		s = serializers.NotifySerializer(data=data)
		result = dict()
		if s.is_valid():
			send_notification(s.validated_data)
			result['status'] = True
		else:
			result['errors'] = s.errors
			result['status'] = False
		return Response(result)

class UpdateNotified(GenericAPIView):
	serializer_class = serializers.UpdateNotified
	parser_classes = (JSONParser,FormParser)
	def post(self,request,*args,**kwargs):
		data = request.data
		s = serializers.UpdateNotified(data=data)
		result = dict()
		print data
		if s.is_valid():
			device = s.validated_data['token']
			event = s.validated_data['event']
			n = Notified.objects.filter(device_id ,event=event)
			n.is_clicked = True
			n.clicked_time = timezone.now()
			result['status'] = True
		else:
			result['errors'] = s.errors
			result['status'] = False
		return Response(result)
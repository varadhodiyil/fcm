from rest_framework import serializers
from notifications.core import models

class RegistrationSerializer(serializers.Serializer):
	device_id = serializers.CharField(max_length=100)
	token = serializers.CharField(max_length=250)
	def save(self):
		# print self.validated_data
		m , created = models.Devices.objects.get_or_create(device_id=self.validated_data['device_id'])
		m.token=self.validated_data['token']
		m.save()
	class Meta:
		fields = "__all__"

class EventLogSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.EventLog
		fields = ["device","event","ip_address"]

class NotifySerializer(serializers.Serializer):
	event = serializers.CharField(max_length=100)
	count = serializers.IntegerField(default=0)
	title = serializers.CharField(max_length=100)
	message = serializers.CharField(max_length=250)
	icon = serializers.URLField()
	navigate_to = serializers.URLField()
	class Meta:
		fields = "__all__"

class UpdateNotified(serializers.Serializer):
	device = serializers.CharField(max_length=100)
	is_clicked = serializers.BooleanField()
	clicked_time = serializers.DateTimeField()
	event = serializers.CharField(max_length=100)
	class Meta:
		fields = "__all__"

from pyfcm import FCMNotification
from notifications.core.models import EventLog , Notified ,Devices , NotificationEvents
from django.db.models import Count
def send_notification(data):
	push_service = FCMNotification(api_key="AIzaSyDIHYrkVm4U5zTva4Bk7BqBKRONtPiy1WA")
	extra_kwargs = {
    	'priority': 'high',
	}
	event = data['event']
	count = data['count']
	event = NotificationEvents(event=event)
	event.save()
	devices = EventLog.objects.values("device__token").annotate(event_count=Count('event')).filter(event__icontains=data['event'],event_count__gte=count)
	for d in devices:
		token = d['device__token']
		
		result = push_service.notify_single_device(registration_id=token, \
			message_icon=data['icon'] , message_body=data['message'],message_title=data['title'],\
			extra_kwargs=extra_kwargs,click_action=data['navigate_to'],tag=event.id)
		token_obj = Devices.objects.filter(token=token).get()
		Notified(event = event,device = token_obj ).save()

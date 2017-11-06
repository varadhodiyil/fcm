from pyfcm import FCMNotification
import json
push_service = FCMNotification(api_key="AIzaSyDIHYrkVm4U5zTva4Bk7BqBKRONtPiy1WA")


# OR initialize with proxies

proxy_dict = {
          "http"  : "http://127.0.0.1",
          "https" : "http://127.0.0.1",
        }
# push_service = FCMNotification(api_key="<api-key>")

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"

title  = message_title,
body = message_body,
logo = "https://pbs.twimg.com/profile_images/839721704163155970/LI_TRk1z_400x400.jpg"
extra_kwargs = {
    'priority': 'high',
}
registration_id = "clIhN18A1vk:APA91bHo9BMvwO6ZfyDpuBRhPASkdxQ68b15dfFf6-JzovvnFAl0BlP4x8J4eld9N4V1FYEd7Q3o7MwzhnEC74uRvuDzzLVyEReXxIIHOMyG8MtG1Be9x9cAiAwEkqZkDxI8Qkl2ujuM"



result = push_service.notify_single_device(registration_id=registration_id, message_icon=logo , message_body=body,message_title=message_title,extra_kwargs=extra_kwargs,click_action="https://google.com")

# # Send to multiple devices by passing a list of ids.
# registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
# message_title = "Uber update"
# message_body = "Hope you're having fun this weekend, don't forget to check today's news"
# result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)

print json.dumps(result)
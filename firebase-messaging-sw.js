// Import and configure the Firebase SDK
// These scripts are made available when the app is served or deployed on Firebase Hosting
// If you do not serve/host your project using Firebase Hosting see https://firebase.google.com/docs/web/setup
importScripts('https://www.gstatic.com/firebasejs/4.6.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/4.6.0/firebase-messaging.js');
importScripts('/scripts/fingerprint.js');
// importScripts('/scripts/jquery-3.2.1.js');
// importScripts('https://www.gstatic.com/firebasejs/4.6.0/init.js');
const apiURL = "http://127.0.0.1:8000/"
firebase.initializeApp({
	'messagingSenderId': '550151811080'
  });
  const messaging = firebase.messaging();

// [START background_handler]
messaging.setBackgroundMessageHandler(function(payload) {
//   console.log('[firebase-messaging-sw.js] Received background message ', payload);
  // Customize notification here
  var notificationTitle = JSON.stringify(payload.data);
  var notificationOptions = {
					body:payload.data.body,
                    icon:payload.data.icon,
					image:payload.data.image,
					tag:payload.data.tag,
					requireInteraction:true,
					badge:payload.data.badge
  }; 
   return self.registration.showNotification(JSON.stringify(payload),notificationOptions);
});
// [END background_handler]
self.addEventListener('notificationclick', function(event) {
	//console.log('Notification click: action', event);
   event.notification.close();
	var tagUrl = event.notification.badge;
	//console.log('Notification action - CTA : ', event);
	//var url = event.notification.tag;
	var url;
	if (event.notification.badge ==='' || typeof event.notification.badge === 'undefined') {
	  url = 'http://localhost';
	} else {
	  url = event.notification.badge;
	}
	var data = {};
	data.device_id = new Fingerprint().get();
	data.event = event.notification.tag;
	var xhr = new XMLHttpRequest();
	xhr.open('POST', apiURL+"update_notify/", true);
	xhr.onload = function () {
		event.waitUntil(
			Promise.all([
				clients.matchAll({
				type: 'window'
				}).then(function(windowClients) {
				console.log('WindowClients', windowClients);
				for (var i = 0; i < windowClients.length; i++) {
					var client = windowClients[i];
					console.log('WindowClient', client);
					if (client.url === url && 'focus' in client) {
					return client.focus();
					}
				}
				if (clients.openWindow) {
					return clients.openWindow(url);    
				}
				}),
			//   self.analytics.trackEvent('notification-click',11)
			])
		);
	};
	xhr.send(data);
	
  });
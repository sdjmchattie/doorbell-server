#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from paho.mqtt.publish import single

BROKER_URL = "127.0.0.1"

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path == '/'):
            self.send_doorbell_mqtt()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('Doorbell Chime Acknowledged', 'UTF-8'))

    def send_doorbell_mqtt(self):
        """Send an MQTT message to BROKER_URL on the doorbell topic.
        """
        single("doorbell", hostname=BROKER_URL)

print('Doorbell chime HTTP service, ready.')
HTTPServer(('0.0.0.0', 15927), RequestHandler).serve_forever()

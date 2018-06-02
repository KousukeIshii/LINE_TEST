from django.shortcuts import render
from django.http import HttpResponse


	REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
	ACCESS_TOKEN = "nEv5t8dy06W+UT3NVcK7OPiEgDbXCTwswcBn0GgkflmT6SMZ1fZWYM3mp8tM3a5TIcZGWh3iA1U1N1iQ4kHoTByBD156IetsDIGqGcgOaEN0WL3lO3faf2ShLBBZpvvAbtE7E5EFbsc6wrXFtbR3mgdB04t89/1O/w1cDnyilFU="
	HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + ACCESS_TOKEN
	}
	
# Create your views here.
def index(request):
    return HttpResponse("This is bot api.")

def callback(request):
	reply = ""
    request_json = json.loads(request.body.decode('utf-8'))
    for events in request_json['events']:
        reply_token = events['replyToken']
        message_type = events['message']['type']

        if message_type == 'text':
            reply = {
            	"replyToken":reply_token
            	"message":[
            		{
            			"type":"text"
            			"text":events['message']['text']
            		}
            	]
            }
            requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(reply))
            


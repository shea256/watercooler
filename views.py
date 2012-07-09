import json
import OpenTokSDK
from django.template import RequestContext
from django.shortcuts import render_to_response
from chats.models import User, Chat, Interest

idx = 0

def home(request):
    return render_to_response('home.html')
    #facebook_profile = request.user.get_profile().get_facebook_profile()
    #return render_to_response('home.html', {'facebook_profile': facebook_profile},
    #                                        context_instance=RequestContext(request))
def landing(request):
	global idx
	idx = idx + 1
	chat = Chat()
	chat.save()
	user = chat.user_set.create(email = 'suleimenov'+str(idx)+'@gmail.com', facebookId = 10100409621467214 + idx)
	user.save()
	return render_to_response('landing.html', { 'chat_id':chat.session_id });

def meeting(request):
# N.B. GET needs to contain userID, chatID

# check if session already exists for chatID
	this_chat_id = int(request.GET['chat_id'])
	print this_chat_id
	chat = Chat.objects.get(pk=1)
	api_key = "7442182"
	api_secret = "f264a8c22128f807c2a9e148b6457a66d7fd63cc"
	opentok_sdk = OpenTokSDK.OpenTokSDK(api_key, api_secret)
	
	if (Chat.objects.all().count() == 1):
		# session not created, so create a new session
		session = opentok_sdk.create_session(request.META['REMOTE_ADDR'])
		session_id = session.session_id
	else:
		chat = Chat.objects.get(pk=1)
		session_id = chat.session_id
	
	# api_key = "7442182"
	# api_secret = "f264a8c22128f807c2a9e148b6457a66d7fd63cc"
	# opentok_sdk = OpenTokSDK.OpenTokSDK(api_key, api_secret)
	# session = opentok_sdk.create_session(request.META['REMOTE_ADDR'])
	# session_id = session.session_id
	
	token = opentok_sdk.generate_token(session_id)
	
# set up OpenTok
	# create session
	return render_to_response('session.html', 
		{'api_key': api_key, 
		 'session_id': session_id, 
		 'token': token})

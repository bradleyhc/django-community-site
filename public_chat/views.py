from django.shortcuts import render

# Create your views here.

t = 'public_chat'

def index(request):
    return render(request, t+'/index.html')


def room(request, room_name):
    return render(request, t+'/chat_room.html', {
        'room_name': room_name
    })
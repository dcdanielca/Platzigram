from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'title': 'Dunkelheit',
        'user': {
            'name': 'Varg Vikernes',
            'picture': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Varg_Vikernes-2.jpg/250px-Varg_Vikernes-2.jpg'
        },
        'timestamp': datetime.now().strftime("%b, %dth, %Y -%H:%M hrs"),
        'photo': 'http://tageslichtlampe-testbericht.de/wp-content/uploads/warum_macht_dunkelheit_krank.jpg',
    },
    {
        'title': 'Iowa',
        'user':{
            'name': 'Corey Taylor',
            'picture': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Corey_Taylor_of_Slipknot_at_Optimus_Alive_Festival_2009_2.jpg/250px-Corey_Taylor_of_Slipknot_at_Optimus_Alive_Festival_2009_2.jpg'
        },
        'timestamp': datetime.now().strftime("%b, %dth, %Y -%H:%M hrs"),
        'photo': 'https://www.planetware.com/photos-large/USIA/iowa-farm.jpg'
    },
    {
        'title': 'Vacaciones',
        'user': {
            'name': 'Dario Bennedetto',
            'picture': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/InddelVal-Boca_%2811%29.jpg/245px-InddelVal-Boca_%2811%29.jpg'
        },
        'timestamp': datetime.now().strftime("%b, %dth, %Y -%H:%M hrs"),
        'photo': 'https://www.prozesa.com/wp-content/uploads/2018/08/playa-vacaciones-pareja-hotel-600x400.jpg'
    }
]

def list_posts(request):
    return render(request, 'posts/feed.html', {'posts': posts})
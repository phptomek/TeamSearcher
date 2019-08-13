from django.shortcuts import render


posts = [
    {
        'author': 'Player4',
        'game': 'Dota 2',
        'content': 'Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum ',
        'link': 'steamcommunity.com/user=Player4',
        'date_posted': 'August 14, 2019'
    },
    {
        'author': 'Player7',
        'game': 'Rocket League',
        'content': 'Looking for mate to play 2s',
        'link': 'steamcommunity.com/user=Player7',
        'date_posted': 'August 18, 2019'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'post/home.html', context)


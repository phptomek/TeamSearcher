from django.shortcuts import render


posts = [
    {
        'author': 'Player4',
        'game': 'Dota 2',
        'content': 'Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum ',
        'link': 'https://steamcommunity.com/profiles/76561198325967622',
        'date_posted': 'August 14, 2019'
    },
    {
        'author': 'Player7',
        'game': 'Rocket League',
        'content': 'Looking for mate to play 2s',
        'link': 'https://steamcommunity.com/profiles/76561198325967622',
        'date_posted': 'August 18, 2019'
    },
    {
        'author': 'Mateuszto',
        'game': 'Rocket League',
        'content': 'Looking for mate to play 3s. Rank Diamond 3 - Add me on steam!',
        'link': 'https://steamcommunity.com/profiles/76561198325967622',
        'date_posted': 'August 21, 2019'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'post/home.html', context)


from django.shortcuts import render

def home_page(request, *args, **kwargs):
    context = {
        'temps': [
            {
                'time':'5AM',
                'temp':'55C'
            },
            {
                'time':'6AM',
                'temp':'58C'
            },
            {
                'time':'7AM',
                'temp':'59C'
            },
            {
                'time':'8AM',
                'temp':'53C'
            },
            {
                'time':'9AM',
                'temp':'51C'
            },
        ],
    }
    return render(request, 'index.html', context)
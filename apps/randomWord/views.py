from django.shortcuts import render, redirect
import random
import string

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    randomW = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
    context = {
        'randomstring' : randomW,
        'counter': request.session['counter']
    }
    return render(request, 'randomWord/index.html', context )

def new(request):
    return redirect('/')


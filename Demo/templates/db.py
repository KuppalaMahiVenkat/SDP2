from django.http import HttpResponse, HttpResponseRedirect, Http404

def loginval(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
        name='mahi@gmail.com'
        password='puli'
        if request.method=='POST':
            if request.POST.get('username') and request.POST.get('pass'):
                return HttpResponseRedirect('/you-are-logged-in/')
            else:
                return HttpResponseRedirect('invalid')
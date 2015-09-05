from django.shortcuts import render
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from django.core.mail import EmailMessage

from .forms import QueryForm

def iles_view(request):
   return render(request, 'ilets.html');

def privacy_view(request):
   return render(request, 'privacy.html');

def aboutus_view(request):
   return render(request, 'aboutus.html');

def contactus_view(request):
   return render(request, 'contactus.html');

def home_view(request):
    form = QueryForm()
    
    if request.POST:
        form = QueryForm(request.POST)
        if form.is_valid():
            messgae  = 'Name : ' + form.cleaned_data['full_name'] + ' Phone Number : ' + form.cleaned_data['phone_number'] + ' email ' + form.cleaned_data['email']
            email = EmailMessage('New User Saved the Information', messgae , to=['infotechviyan@gmail.com'])
            email.send()
            form.save()
            return redirect('/call_us')

    return render_to_response('index.html',{
        'form': form},context_instance=RequestContext(request))
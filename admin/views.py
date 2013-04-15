# Create your views here.
from django.shortcuts import render_to_response
from admin.forms import UserForm
from admin.forms import RoleForm
from django.template import RequestContext
from admin.models import User

def user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            userValue = form.cleaned_data
            print userValue['name']
            print userValue
            user=User(name=userValue['name'],email=userValue['email'],description=userValue['description'])
            user.save()
    else:
        form = UserForm()
    return render_to_response('user.html', {'form': form},context_instance=RequestContext(request))


def role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RoleForm()
    return render_to_response('user.html', {'form': form},context_instance=RequestContext(request))


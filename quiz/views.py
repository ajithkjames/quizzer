from django.http import HttpResponse, Http404
from django.shortcuts import render,get_object_or_404,render_to_response
from django.views.generic import View
from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from.models import *
from.forms import *

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

@login_required
def HomeView(request):
	if hasattr(request.user, 'profile'):
		profile=Profile.objects.get(user=request.user)
		if profile.account_type==0:
			return redirect('/student/home')
		else:
			return redirect('/teacher/home')
	else:
		return redirect('/create-profile')

def create_profile(request):
	if not request.user.is_authenticated():
		return render(request, '/')
	else:
		form = ProfileForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.user = request.user
			profile.avatar = request.FILES['avatar']
			file_type = profile.avatar.url.split('.')[-1]
			file_type = file_type.lower()
			if file_type not in IMAGE_FILE_TYPES:
				context ={
				    'profile': profile,
				    'form': form,
				    'error_message': 'Image file must be PNG, JPG, or JPEG',
				}
				return render(request, 'createprofile.html', context)
			profile.save()
			return redirect('/profile')
		context = {
			"form": form,
		}
		return render(request, 'createprofile.html', context)

def Profile_view(request):
	profile=Profile.objects.get(user=request.user)
	context = {
		"profile": profile,
	}
	return render(request, 'profile.html', context)
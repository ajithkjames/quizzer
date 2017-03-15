from django.http import HttpResponse, Http404
from django.shortcuts import render,get_object_or_404,render_to_response
from django.views.generic import View
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from datetime import datetime
from.models import *
from.forms import *
from .mixins import *

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

class Signup(View):
	template_name = "signup.html"
	def __init__(self, **kwargs):
		pass

	def get(self, request):
		return render(request, self.template_name)
	
	def post(self, request):
		try:
			first_name = request.POST.get("first_name")
			last_name = request.POST.get("last_name")
			email = request.POST.get("email")
			raw_password = request.POST.get("password")
			new_user = User.objects.create_user(email, first_name= first_name, last_name = last_name, email = email)
			new_user.set_password(raw_password)
			new_user.save()
			login(self.request, new_user)
		except:
			return redirect('/')
		return redirect('/')

@login_required
def HomeView(request):
	if hasattr(request.user, 'profile'):
		profile=Profile.objects.get(user=request.user)
		if profile.account_type==0:
			return redirect('/quiz/student-home')
		else:
			return redirect('/quiz/teacher-home')
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

@login_required
def Profile_view(request):
	profile=Profile.objects.get(user=request.user)
	context = {
		"profile": profile,
	}
	return render(request, 'profile.html', context)


class edit_profile(LoginRequiredMixin, UpdateView):
	model = Profile
	template_name= 'profile_form.html'
	fields = ['avatar','school','standard','phone']


class StudentHome(LoginRequiredMixin, generic.ListView):
	template_name= 'student-home.html'

	def get_queryset(self):
		return Quiz.objects.filter(start__lte=datetime.now(),end__gte=datetime.now())

class QuizDetailsView(LoginRequiredMixin, View):
	template_name= 'quiz-details.html'      
	def get(self, request, pk):
		quiz=Quiz.objects.get(pk=pk)
		try:
			attempt=Attempt.objects.get(quiz=quiz,user=request.user)
			return render(request, self.template_name, {'object': quiz,'attempt':attempt})
		except Exception as e:
			print e
		return render(request, self.template_name, {'object': quiz})

class testprogress(LoginRequiredMixin,View):
	template_name= 'quiz-ongoing.html'

	def get(self, request, pk):
		quiz=Quiz.objects.get(pk=pk)
		try:
		    done=Attempt.objects.get(quiz=quiz,user=request.user)
		except Exception as e:
			print e
			done=''
		questions=[]
		question=Question.objects.filter(quiz=pk).order_by('created_at')
				
		return render(request, self.template_name, {'questions': question,'done':done})

	def post(self, request, pk):
		quiz=Quiz.objects.get(pk=pk)
		attempt=Attempt(quiz=quiz)
		attempt.user=request.user
		attempt.save()
		my_data = request.POST
		attempt=Attempt.objects.get(quiz=quiz,user=request.user)
		print my_data
		del my_data['csrfmiddlewaretoken']
		for key, value in my_data.iteritems():
			question=Question.objects.get(id=key)
			answer=Choice.objects.get(id=value)
			testentry=TestEntries(attempt=attempt,question=question,answer=answer)
			testentry.save()
		return redirect('/quiz/myresults')

class result(LoginRequiredMixin,View):
	template_name= 'result.html'

	def get(self, request, pk):
		attempt=Attempt.objects.get(pk=pk)
		totalmarks=attempt.quiz.question_set.all().count()
		entries=TestEntries.objects.filter(attempt=attempt).order_by('-created_at')
		mark=0
		for entry in entries:
			if entry.answer.is_correct==True:
				mark+=1
			
		return render(request, self.template_name, {'entries': entries,'mark':mark,'totalmarks':totalmarks})


class myresults(LoginRequiredMixin,View):
	template_name= 'myresults.html'

	def get(self, request):
		attempt=Attempt.objects.filter(user=request.user)
	
		return render(request, self.template_name, {'attempt': attempt})


class TeacherHome(ProtectedTeacherView, generic.ListView):
	template_name= 'teacher-home.html'

	def get_queryset(self):
		return Quiz.objects.filter(author=self.request.user)


class AllAttempts(LoginRequiredMixin,View):
	template_name= 'allattempts.html'

	def get(self, request, pk):
		attempts=Attempt.objects.filter(quiz=pk).order_by('-created_at')
		return render(request, self.template_name, {'attempts': attempts})

class LeaderBoard(LoginRequiredMixin, generic.ListView):
	template_name= 'leader-board.html'

	def get_queryset(self):
		return Quiz.objects.all()

class QuizLeaders(LoginRequiredMixin,View):
	template_name= 'leaders.html'

	def get(self, request, pk):
		
		a=sorted(Attempt.objects.filter(quiz=pk), key=lambda t: -t.marks)
		return render(request, self.template_name, {'attempts': a})


@login_required
def CreateQuiz(request):
	form = QuizForm(request.POST)
	if hasattr(request.user, 'profile'):
		if request.method == 'POST':
			
				
				if form.is_valid():
					quiz = form.save(commit=False)
					quiz.author = request.user
					quiz.save()
					return redirect('/')
				context = {
					"form": form,
				}
				return render(request, 'create-quiz.html', context)
	else:
		return redirect('/create-profile')
	context = {'form': form}
	return render(request, 'create-quiz.html', context)



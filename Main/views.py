from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.template import *
from .models import Lectures
from .forms import LecturesForm

# Create your views here.


def dashboard(request):
	ai = Lectures.objects.filter(course="ai").order_by('lecture_no')
	web = Lectures.objects.filter(course="web").order_by('lecture_no')
	oop = Lectures.objects.filter(course="oop").order_by('lecture_no')
	multimedia = Lectures.objects.filter(course="multimedia").order_by('lecture_no')
	softeng = Lectures.objects.filter(course="softeng").order_by('lecture_no')
	db_apps = Lectures.objects.filter(course="db_apps").order_by('lecture_no')
	mod_sim = Lectures.objects.filter(course="mod_sim").order_by('lecture_no')

	return render(request, "dashboard.html", {"user_agent": request.user_agent, "ai": ai, "web": web,
	"oop": oop, "multimedia": multimedia, "softeng": softeng, "db_apps": db_apps, "mod_sim": mod_sim})

def index(request):
    if request.method == "POST":
        return redirect('dashboard')

    return render(request, "index.html", {"user_agent": request.user_agent})

def _login_(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			user = request.user.username
			messages.success(request, f"welcome admin %s !"%user)
			return redirect('panel')
		else:
			messages.error(request, f"هوووووووووووووووووووووووووووووي")
			return redirect('login')

	if request.user.is_authenticated:
		return redirect('panel')

	return render(request, 'login.html', {"user_agent": request.user_agent})


def panel(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			if(request.POST):
				lec_na = request.POST['lec_na']
				lec_no = request.POST['lec_no']
				course = request.POST['category']
				if(lec_na and lec_no):
					pdf = request.POST['pdf']
					ppt = request.POST['ppt']
					word = request.POST['word']
					video = request.POST['video']

					if not pdf:
						pdf = "0"

					if not ppt:
						ppt = "0"

					if not video:
						video = "0"

					if not word:
						word = "0"

					form = LecturesForm({'course': course,'lecture_no': lec_no, 'lecture_na': lec_na, 'pdf': pdf, 'ppt': ppt,'word': word, 'video': video})

					if form.is_valid():
						messages.success(request, f"lecture %s %s is successfully added to %s course"%(lec_na, lec_no, course))
						form.save()
						return redirect('panel')
					else:
						messages.error(request, f"form is not valid!")
						messages.error(request, f"leave the link fields empty & submit the lecture, then go & edit it and paste the link in the required field & update the lecture, it should work!")
						return redirect('panel')

				else:
					messages.error(request, f"please enter a name and a number for the lecture")
					return redirect('panel')
		else:
			courses = Lectures.objects.order_by('course','lecture_no')

			return render(request, "panel.html", {"user_agent": request.user_agent, "courses": courses})

	return redirect('index')

def _update_(request, lecture_id):
	if not request.user.is_authenticated:
		return redirect('index')

	if request.method == "POST":
		lecture = Lectures.objects.get(pk=lecture_id)
		lecture_old = lecture.course + " -> " + lecture.lecture_na + " " + str(lecture.lecture_no)

		lecture.lecture_na = request.POST['lec_na']
		lecture.course = request.POST['category']
		lecture.lecture_no = request.POST['lec_no']
		lecture.pdf = request.POST['pdf']
		lecture.ppt = request.POST['ppt']
		lecture.word = request.POST['word']
		lecture.video = request.POST['video']

		if not lecture.pdf:
			lecture.pdf = "0"

		if not lecture.ppt:
			lecture.ppt = "0"

		if not lecture.word:
			lecture.word = "0"

		if not lecture.video:
			lecture.video = "0"

		lecture.save()
		messages.success(request, f"'{lecture_old}' was updated! ")

		return redirect('panel')
	else:
		lecture = Lectures.objects.get(pk=lecture_id)
		messages.warning(request, f"fill all important fields cause it will be saved if its empty or not")
		return render(request, "update.html", {"user_agent": request.user_agent, "lecture": lecture})

def _logout_(request):
	if request.user.is_authenticated:
		user = request.user.username
		messages.success(request, f"see you later admin '{user}'")
		logout(request)
		return redirect('index')
	else:
	    return redirect('index')

def delete_lecture(request, lecture_id):
	lecture = Lectures.objects.get(pk=lecture_id)
	lecture.delete()
	messages.success(request, f"course -> '{lecture.course}' lecture '{lecture.lecture_na} {lecture.lecture_no}'  successfully deleted!")

	return redirect('panel')

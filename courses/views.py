from django import views
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from courses.models import Course, Video
from courses.forms import RegistrationForm, LoginForm


class HomeView(View):
    def get(self, request):
        courses = Course.objects.all()
        context = {
            'courses': courses,
        }

        return render(request, 'courses/home.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class SignupView(View):
    template_name = 'courses/signup.html'
    success_url = 'courses:login'

    def get(self, request):
        form = RegistrationForm()
        context = {
            'form': form,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationForm(request.POST)

        if not form.is_valid():
            context = {
                'form': form,
            }

            return render(request, self.template_name, context)

        user = form.save()

        if user is not None:
            return redirect(self.success_url)


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    template_name = 'courses/login.html'
    success_url = 'courses:home'

    def get(self, request):
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = LoginForm(request=request, data=request.POST)

        if not form.is_valid():
            context = {
                'form': form,
            }

            return render(request, self.template_name, context)

        return redirect(self.success_url)


class SignoutView(View):
    def get(self, request):
        logout(request)

        return redirect('courses:home')


def coursePage(request, slug):
    course = Course.objects.get(slug=slug)
    serial_number = request.GET.get('lecture')
    videos = course.video_set.all().order_by("pk")

    if serial_number is None:
        video = Video.objects.filter(course=course).first()
    else:
        stuff = serial_number.replace('-', ' ')
        video = Video.objects.get(title=stuff, course=course)

    if ((request.user.is_authenticated is False) and (video.is_preview is False)):
        return redirect('courses:login')

    context = {
        'course': course,
        'video': video,
        'videos': videos,
    }

    return render(request, 'courses/course_page.html', context)

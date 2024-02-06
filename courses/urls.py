from django.urls import path
from courses import views


app_name = 'courses'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signout/', views.SignoutView.as_view(), name='signout'),
    path('course/<str:slug>/', views.coursePage, name='course_page'),
]

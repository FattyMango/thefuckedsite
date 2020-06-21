from django.urls import path
from home import views

urlpatterns = [
	path("", views.HomeView , name="home"),
	path("YourAss", views.Ass , name="ass"),
	path("YourLife", views.Life , name="life"),
	path("YourGPA", views.GPA , name="gpa"),
	path("YourMusicTaste", views.Taste, name="taste"),

]
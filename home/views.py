from django.shortcuts import render


# Create your views here.
def HomeView (request):
	lel={}
	context=["YourAss","YourLife","YourGPA","YourMusicTaste"]

	lel['hm']=context

	return render(request,"lel/home.html",lel)

def Ass (request):
	return render(request,"FuckedList/YourAss.html",)

def GPA (request):
	return render(request,"FuckedList/YourGPA.html",)

def Life (request):
	return render(request,"FuckedList/YourLife.html",)

def Taste (request):
	return render(request,"FuckedList/YourMusicTaste.html",)
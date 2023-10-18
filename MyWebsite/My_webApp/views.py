from django.shortcuts import render



# Create your views here.
def homepage(requesi):
    return render(requesi, 'homepage.html')

def about_me(request):
    return render(request, 'AboutMe.html')

def contact(request):
    return render(request, 'contact.html')  

def skills(request):
    return render(request, 'skills.html') 



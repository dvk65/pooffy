from django.shortcuts import render
from .models import Destination
def index(request):
    
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog_home(request):
    return render(request,'blog-home.html')

def blog_single(request):
    return render(request,'blog-single.html')

def cats(request):
    dest1 = Destination()
    dest1.name='Rabbit'
    dest1.breed='white fluff'
    dest1.desc='Back injury. Loves neck scratches. Plops at own wish. Scared to show too much love.'
    dest1.img='whitefloof.jpg'
    
    dest2 = Destination()
    dest2.name='Salty'
    dest2.breed='Ochre fluff'
    dest2.desc='Ankle injury. Loves neck, whisker scratches. Plops at own wish. Copies Rabbit.'
    dest2.img ='small_white_floof.jpg'
    #dest2.offer='False'

    cats_all=[dest1,dest2]
    return render(request, 'cats.html', {'cats_all':cats_all})

def dogs(request):
    return render(request,'dogs.html')

def contact(request):
    return render(request,'contact.html')

def elements(request):
    return render(request,'elements.html')

def volunteer(request):
    return render(request,'volunteer.html')

def adoptee(request):
    return render(request,'adoptee.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def adoptee(request):
    return render(request,'adoptee.html')
# Create your views here.

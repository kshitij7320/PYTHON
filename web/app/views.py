from django.shortcuts import render
from app.forms import Contactform
# Create your views here.
def index(request):
    con = Contactform()
    return render(request,'index.html',{'form':con})
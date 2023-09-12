from django.shortcuts import render, get_object_or_404
from . models import blog, side_photos, side_bar

# Create your views here.

def home(request):
    obj=blog.objects.all()  #storing data from blog class (table)
    obj1=side_photos.objects.all()
    obj2=side_bar.objects.all()
    return render(request,'index.html',{'data':obj,'data1':obj1,'data2':obj2}) #storing all data in obj(variable) to data(key)

def about(request):
    return render(request,'about-us.html')

def contact(request):
    return render(request,'contact.html')

def single(request,id):
    obj3=get_object_or_404(blog, pk=id)
    return render(request,'single-post.html',{'obj':obj3})



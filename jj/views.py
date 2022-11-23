from django.shortcuts import render,HttpResponse
from jj.models import post,posts,event,train

def jj(request):
       allpost=post.objects.all()
       context={'allposts':allpost}
       return render(request,'index.html',context)

def events(request):
       allpost=event.objects.all()
       context={'allposts':allpost}
       return render(request,'events.html',context)
       
def about(request):
       allpost=posts.objects.all()
       context={'allposts':allpost}
       return render(request,'about.html',context)

def course(request):
   
       return render(request,'course.html')

def cou(request):
  
       return render(request,'cou.html')

def contact(request):
    
       return render(request,'contect.html')


def trainer(request):
       allpost=train.objects.all()
       context={'allposts':allpost}
       return render(request,'trainer.html',context)





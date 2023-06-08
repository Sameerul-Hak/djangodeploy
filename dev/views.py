from django.shortcuts import render,redirect
from dev.models import Post,Comments
from dev.forms import Form
# Create your views here.
def home(request):
    posts=Post.objects.all()

    return render(request,"dev/index.html",{"posts":posts})

def particularpost(request,pk):
    postpar=Post.objects.get(id=pk)
    comments=Comments.objects.filter(post=postpar)
    print(comments)
    return render(request,"dev/particularpost.html",{"post":postpar,"comments":comments})


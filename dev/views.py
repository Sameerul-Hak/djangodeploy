from django.shortcuts import render,redirect
from dev.models import Post,Comments
from dev.forms import Form
# Create your views here.
def home(request):
    posts=Post.objects.all()

    return render(request,"dev/index.html",{"posts":posts})

def particularpost(request,pk):
    postpar=Post.objects.get(id=pk)
    if request.method=="POST":
        comment=Form(request.POST)
        if comment.is_valid():
            comm=comment.save(commit=False)
            comm.user=request.user
            comm.post=postpar
            comm.save()
            
            return redirect('home')
    comment=Form()
    comments=Comments.objects.filter(post=postpar)
    return render(request,"dev/particularpost.html",{"post":postpar,"comments":comments,'form':comment})


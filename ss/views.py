from django.shortcuts import render
from .models import Member
from .forms import Memberform
# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Memberform(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            print('*'*25)
            
        else:
            print(form.errors)
    return render(request,'index.html',{})

def result(request):
    all_member = Member.objects.all
        
    return render(request,'result.html',{'all': all_member})

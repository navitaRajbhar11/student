from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserForm
from .models import User

# Create your views here.

def add(request):
    if request.method == "POST":
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("form submit suceessful")
            return redirect('show')
        else:
            print("error",form.errors)
    else:
        form = UserForm() #form.py
    return render(request, 'enroll/add.html',{"forms":form})

def show(request):
    student = User.objects.all() #model.py
    return render(request,'enroll/show.html',{"student":student})
 
def update(request,id):
    edit = get_object_or_404(User, pk=id)
    
    if request.method == 'POST':
        edit = User.objects.get(pk=id)
        form_edit = UserForm(request.POST,request.FILES,instance=edit)
        if form_edit.is_valid():
            form_edit.save()
            return redirect('show')
    else:
        form_edit = UserForm(instance=edit)
    return render(request, 'enroll/update.html',{'form_edit':form_edit})
   

def delete(request,id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        data.delete()
    return redirect('/')


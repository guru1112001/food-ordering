from django.shortcuts import render,redirect
from .models import Customer
from .forms import CreateUserForm
from django.contrib import messages



# Create your views here.
def RegisterPage(request):
    form=CreateUserForm()
    if request.method == "POST":
        form= CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            messages.success(request,f"Your Account has been created! you are now able to log-in")
            return redirect("login")
    
    else:
        form=CreateUserForm()
    return render(request,"account/register.html",{"form":form})



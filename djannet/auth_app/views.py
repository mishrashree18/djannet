from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import RegisterForm


@csrf_exempt
def register_user(request):
    #view for registering user 
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect("/login")

    else: 
        form = RegisterForm()
        
    return render(request, "auth_app/register.html", {'form': form,})
        
        
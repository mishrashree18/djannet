from django.shortcuts import render, redirect


def home_page(request):
    #homepage of the app 
    if request.user.is_authenticated: 
        context = {
            'username' : request.user.username, 
            'email' : request.user.email, 
            'pk' : request.user.pk,
        }
        return render(request, "djannet_app/homepage.html", context)

    return redirect("/login")

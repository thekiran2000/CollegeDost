from django.shortcuts import render, HttpResponse, redirect
# from home.models import Contact
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
# from blog.models import Post


def home(request):
    return render(request, "logiin.html")
def index(request):
    return render(request, "signup.html")


def handleSignUp(request):

    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
         # check for errorneous input
        if len(username)<10:
            # messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            # messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')

        if (pass1!= pass2):
            #  messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=username
        myuser.save()
        # messages.success(request, " Your iCoder has been successfully created")
        print("hello")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user=authenticate(username= loginusername, password= loginpassword)
        print(user)
        print("hello")
        if user is not None:
            login(request, user)

            print("yup")
            messages.success(request, "Successfully Logged In")
            return render(request, 'logiin.html')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            print("hello")
            return redirect('home')

    return HttpResponse("404- Not founddsfdsfsdfsdfsfsdfsfdsf")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


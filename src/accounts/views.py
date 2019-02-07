from django.http import HttpResponse
from django.views.generic import CreateView, FormView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login , get_user_model
from django.utils.http import is_safe_url

from .forms import LoginForm , RegisterForm, GuestForm
from .models import GuestEmail
from .signals import user_logged_in

# Create your views here.

def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        "form":form
    }
    next = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next or next_post or None
    if form.is_valid():
        email           = form.cleaned_data.get("email")
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect("/register")

    return redirect("/register")

class LoginView(FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/login.html'

    def form_valid(self,form):

        request = self.request
        next = request.GET.get('next')
        next_post = request.POST.get('next')
        redirect_path = next or next_post or None
        print(form)

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=email , password=password)
        print('current user for email: ' + email  + ' password: ' + password + 'is')
        print(user)
        #print(request.user.is_authenticated())
        if user is not None:
            login(request, user)
            user_logged_in.send(user.__class__,instance=user,request=request)
            print('check safe')
            print(redirect_path)
            if is_safe_url(redirect_path, request.get_host()):
                print('safe url')
                return redirect(redirect_path)
            else:
                print('not safe url')    
                return redirect("/")
        
        return super(LoginView,self).form_invalid(form)


# def login_page(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         "form":form
#     }
#     next = request.GET.get('next')
#     next_post = request.POST.get('next')
#     redirect_path = next or next_post or None
#     if form.is_valid():

#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(request,username=username , password=password)
#         print(user)
#         #print(request.user.is_authenticated())
#         if user is not None:
#             login(request, user)
#             print('check safe')
#             print(redirect_path)
#             if is_safe_url(redirect_path, request.get_host()):
#                 print('safe url')
#                 return redirect(redirect_path)
#             else:
#                 print('not safe url')    
#                 return redirect("/")
#         else:
#             print("error")    

#     return render(request,"accounts/login.html",context)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

User = get_user_model()

# def register_page(request):
#     form = RegisterForm(request.POST or None)
#     context = {
#         "form":form
#     }
#     if form.is_valid():
#         form.save()
#     return render(request,"accounts/register.html",context)
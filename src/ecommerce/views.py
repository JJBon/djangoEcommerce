from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login , get_user_model
from .forms import ContactForm 

def home_page(request):
    # if not request.user.is_authenticated():
    #     return Login

    context = {
        "title":"Hello World!",
        "content":"Welcome to home page"
    }
    if request.user.is_authenticated():
        context["premium_content"] = "YEAHHHHHHH"
    return render(request,"home_page.html",context)

def about_page(request):
    context = {
        "title":"About Page",
        "content":"Welcome to about page"
    } 
    return render(request,"home_page.html",context)


def contact_page(request):

    print(".......................................")

    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":"Welcome to contact page",
        "form":contact_form,
        "brand": "new Brand Name"
    }

    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message":"Thank you"})

    if contact_form.errors:
        print(contact_form.cleaned_data)
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))

    return render(request,"contact/view.html",context)



def home_page_old(request):
    html_ = """
    <!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css" integrity="sha384-9gVQ4dYFwwWSjIDZnLEWnxCjeSWFphJiwGPXr1jddIhOegiu1FwO5qRGvFXOdJZ4" crossorigin="anonymous">

        <title>Hello, world!</title>
    </head>
    <body>
        <div class = 'text-center'>
            <h1>Hello, world!</h1>
        </div>   

        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js" integrity="sha384-cs/chFZiN24E4KMATLdqdvsezGxaGsi4hLGOzlXwp5UZB1LY//20VyM2taTB4QvJ" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js" integrity="sha384-uefMccjFJAIv6A+rW+L4AHf99KvxDjWSu1z9VI8SKNVmz4sk7buKt/6v9KI65qnm" crossorigin="anonymous"></script>
    </body>
    </html>
    """
    return HttpResponse(html_)


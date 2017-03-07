from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SearchForm
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from .models import ParkingSpot
from django.urls import reverse
from django.contrib.auth.models import User

def account(request):
    return render(request, 'home/account.html', {'view': 'account'})


def sell(request):
    return render(request, 'home/sell.html', {'view': 'sell'})


def home(request):
    # url = reverse(signup, urlconf=None, args=None, kwargs=None)
    # atHome = True
    return render(request, 'home/home.html', {'view': 'home'})


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            login(request, user)
            # do stuff
            return HttpResponseRedirect(reverse(home))
    else:
        form = UserForm()

    url = reverse(home, urlconf=None, args=None, kwargs=None)
    return render(request, 'home/signup.html', {'form': form, 'url': url, 'link':'Home'})


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse(home))
        else:
            return HttpResponse("error")
    return render(request, 'home/signin.html', {})

    # url = reverse(home, urlconf=None, args=None, kwargs=None)
    # return render(request, 'home/signin.html', {'url':url, 'link':'Home'})

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse(home))

def search(request):
    spots = ParkingSpot.objects.all()
    city = request.GET['city']
    spots = spots.filter(city__icontains=city)
    if spots:
        response = "spots in " + city + ":<br>" + '<br>'.join([str(i) for i in spots]) + "<p><a href=\"/\">back</a></p>"
    else:
        response = "no spots found in city " + city + ", sorry!!<p><a href=\"/\">back</a></p>"
    return HttpResponse(response)

    # if request.method == "POST":
    #     form = QuestionChoiceForm(request.POST)
    #     if form.is_valid():
    #         question = form.save(commit=False)
    #         question.pub_date = timezone.now()
    #         question.save()
    #         question.choice_set.create(choice_text=form.cleaned_data['c1'], votes=0).save()
    #         question.choice_set.create(choice_text=form.cleaned_data['c2'], votes=0).save()
    #         if form.cleaned_data['c3'] != "":
    #             question.choice_set.create(choice_text=form.cleaned_data['c3'], votes=0).save()
    #         if form.cleaned_data['c4'] != "":
    #             question.choice_set.create(choice_text=form.cleaned_data['c4'], votes=0).save()
    #         return HttpResponseRedirect(reverse('polls:index'))
    # else:
    #     form = QuestionChoiceForm()
    # return render(request, 'polls/create.html', {'form':form})
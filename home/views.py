from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .forms import UserForm, SearchForm
from .models import ParkingSpot
from django.contrib.auth.models import User


# need to add: bootstrap styling
class UserDetail(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'username']
    template_name = 'home/account.html'
    success_url = '/account?success=true'

    def get_object(self):
        return self.request.user

    def __init__(self, *args, **kwargs):
        super(UserDetail, self).__init__(*args, **kwargs)
        for field in self.fields:
            print field


def home(request):
    return render(request, 'home/home.html', {})


@login_required
def sell(request):
    return render(request, 'home/sell.html', {})


# figure out how to make name inputs inline
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
    return render(request, 'home/signup.html', {'form': form})


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        next_page = request.POST['next']
        if next_page == "":
            next_page = reverse(home)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(next_page)
        else:
            return HttpResponse("error")
    return render(request, 'home/signin.html', {})


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
        response = "no spots found in city " + city + ", sorry :c<p><a href=\"/\">back</a></p>"
    return HttpResponse(response)


### POST form syntax
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
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
from .forms import SignUpForm, LoginForm
from django.http import HttpResponseRedirect
from .models import TeamMember
from Rest_API.models import DataStock, Index

# Create your views here.
def index(request):
    stockdata = Index.objects.order_by('-date')[0:1]
    # operation = Index.objects.raw("SELECT nepse FROM "Rest_API_index" ORDER BY "date" DESC LIMIT 1")
    # a = Index.objects.raw("SELECT nepse FROM Rest_API_index ORDER BY date DESC LIMIT 1")
    return render(request, 'index.html', {'dataset' : stockdata})


def aboutus(request):
    team = TeamMember.objects.all()
    return render(request, 'aboutus.html', {'team' : team})


def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = first_name
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            print('Successfully userform data taken.')
            print(request.POST)

            if password1==password2:
                if User.objects.filter(username=username):
                    print('Username Taken')
                    messages.info(request, 'Username Taken')
                    return redirect('signup')
                elif User.objects.filter(email=email):
                    print('Email Taken')
                    messages.info(request, 'Email Taken')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                    print('user created')
                    user.save()
                    return redirect('index')
        else:
                print('password not matching')
                messages.info(request, 'Password Not Matching')
                return redirect('signup')

    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form' : form})



def login(request):
    #Flush the session in the site
    if 'User' in request.session:
        print('Session Present')
        print(request.session['User'])
        logout(request)
        redirect('login')

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            #email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #user = authenticate(password=password, email=email)
            user = authenticate(password=password, username=username)

            print(request.POST)

            if user is not None:
                #If user is logged in session is set
                request.session['User'] = 'True'
                print("logged In User")
                auth.login(request, user)
                
                return redirect('index')
            else:
                messages.info(request, "Invalid Username or Password")
                print('Not Logged In')

            return redirect('login')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form })


def logout(request):
    #Delete the user session
    request.session.flush()
    auth.logout(request)
    return redirect('/')


def search(request):
    qstock = request.GET.get('query')
    # Stock_q = DataStock.objects.filter(Symbol=qstock).order_by('-Date')[0:1].get()
    Stock_q = DataStock.objects.filter(Symbol=qstock).order_by('-Date')[0:1]
    # Stock_q = DataStock.objects.filter(Symbol=qstock).order_by('Date').last()
    # Stock_q = DataStock.objects.order_by('Symbol')[0:1]
    print(Stock_q.query)
    print(Stock_q)
    print(qstock)
    
    Stock = {
        'Symbol' : qstock,
    }
    return render(request, 'search.html', { 'stocks' : Stock_q, 'stock_symbol' : qstock })

def chart(request, stock_symbol):
    return render(request, 'charter.html')
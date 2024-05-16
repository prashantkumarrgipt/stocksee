from django.shortcuts import render,HttpResponse , redirect
from .utils import get_stock_price
from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User
from .models import Watchlist, Stock
# Create your views here.


def dashboard(request):
    # symbol = 'AAPL'  # Example stock symbol 
    # latest_price = get_stock_price(symbol)
    # # latest_price = 'temp'
    # return render(request, 'index.html', {'latest_price': latest_price})

    if request.user.is_authenticated:
        watchlist = Watchlist.objects.filter(user=request.user).first()
        if watchlist:
            stock_prices = {}
            for stock in watchlist.stocks.all():
                price = get_stock_price(stock.symbol)
                stock_prices[stock.symbol] = price
        else:
            stock_prices = None
        return render(request, 'index.html', {'stock_prices': stock_prices})
    else:
        return render(request, 'index.html')


def create_watchlist(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        if symbol:
            # Create or get the stock object
            stock, created = Stock.objects.get_or_create(symbol=symbol)
            # Get or create the user's watchlist
            watchlist, created = Watchlist.objects.get_or_create(user=request.user)
            watchlist.stocks.add(stock)
            watchlist.save()
    return redirect('home')

# signup
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<5:
            messages.error(request, " Your user name must be under 5 characters")
            return redirect('home')

        # username must be only letters and numbers 
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')

        # password should match 
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('home')
        
        # Create the user
        # Create the user
        try:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your account has been successfully created")
            return redirect('home')  # Assuming you have a login view
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('home')

    else:
        return render(request, 'home')

    # else:
    #     return HttpResponse("404 - Not found")
 
        

# login
def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect(request.META.get('HTTP_REFERER', 'index'))
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

# logout
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect(request.META.get('HTTP_REFERER', 'home'))

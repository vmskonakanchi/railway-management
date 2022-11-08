from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.views.generic import View
from app.forms import *
from .models import Train, Booking

_HOME_PAGE = 'index.html'
_LOGIN_PAGE = 'login.html'
_REGISTER_PAGE = 'register.html'
_USER_HOME_PAGE = 'user/home.html'
_ADMIN_HOME_PAGE = 'admin/home.html'
_USER_BOOKINGS_PAGE = 'user/bookings.html'
_ADD_BOOKING_PAGE = 'admin/add_booking.html'
_ADMIN_USERS = 'admin/users.html'
_ADMIN_REQUESTS = 'admin/requests.html'
_ADMIN_TRAINS = "admin/trains.html"
_ADMIN_EDIT_TRAIN = "admin/edit_train.html"


# Function based views
def index(req):
    return render(req, _HOME_PAGE)


def logout_user(req):
    if req.user is not None:
        logout(req)
    return redirect('/')


def user_bookings(req):
    return render(req, _USER_BOOKINGS_PAGE , {"bookings" : Booking.objects.filter(user=req.user)})

def users(req):
    return render(req,_ADMIN_USERS , {"users" : User.objects.all()})


def trains(req):
    return render(req, _ADMIN_TRAINS , {"trains" : Train.objects.all()})


def delete(req,id):
    train = Train.objects.filter(id=id)
    if train is not None:
        train = train[0]
        train.delete()
    return redirect('/admin/trains')

def book(req,id):
    train = Train.objects.filter(id=id)
    if train is not None:
        train = train[0]
        if train.available_seats > 0:
            booking = Booking(user=req.user, train=train)
            booking.save()
            return redirect('/user/bookings')
        else:
            return redirect('/user')

def accept(req, id):
    request = Booking.objects.filter(id=id)
    if request is not None:
        request = request[0]
        request.status = 2
        request.save()
    return redirect('/admin/requests')


def reject(req, id):
    request = Booking.objects.filter(id=id)
    if request is not None:
        request = request[0]
        request.status = 1
        request.save()
    return redirect('/admin/requests')

# Class based views
class EditTrainView(View):
    def get(self,req,id):
        train = Train.objects.filter(id=id)
        if train is not None:
            train = train[0]
            form = EditBookingForm(instance=train)
            return render(req, _ADMIN_EDIT_TRAIN, {'form': form , 'train' : train})
        else:
            return redirect('/admin/trains')

    def post(self,req,id):
        train = Train.objects.filter(id=id)
        if train is not None:
            train = train[0]
            form = EditBookingForm(req.POST, instance=train)
            if form.is_valid():
                form.save()
                return redirect('/admin/trains')
            else:
                return render(req, _ADMIN_EDIT_TRAIN, {'form': form})
        else:
            return redirect('/admin/trains')
class LoginView(View):

    def get(self, req):
        return render(req, _LOGIN_PAGE, {'form': LoginForm()})

    def post(self, req):
        form = LoginForm(req.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if not User.objects.filter(email=email).exists():
                form.add_error('email', 'User does not exist')
                return render(req, _LOGIN_PAGE, {'form': form})
            if email == 'admin@gmail.com':
                user = authenticate(req, username='admin', password=password)
                if user is not None:
                    login(req, user)
                    return redirect('/admin')
                else:
                    form.add_error('password', 'Invalid password')
                    return render(req, _LOGIN_PAGE, {'form': form})
            user = authenticate(req, username=email, password=password)
            if user is not None:
                login(req, user)
                if user.is_superuser:
                    return redirect('/admin/')
                else:
                    return redirect('/user/')
            else:
                form.add_error('password', 'Invalid Password')
                return render(req, _LOGIN_PAGE, {'form': form})
        else:
            
            return render(req, _LOGIN_PAGE, {'form': form})


class RegisterView(View):

    def get(self, req):
        return render(req, _REGISTER_PAGE, {'form': RegisterForm()})

    def post(self, req):
        form = RegisterForm(req.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            first_name = form.cleaned_data['first_name']
            if len(User.objects.filter(email=email)) > 0:
                form.add_error('email', 'Email already exists')
                return render(req, _REGISTER_PAGE, {'form': form, 'errors':form.errors.values()})
            if len(password) < 8:
                form.add_error('password', 'Password must be at least 8 characters')
                return render(req, _REGISTER_PAGE, {'form': form, 'errors':form.errors.values()})
            if password == confirm_password:
                user = User.objects.create_user(email, email, password)
                user.first_name = first_name
                user.save()
                return render(req, _REGISTER_PAGE, {'form': LoginForm() , 'message' : 'User Registered successfully'})
            else:
                form.add_error('confirm_password', 'Password and confirm password should be same')
                return render(req, _REGISTER_PAGE, {'form': form, 'errors':form.errors})
        else:
            form.add_error('email' , 'Invalid email')
            return render(req, _REGISTER_PAGE, {'form': form, 'errors':form.errors})


class AdminView(View):
    def get(self, req):
        return render(req, _ADMIN_HOME_PAGE)

    def post(self, req):
        pass


class AdminAddBooking(View):
    def get(self, req):
        return render(req, _ADD_BOOKING_PAGE , {'form': AddBookingForm()})

    def post(self, req):
        form = AddBookingForm(req.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.available_seats = form.cleaned_data['total_seats']
            form.save()
            return render(req,_ADD_BOOKING_PAGE, {"success" : "Train added successfully" , 'form' : AddBookingForm()})
        else:
            return render(req, _ADD_BOOKING_PAGE, {'form': AddBookingForm(), 'errors':form.errors})


class UserView(View):

    def get(self, req):
        return render(req, _USER_HOME_PAGE , {"trains" : Train.objects.all()})

    def post(self, req):
        pass


class AdminUserRequests(View):

    def get(self,req):
        return render(req,_ADMIN_REQUESTS,{"requests" : Booking.objects.filter(status=0)})

    def post(self,req):
        pass
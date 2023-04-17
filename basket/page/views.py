from django.contrib import messages

from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from .models import Coach
from .forms import UserForm, CoachForm
def signup(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email=form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'A user with this email already exists.')
                return redirect('signup')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken.')
                return redirect('signup')

            user = User(
                username=username,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_number=form.cleaned_data['phone_number'],
                email=email,
                gender=form.cleaned_data['gender'],
                skill_level=form.cleaned_data['skill_level'],
                password=form.cleaned_data['password']
            )
            user.save()
            messages.success(request, 'Your account has been created. Please log in.')
            return redirect('home')

    return render(request, 'signup.html', {'form': form})


def home(request):
    return render(request, 'home.html')
def coach_signup(request):
    if request.method == 'POST':
        form = CoachForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if a coach with the given email already exists
            email = form.cleaned_data['email']
            if Coach.objects.filter(email=email).exists():
                messages.error(request, 'A coach with this email already exists.')
                return redirect('signup_coach')
            # Check if a coach with the given username already exists
            username = form.cleaned_data['username']
            if Coach.objects.filter(username=username).exists():
                messages.error(request, 'A coach with this username already exists.')
                return redirect('signup_coach')
            # Create a new Coach object with the form data
            coach = Coach(
                username=username,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                phone_number=form.cleaned_data['phone_number'],
                email=email,
                gender=form.cleaned_data['gender'],
                password=form.cleaned_data['password'],
                experience=form.cleaned_data['experience'],
                resume=request.FILES['resume']
            )
            # Save the Coach object to the database
            coach.save()
            # Redirect to a success page or log in the coach
            return redirect('home')
    else:
        form = CoachForm()
    return render(request, 'coach_signup.html', {'form': form})

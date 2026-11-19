from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpRequest, HttpResponse

from .models import Profile
from .forms import RegistrationForm


def register(request: HttpRequest) -> HttpResponse:
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        with transaction.atomic():
            user = form.save()
            Profile.objects.create(user=user, role=form.cleaned_data['role'])

        return redirect('accounts:login')

    return render(request, 'accounts/registration.html', {'form': form})


def login():
    ...


def logout():
    ...

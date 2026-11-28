
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ReceiptUserCreationForm


# =========================
# Registration
# =========================

def register_page(request):

    if request.method == "POST":

        form = ReceiptUserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Registration successful. Please login."
            )

            return redirect("login")

    else:

        form = ReceiptUserCreationForm()

    return render(
        request,
        "register.html",
        {"form": form}
    )


# =========================
# Login
# =========================

def login_page(request):

    if request.method == "POST":

        email = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        else:

            messages.error(
                request,
                "Invalid email or password."
            )

    return render(request, "login.html")


# =========================
# Logout
# =========================

def logout_page(request):

    logout(request)

    return redirect("login")

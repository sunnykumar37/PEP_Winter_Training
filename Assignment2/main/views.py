from django.shortcuts import render, redirect
from .forms import RegistrationForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings


# ---------- Registration ----------
def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            send_mail(
                subject="Welcome to Our Platform",
                message=f"Hello {user.name}, your registration is successful.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email],
                fail_silently=False,
            )

            return render(request, "success.html")

    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form": form})


# ---------- Contact ----------
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            send_mail(
                subject=f"New Contact Query from {contact.name}",
                message=f"""
Name: {contact.name}
Email: {contact.email}

Message:
{contact.message}
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )

            return render(request, "contact_success.html")

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
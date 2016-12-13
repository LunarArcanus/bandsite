from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from models import BandInfo
from forms import SignupForm
from merch import sale_items

def form_handler(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            band = form.save(commit=False)
            fields = {
                "name": form.cleaned_data["name"],
                "est_date": form.cleaned_data["est_date"],
                "pub_date": timezone.now(),
                "members": form.cleaned_data["members"]
            }

            band.name = fields["name"]
            band.est_date = fields["est_date"]
            band.pub_date = fields["pub_date"]
            band.members = fields["members"]

            band.save()
            request.session["band_sub_name"] = fields["name"]
            return redirect("submitted")
        else:
            return redirect("index")
    else:
        form = SignupForm()
    return render(request, 'form.html', {"form": form})

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "aboutus.html")

def bands(request):
    band_list = BandInfo.objects.all()
    return render(request, "bands.html", {'band_list': band_list})

def submitted(request):
    return render(request, "submitted.html", {
                "band_name": request.session["band_sub_name"]
                })

def merch(request):
    return render(request, "buy.html", {"item_list": sale_items})

def cart(request):
    return render(request, "cart.html")

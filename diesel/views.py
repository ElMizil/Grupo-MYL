from django.shortcuts import render, redirect
from .forms import DieselLogForm
from .models import DieselLog

def diesel_create(request):
    if request.method == "POST":
        form = DieselLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("diesel_list")
    else:
        form = DieselLogForm()

    return render(request, "diesel/diesel_form.html", {"form": form})


def diesel_list(request):
    logs = DieselLog.objects.order_by("-fecha")[:200]  # últimos 200
    return render(request, "diesel/diesel_list.html", {"logs": logs})

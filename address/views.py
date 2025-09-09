import os

from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET

from .forms import AddressForm


@require_GET
def pick_address(request):
    form = AddressForm()
    email = os.environ.get("EMAIL_USER") or getattr(settings, "EMAIL_HOST_USER", "")
    return render(request, "pick_address.html", {"form": form, "email": email})


@require_POST
def save_address(request):
    form = AddressForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse('<p class="success-msg">Address saved!</p>')
    return HttpResponse(
        '<div id="form-container"><form id="address-form" method="post" '
        'hx-post="{url}" hx-target="#form-container" hx-swap="outerHTML">'
        '{csrf}{fields}<button type="submit" class="btn-save">Save</button>'
        "</form></div>".format(
            url=request.build_absolute_uri(),  # same save endpoint
            csrf=f'<input type="hidden" name="csrfmiddlewaretoken" value="{request.COOKIES.get("csrftoken","")}">',
            fields=form.as_p(),
        )
    )

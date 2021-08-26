from django.urls import reverse
from Contact_me.forms import messageform
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
def contact(request):
    form = messageform(request.POST)
    if form.is_valid():
        form.save()
        form =messageform()
    return HttpResponseRedirect(reverse ('index'))
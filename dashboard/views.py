from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from aid.models import Request

@login_required
def index(request):
    items = Request.objects.filter(author=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })

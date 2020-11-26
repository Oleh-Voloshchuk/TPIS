from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    local_dt = datetime.now()
    response = {'date': local_dt, 'current_page': request.build_absolute_uri(), 'server_info': os.name, 'client_info': os.uname()[1]}
    return JsonResponse(response)
# Create your views here.


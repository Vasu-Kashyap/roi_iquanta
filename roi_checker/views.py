from django.shortcuts import render
from http.client import HTTPResponse
from urllib import response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from .models import college
from .filters import CollegeFilter

from .models import *


def index(request):
    colleges = CollegeFilter(request.GET)
    return render(request, 'index.html', {'colleges': colleges})


@csrf_protect
def nindex(response):
    if response.method == "POST":
        print(response.POST)
        name = response.POST.get("Name")
        fs = response.POST.get("fees")
        pkg = response.POST.get("package")
        allclg = college.objects.all()
        clg = []
        for c in allclg:
            # print(c.fees, fs)
            # print(c.average, pkg)
            lakh = 100000
            if c.fees <= int(fs) / lakh and c.average >= int(pkg) / lakh:
                clg.append(c)

        return render(response, "nidx.html", {'clg': clg})
    return render(response, "nidx.html")

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import college


def is_number(s):
    """ Returns True is string is a number. """
    try:
        float(s)
        return True
    except ValueError:
        return False


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'fees', 'average', 'median')

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv)]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            if not csv_file.name.endswith('.csv'):
                messages.warning(request,'wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")
            print(len(csv_data))
            for x in csv_data:
                fields = x.split(",")
                if len(fields) == 1:
                    break
                print(fields[0], float(fields[1]), float(fields[2]), fields[3])

                created = college.objects.update_or_create(
                    name=fields[0],
                    fees=float(fields[1]),
                    average=float(fields[2]),
                    median=float(fields[3]) if is_number(fields[3]) else None
                )

            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}

        return render(request, "admin/csv_upload.html", data)


admin.site.register(college, PeopleAdmin)

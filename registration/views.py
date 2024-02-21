from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def upload_file(request):
    if request.method == "POST":
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            file is saved
            form.save()
            return HttpResponse("Thanks for uploading your consent form! We will be in touch soon")
    else:
        form = ModelFormWithFileField()
    return render(request, "index.html", {"form": form})


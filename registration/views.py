from django.shortcuts import render
from django.http import HttpResponse 
from .form import UploadFileForm
from .models import ModelWithFileField


# from Django website
    

def upload_file(request):
    template_name = "registration//index.html"
    if request.method == "POST":
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
             file is saved
             form.save()
             return HttpResponse("Thank you for uploading your form. We will be in contact soon!")
    else:
        form = ModelFormWithFileField()
    return render(request, "upload.html", {"form": form})
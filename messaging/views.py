from django.shortcuts import render, get_object_or_404
from .models import Message

# https://ordinarycoders.com/blog/article/django-messages-framework
# Create your views here.
def Contactform(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      subject = "Contact us" 
      body = {
      'sender': form.cleaned_data['sender'], 
      'receiver': form.cleaned_data['receiver'], 
      'subject': form.cleaned_data['subject'], 
      'body':form.cleaned_data['body'], 
      'email':form.cleaned_data['email'],
      }
      message = "\n".join(body.values())

      try:
        send_mail(subject, message, 'lydsjoyy@gmail.com', ['lydsjoyy@gmail.com']) 
      except BadHeaderError:
        return HttpResponse('Invalid header found.')
      messages.success(request, "Message sent." )
      return redirect ("main:home")
      messages.error(request, "Error. Message not sent.")

      return render(
        request,
        "messaging/messages.html",
        {"message": amessage},
    )
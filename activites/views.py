from django.shortcuts import render

# Create your views here.
def activites(request):
    """
    Renders the activty page
    """
    activites = activites.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "activites.html",
        {"activites": activites},
    )
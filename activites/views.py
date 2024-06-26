from django.shortcuts import render

# Create your views here.
def activites(request):
    """
    Renders the activty page
    """
    activites = activites.objects.all()

    return render(
        request,
        "activites.html",
        {"activites": activites},
    )
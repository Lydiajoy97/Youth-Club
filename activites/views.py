from django.shortcuts import render

# Create your views here.
def activities(request):
    """
    Renders the About page
    """
    activities = activities.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "activities.html",
        {"activities": activities},
    )
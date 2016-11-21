from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):

    return render(request, "disappearingninjas/index.html")
def showall(request):

    return render(request, "disappearingninjas/showall.html")

def show(request, color):

    if color in ('blue', 'red', 'orange', 'purple'):
        context={
        'color': color,
        }
    else:
        context={
        'color': 'all',
        }

    print ("*"*100)
    print color
    print context
    print ("*"*100)


    return render(request, "disappearingninjas/show.html", context)

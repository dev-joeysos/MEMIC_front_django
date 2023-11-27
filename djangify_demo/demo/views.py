from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'demo/index.html')

def four_one(request):
    return render(request, 'demo/401.html')

def four_four(request):
    return render(request, 'demo/404.html')

def faqs(request):
    return render(request, 'demo/faqs.html')

def feedback(request):
    return render(request, 'demo/feedback.html')

def input(request):
    return render(request, 'demo/input.html')

def record(request):
    return render(request, 'demo/record.html')

def style_guide(request):
    return render(request, 'demo/sytle-guide.html')
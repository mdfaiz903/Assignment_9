from django.shortcuts import render

# Create your views here.
def home(request):
    context={
        'data':'Helllo world',
    }
    return render(request,'homeview/index.html',context)

def contact(request):
    return render(request,'contact/contact.html')
   
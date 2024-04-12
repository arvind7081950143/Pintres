from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm,SignupForm,ContactForm
from item.models import Item,Category
from django.db.models import Q
from . models import Contact
def index(request):
    item_image=Item.objects.all()
    return render(request,'core/index.html',{'image':item_image})
def details(request,pk):
    items=get_object_or_404(Item,pk=pk)
    return render(request,'core/details.html',{'item':items})
def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('core:index')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'core/login.html', {'error_message': error_message})
    else:
        return render(request, 'core/login.html')


def singnup(request):
    # if request.method == 'POST':
    #     form = SignupForm(request.POST)

    #     if form.is_valid():
    #         form.save()

    #         return redirect('/login/')
    # else:
    #     form = SignupForm()

    # form=SignupForm()
    if request.method == 'POST':
        username = request.POST['Username']
        email = request.POST['email']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('core:login')
            except:
                error_message = 'Error creating account'
                return render(request, 'core/singnup.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'core/singnup.html', {'error_message': error_message})
    return render(request, 'core/singnup.html')

def logout(request):
    auth.logout(request)
    return redirect('core:index')
def brows(request):
    query = request.GET.get('search-data', '')
    category_id = request.GET.get('category', 0)
    category=Category.objects.all()
    item=Item.objects.all()
    if category_id:
        item = item.filter(category_id=category_id)

    if query:
        item = item.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request,"core/brows.html",{'category':category,'item':item,'query':query})

def contact(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST)
        form.save()
        return redirect('core:contact')
    return render(request,'core/contact.html',{'form':form})

def contact_inbox(request):
    if request.user.is_superuser:
        contact=Contact.objects.all()
        print(contact)
        return render(request,'core/inbox.html',{'contact':contact})
    else:
        return HttpResponse('<h1>''I am sorry....''</h1>')
    
def about(request):
    return render(request,'core/about.html')
# Create your views here.

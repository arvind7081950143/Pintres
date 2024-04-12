from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from item.models import Item,Category
from .forms import NewItemForm,editprofileForm,EditItemForm
from .models import Profile,Profile_user
from django.contrib.auth.models import User
import os


@login_required
def dashboard(request):
    items=Item.objects.filter(created_by=request.user)
    return render(request,'dashboard/dashboard.html',{'item':items})
@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('core:details',pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'dashboard/upload.html', {
        'form': form,
    })
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('core:details', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'dashboard/editupload.html', {
        'form': form,
        'title': 'Edit item',
    })

def profile_user(request):
    profile=Profile_user.objects.filter(created_by=request.user)
    if len(profile)==0:
        return redirect('dashboard:profile')
    return render(request,"dashboard/profile_user.html",{'profile':profile})
@login_required
def profile(request):
    if request.method == 'POST':
        form = editprofileForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('dashboard:profile_user')
    else:
        form = editprofileForm()

    form=editprofileForm()
    return render(request,'dashboard/profile.html',{'form':form})
def edit_profile(request):
    profile_data=Profile_user.objects.filter(created_by=request.user)
    data=''
    for i in profile_data:
        data=i
    if request.method == 'POST':
        form = editprofileForm(request.POST, request.FILES, instance=data)

        if form.is_valid():
            form.save()

            return redirect('dashboard:profile_user')
    else:
        form = editprofileForm(instance=data)

    return render(request,'dashboard/edit_profile.html',{'profile':data,'form':form})

# Create your views here.

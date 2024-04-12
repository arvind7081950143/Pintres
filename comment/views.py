from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation
from django.contrib import auth
from django.contrib.auth.models import User
def comment(request,pk):
  if request.user.is_authenticated:

    item = get_object_or_404(Item, pk=pk)

    if item.created_by == request.user:
        return redirect('dashboard:dashboard')
    
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        # return redirect('conversation:detail', pk=conversations.first().id)
        pass

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('core:details',pk)
    else:
        form = ConversationMessageForm()
    
    return render(request,'comment/comment.html',{'item':item,'form':form})
  else:
      return redirect('core:login')

def inbox(request):
    comment = Conversation.objects.filter(members__in=[request.user.id])
    return render(request,'comment/inbox.html',{'comment':comment})
def details(request,pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('comment:details', pk)
    else:
        form = ConversationMessageForm()


    return render(request,'comment/details.html',{'conversation':conversation,'form':form})
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from dashboard.views import index
from user.models import UserProfile

from aid.models import Request

from .forms import ConversationMessageForm
from .models import Conversation

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Request, pk=item_pk)

    if item.author == request.user:
        items = Request.objects.filter(author=request.user)

        return render(request, 'dashboard/index.html', {
            'Requests': items,
        })
    conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.author)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('aid:request_detail', pk=item_pk)
    else:
        form = ConversationMessageForm()
    
    return render(request, 'conversation/new.html', {
        'form': form
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    for convo in conversations:
    # Get all members in this conversation
        members = list(convo.members.all())
        # Remove the logged-in user to get the other member
        receiver = [m for m in members if m != request.user]
        if receiver:
            receiver_user = receiver[0]  # The other member
            profile = UserProfile.objects.filter(user=receiver_user).first()
        else:
            receiver_user = None
            profile = None
    requests = Request.objects.filter(author=request.user)
    picture=UserProfile.objects.filter(user=request.user).first()
    print("conversations", conversations)

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations,
        'requests': requests,
        "profilee": profile,
        "profile": picture,
    })

@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()

            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()
        members = list(conversation.members.all())
        print(members)
            # Remove the logged-in user to get the other member
        receiver = [m for m in members if m != request.user]
        print(receiver)
        if receiver:
            receiver_user = receiver[0]  # The other member
            receiverr= UserProfile.objects.filter(user=receiver_user).first()
        else:
            receiver_user = None
            receiverr = None
    sender=UserProfile.objects.filter(user=request.user).first()
    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form,
        'sender':sender,
        "receiver":receiverr,
    })
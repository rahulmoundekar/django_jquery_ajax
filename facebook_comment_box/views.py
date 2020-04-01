from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
import json

# Create your views here.
from facebook_comment_box.MessageForm import MessageForm
from facebook_comment_box.models import Message


def indexView(request):
    form = MessageForm()
    return render(request, "index.html", {"form": form})


def viewPostComments(request):
    if request.is_ajax:
        messages = Message.objects.all().order_by('-id')
        json_messages = serializers.serialize("json", messages)
    return JsonResponse({"messages": json_messages}, status=200)


def sendComments(request):
    # request should be ajax and method should be POST.
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = MessageForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            message = form.save()
            print(message)
            # serialize in new messages object in json
            json_messages = serializers.serialize("json", [message, ])
            # send to client side.
            return JsonResponse({"messages": json_messages}, status=200)
        else:
            # some form errors occured.
            return JsonResponse({"error": form.errors}, status=400)
    # some error occurred
    return JsonResponse({"error": ""}, status=400)

from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse, HttpResponseRedirect
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import contractions
import re
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .wordcloud import show
import os


def simple_upload(request):
    if request.method == 'POST' and request.FILES:
        user_ip = request.META.get("REMOTE_ADDR")
        if not os.path.exists('./whatsapp/uploaded_files/' + user_ip):
            os.makedirs('./whatsapp/uploaded_files/' + user_ip)
        path_to_upload = './whatsapp/uploaded_files/' + user_ip + "/"

        files = request.FILES
        for file in files.getlist('uploadedFile'):
            if os.path.exists(path_to_upload + "chat.txt"):
                os.remove(path_to_upload + "chat.txt")
            with open(path_to_upload + "chat.txt", 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
        file_check = "Messages to this chat and calls are now secured with end-to-end encryption. Tap for more info."
        file_check_group = "created group"
        message = 'error'
        with open(path_to_upload + "chat.txt", 'r', encoding="utf8") as f:
            a = show(f)
            print(a['secure_url'][54:])
        return render(request, 'simple_upload_result.html', {
            'uploaded_file_url': a['secure_url'][54:]
        })
    return render(request, 'simple_upload.html')


def test(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'test.html')
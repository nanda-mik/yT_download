from django.shortcuts import render, redirect
from django.contrib import messages

from pytube import YouTube

# Create your views here.
def home(request):
    return render(request, 'index.html')

def download(request):
    if request.method == 'POST':
        url = request.POST['url']
        if url:
            my_video = YouTube(url)
            try:
                print("download started")
                my_video = my_video.streams.get_lowest_resolution()
                my_video.download()
            except AttributeError as exc:
                print(exc)
                messages.error("error in downloading")
            messages.success(request, 'Video Downloaded.')
            return redirect('home')
        else:
            messages.warning(request, 'Please Enter Video URL')
            return redirect('home')

    return redirect('home')
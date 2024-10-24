from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album
# Create your views here.


def album_image_view(request):

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('album_images')
    else:
        form = AlbumForm()
    return render(request, 'album_image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')

# for displaying images

def display_album_images(request):
    if request.method == 'GET':
        # getting all the data of gallary photo
        album = Album.objects.all()
        return render(request, 'display_album_images.html', {'album': album})


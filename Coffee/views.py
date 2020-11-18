from django.shortcuts import render, get_object_or_404, redirect

from .models import Artwork, WrittenPiece
from .forms import CaptchaForm

def index(request):
    return render(request, 'Coffee/index.html')


def artwork_home(request):
    artwork_list = Artwork.objects.order_by('title')
    return render(request, 'Coffee/artwork_home.html', {'artwork_list': artwork_list})


def artwork(request, artwork_id):
    context = {'artwork': get_object_or_404(Artwork, pk=artwork_id), 'form': CaptchaForm()}
    return render(request, 'Coffee/artwork.html', context)


def artwork_like(request, artwork_id):
    if request.POST:
        form = CaptchaForm(request.POST)

        if form.is_valid():
            get_object_or_404(Artwork, pk=artwork_id).like()
            return redirect('Coffee:artwork', artwork_id=artwork_id)
    return redirect('Coffee:artwork', artwork_id=artwork_id)


def written(request, written_id):
    context = {'written': get_object_or_404(WrittenPiece, pk=written_id), 'form': CaptchaForm()}
    return render(request, 'Coffee/written_piece.html', context)


def written_home(request):
    written_list = WrittenPiece.objects.order_by('title')
    return render(request, 'Coffee/written_piece_home.html', {'written_list': written_list})


def written_like(request, written_id):
    if request.POST:
        form = CaptchaForm(request.POST)

        if form.is_valid():
            get_object_or_404(WrittenPiece, pk=written_id).like()
            return redirect('Coffee:writtenPiece', written_id=written_id)
    return redirect('Coffee:writtenPiece', written_id=written_id)
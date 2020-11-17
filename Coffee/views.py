from django.shortcuts import render, get_object_or_404, redirect

from .models import Artwork, WrittenPiece


def index(request):
    return render(request, 'Coffee/index.html')


def artwork_home(request):
    artwork_list = Artwork.objects.order_by('title')
    return render(request, 'Coffee/artwork_home.html', {'artwork_list': artwork_list})


def artwork(request, artwork_id):
    return render(request, 'Coffee/artwork.html', {'artwork': get_object_or_404(Artwork, pk=artwork_id)})


def artwork_like(request, artwork_id):
    get_object_or_404(Artwork, pk=artwork_id).like()
    return redirect('Coffee:artwork', artwork_id=artwork_id)


def written(request, written_id):
    return render(request, 'Coffee/written_piece.html', {'written': get_object_or_404(WrittenPiece, pk=written_id)})


def written_home(request):
    written_list = Artwork.objects.order_by('title')
    return render(request, 'Coffee/written_piece_home.html', {'written_list': written_list})


def written_like(request, written_id):
    get_object_or_404(WrittenPiece, pk=written_id).like()
    return redirect('Coffee:writtenPiece', written_id=written_id)

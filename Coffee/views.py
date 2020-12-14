from django.shortcuts import render, get_object_or_404, redirect
from profanityfilter import ProfanityFilter

from .forms import CaptchaForm, CommentForm
from .models import Artwork, ArtworkComment, WrittenPiece, WrittenPieceComment

pf = ProfanityFilter(extra_censor_list=open('Coffee/profanity_list.txt', 'r').read().split('\n'))


def index(request):
    return render(request, 'Coffee/index.html')


def artwork_home(request):
    artwork_list = Artwork.objects.order_by('title')
    return render(request, 'Coffee/artwork_home.html', {'artwork_list': artwork_list})


def artwork(request, artwork_id):
    art = get_object_or_404(Artwork, pk=artwork_id)
    context = {'artwork': art, 'likeForm': CaptchaForm(),
               'commentForm': CommentForm, 'comments_ordered': art.comments.all().order_by('-timestamp')}
    return render(request, 'Coffee/artwork.html', context)


def artwork_like(request, artwork_id):
    if request.POST:
        form = CaptchaForm(request.POST)

        if form.is_valid():
            get_object_or_404(Artwork, pk=artwork_id).like()

    return redirect('Coffee:artwork', artwork_id=artwork_id)


def artwork_comment(request, artwork_id):
    if request.POST:
        form = CommentForm(request.POST)

        if form.is_valid():
            if not (pf.is_profane(form.cleaned_data['author']) or pf.is_profane(form.cleaned_data['comment'])):
                ArtworkComment(artwork=get_object_or_404(Artwork, pk=artwork_id), author=form.cleaned_data['author'],
                               body=form.cleaned_data['comment']).save()

    return redirect('Coffee:artwork', artwork_id=artwork_id)


def written(request, written_id):
    written = get_object_or_404(WrittenPiece, pk=written_id)
    context = {'written': written, 'likeForm': CaptchaForm, 'commentForm': CommentForm,
               'comments_ordered': written.comments.all().order_by('-timestamp')}
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


def written_comment(request, written_id):
    if request.POST:
        form = CommentForm(request.POST)

        if form.is_valid():
            if not (pf.is_profane(form.cleaned_data['author']) or pf.is_profane(form.cleaned_data['comment'])):
                WrittenPieceComment(written_piece=get_object_or_404(WrittenPiece, pk=written_id),
                                    author=form.cleaned_data['author'],
                                    body=form.cleaned_data['comment']).save()

    return redirect('Coffee:writtenPiece', written_id=written_id)

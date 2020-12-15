from django.shortcuts import render, get_object_or_404, redirect
from profanityfilter import ProfanityFilter

from .forms import CaptchaForm, CommentForm
from .models import Recipe, RecipeComment, WrittenPiece, WrittenPieceComment

pf = ProfanityFilter(extra_censor_list=open('Coffee/profanity_list.txt', 'r').read().split('\n'))


def index(request):
    return render(request, 'Coffee/index.html')


def recipe_home(request):
    recipe_list = Recipe.objects.order_by('title')
    return render(request, 'Coffee/recipe_home.html', {'recipe_list': recipe_list})


def recipe(request, recipe_id):
    obj = get_object_or_404(Recipe, pk=recipe_id)
    context = {'recipe': obj, 'likeForm': CaptchaForm(),
               'commentForm': CommentForm, 'comments_ordered': obj.comments.all().order_by('-timestamp')}
    return render(request, 'Coffee/recipe.html', context)


def recipe_like(request, recipe_id):
    if request.POST:
        form = CaptchaForm(request.POST)

        if form.is_valid():
            get_object_or_404(Recipe, pk=recipe_id).like()

    return redirect('Coffee:recipe', recipe_id=recipe_id)


def recipe_comment(request, recipe_id):
    if request.POST:
        form = CommentForm(request.POST)

        if form.is_valid():
            if not (pf.is_profane(form.cleaned_data['author']) or pf.is_profane(form.cleaned_data['comment'])):
                RecipeComment(recipe=get_object_or_404(Recipe, pk=recipe_id), author=form.cleaned_data['author'],
                              body=form.cleaned_data['comment']).save()

    return redirect('Coffee:recipe', recipe_id=recipe_id)


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

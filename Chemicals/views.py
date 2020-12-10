from django.shortcuts import render, get_object_or_404, redirect

from .forms import CaptchaForm
from .models import Topic, Group


def index(request):
    topic_list = Topic.objects.order_by('title')
    context = {'topic_list': topic_list}
    return render(request, 'Chemicals/index.html', context)


def detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    context = {'topic': topic, 'form': CaptchaForm()}
    return render(request, 'Chemicals/detail.html', context)


def like(request, topic_id, group_id):
    if request.POST:
        form = CaptchaForm(request.POST)

        if form.is_valid():
            get_object_or_404(Group, pk=group_id).like()

    return redirect('Chemicals:detail', topic_id=topic_id)

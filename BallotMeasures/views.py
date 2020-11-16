from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Group


def index(request):
    topic_list = Topic.objects.order_by('title')
    context = {'topic_list': topic_list}
    return render(request, 'index.html', context)


def detail(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    context = {'topic': topic}
    return render(request, 'detail.html', context)


def like(request, topic_id, group_id):
    group = get_object_or_404(Group, pk=group_id)
    group.like()

    return redirect('BallotMeasures:detail', topic_id=topic_id)

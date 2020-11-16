from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=600)

    def __str__(self):
        return self.title


class Group(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    poster = models.URLField(max_length=200)
    research = models.URLField(max_length=200)
    class_name = models.CharField(max_length=50, default="na")
    likes = models.IntegerField(default=0)

    def like(self):
        self.likes += 1
        self.save()

    def reset_likes(self):
        self.likes = 0
        self.save()

    def __str__(self):
        return self.class_name + ' ' + self.topic.title


class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_initial = models.CharField(max_length=4)

    def __str__(self):
        return self.first_name + ' ' + self.last_initial

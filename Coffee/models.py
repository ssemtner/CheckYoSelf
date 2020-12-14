from django.db import models


class Artwork(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    statement = models.CharField(max_length=2000)
    image = models.URLField(max_length=200)
    thumbnail = models.URLField(max_length=200)

    def like(self):
        self.likes += 1
        self.save()

    def __str__(self):
        return self.title


class ArtworkComment(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='comments')
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    body = models.CharField(max_length=200)

    def __str__(self):
        return 'Artwork Comment {} by {}'.format(self.body, self.author)


class WrittenPiece(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    likes = models.IntegerField(default=0)
    thumbnail = models.URLField(max_length=200)

    def like(self):
        self.likes += 1
        self.save()

    def __str__(self):
        return self.title


class WrittenPieceComment(models.Model):
    written_piece = models.ForeignKey(WrittenPiece, on_delete=models.CASCADE, related_name='comments')
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    body = models.CharField(max_length=200)

    def __str__(self):
        return 'Written Piece Comment {} by {}'.format(self.body, self.author)

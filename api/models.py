from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Movie(models.Model):
    imdbID = models.CharField(max_length=10, primary_key=True)
    Title = models.CharField(max_length=32)
    Plot = models.TextField(max_length=256)
    Year = models.IntegerField()
    Runtime = models.CharField(max_length=8)
    Genre = models.TextField(max_length=128)
    Director = models.CharField(max_length=32)
    Actors = models.TextField(max_length=128)
    Poster = models.TextField(max_length=256)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum_rating = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum_rating += rating.stars
        if len(ratings) > 0:
            return sum_rating / len(ratings)
        else:
            return 0


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(5)])
    comments = models.TextField(max_length=256)

    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)

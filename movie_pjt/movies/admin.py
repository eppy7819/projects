from django.contrib import admin
from .models import Movie
from .models import Genre
from .models import Cast
from .models import Emotion
# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Cast)
admin.site.register(Emotion)
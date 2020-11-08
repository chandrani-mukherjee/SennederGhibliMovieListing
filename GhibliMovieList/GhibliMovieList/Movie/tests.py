from django.test import TestCase
from MovieCharacter.models import People
from Movie.models import Movie

class MovieTestCase(TestCase):
    def setUp(self):
        peopleObj = People.objects.create(id="people1234", name="TestPeople",gender="Female",age=30,eye_color="Black",hair_color="Black")
        movieObj = Movie.objects.create(id="movie1234", title="TestMovie",description="TestMovieDesc",director="TestDirector",producer="TestProducer",release_date="2020",rt_score="5")
        movieObj.character.add(peopleObj)

    def test_movie_list(self):
        """List movie with character"""
        movie = Movie.objects.get(title="TestMovie")
        self.assertEqual(movie.id, 'movie1234')
       

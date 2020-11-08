Steps to start the project

1. source ~\env\Scripts\activate

2. cd  GhibliMovieList\GhibliMovieList

3. python manage.py runserver

4. Access Django Admin Page in http://localhost:8000/admin/ with 

	Credentials TestUser : User1234

5. Simple POST with Token enabled to the below endpoint loads the data from Ghibli APIs

   Method: POST
   URL: http://localhost:8000/movie/movies

6. fetch movies using below endpoint

   Method: GET
   URL: http://localhost:8000/movie/movies
   
7. Get the paginated response from the above endpoint

8. Run Test using below command

   python manage.py tests


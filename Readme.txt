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

9. Find the fetch movie call response . You can move ahead to next page from the embedded URL

http://localhost:8000/movie/movies

GET /movie/movies
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 9,
    "next": "http://localhost:8000/movie/movies?page=2",
    "previous": null,
    "results": [
        {
            "id": "2de9426b-914a-4a06-a3a0-5e6d9d3886f6",
            "character": [
                {
                    "id": "89026b3a-abc4-4053-ab1a-c6d2eea68faa",
                    "name": "Niya",
                    "gender": "Male",
                    "age": "NA",
                    "eye_color": "White",
                    "hair_color": "Beige"
                }
            ],
            "title": "Arrietty",
            "description": "14-year-old Arrietty and the rest of the Clock family live in peaceful anonymity as they make their own home from items 'borrowed' from the house's human inhabitants. However, life changes for the Clocks when a human boy discovers Arrietty.",
            "director": "Hiromasa Yonebayashi",
            "producer": "Toshio Suzuki",
            "release_date": "2010",
            "rt_score": 95
        }    ]
}



10. Create movies 

http://localhost:8000/movie/movies

POST /movie/movies
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "info": "Movie Details created successfully"
}



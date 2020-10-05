import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tmdb_client

from unittest.mock import Mock

def test_get_single_movie(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_single_movie = ['Movie 1']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_single_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


   single_movie = tmdb_client.get_single_movie(movie_id="123")
   assert single_movie == mock_single_movie

   '''def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()'''
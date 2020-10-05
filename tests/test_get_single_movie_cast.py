import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tmdb_client

from unittest.mock import Mock

def test_get_single_movie_cast(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_single_movie_cast = [{"cast": "cast 1"}]
   mock_cast=mock_single_movie_cast[0]
   mock_cast_fin=mock_cast["cast"]


   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value= mock_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


   single_movie_cast = tmdb_client.get_single_movie_cast(movie_id="123")

   assert single_movie_cast == mock_cast_fin

'''def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]'''
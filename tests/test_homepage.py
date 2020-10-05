import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from unittest.mock import Mock


def test_homepage(monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200
       api_mock.assert_called_once_with('movie/popular')

'''@pytest.mark.parametrize('n, result', (
    ('movie/popular', 200),
    ('movie/now_playing', 200),
    ('movie/top_rated', 200),
    ('movie/upcoming', 200),
))
def test_homepage(monkeypatch, n, result):
    api_mock = Mock(return_value={'results': [0,1,2,3,4,5,6,7,8,9]})
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == result
        '''
import unittest


# Functions to practice writing tests for:
def get_daily_movie():
    return 'Parasite'


def get_licensed_movies():
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies


def get_wifi_status():
    return False

# Unit Tests Below: 
class EntertainmentSystemTests(unittest.TestCase):

  def test_movie_license(self):
    daily_movie = get_daily_movie()
    licensed_movies = get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  def test_wifi_status(self):
    wifi_enabled = get_wifi_status()
    self.assertTrue(wifi_enabled)

import unittest


# Functions to practice writing tests for:
def get_daily_movie():
    return 'Parasite'


def get_licensed_movies():
    licensed_movies = ['Parasite', 'Nomadland', 'Roma']
    return licensed_movies


def get_wifi_status():
    return False


def get_device_temp():
    print('Reading the temperature of the entertainment system device...')
    return 40


def get_maximum_display_brightness():
    print('Calculating maximum display brightness in nits...')
    return 399.99999999


# Unit Tests Below: 
class EntertainmentSystemTests(unittest.TestCase):

    def test_movie_license(self):
        daily_movie = get_daily_movie()
        licensed_movies = get_licensed_movies()
        self.assertIn(daily_movie, licensed_movies)

    def test_wifi_status(self):
        wifi_enabled = get_wifi_status()
        self.assertTrue(wifi_enabled)


# If the OG file changed to have more movies like so: 

# def get_daily_movies():
#     print('Retrieving the movie set to play on today\'s flight...')
#     return ['Parasite', 'Nomadland', 'Roma', 'Black Widow', 'Spiral']


# def get_licensed_movies():
#     print('Retrieving the list of licenses movies from the database...')
#     licensed_movies = ['Parasite', 'Nomadland', 'Roma']
#     return licensed_movies

# You can test MULTIPLE movies at once with the following method instead 
# (pretend this is linked to something called entertainment.py): 
    def test_movie_license(self):
        daily_movies = entertainment.get_daily_movies()
        licensed_movies = entertainment.get_licensed_movies()

        # Write your code below:
        for movie in daily_movies:
            print(movie)
            with self.subTest(movie):
                self.assertIn(movie, licensed_movies)


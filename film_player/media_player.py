import os
import string

class Player:
    def __init__(self, film_url: str, quality=720, volume=50):
        self.film_url = film_url
        self.quality = quality
        self.films = {}
        self.current_film = {}
        self.volume = volume

    def play(self) -> dict or None:
        """
        Get film data from list film

        :return: dict or None film
        """
        film = self.films.get(self.film_url)

        if film:
            self.current_film = film
            return self.current_film

    def pause(self):
        """
        Set pause to film

        :return: dict or None film
        """
        self.current_film['pause'] = True

    def save_time(self, save: bool):
        if save is True:
            # TODO: add more functionality to save time
            return
        else:
            pass

    def change_quality(self, quality: int) -> str:
        """
        Change film quality

        :param quality: int of quality
        :return: link of film
        """
        self.film_url = self.film_url
        return self.film_url

    def change_volume(self, volume: int):
        """
        Change film quality

        :param quality: int of quality
        :return:
        """
        self.volume = volume

    def __str__(self):
        return f'{self.current_film})'



def create_dirs():
    os.mkdir('film_storage')

    for letter in string.ascii_uppercase:
        path = os.path.join('film_storage', letter)
        os.mkdir(path)



if __name__ == '__main__':
    create_dirs()
import os


class Film:
    def __init__(self, film: dict, storage_address=None):
        self.film = film
        self.storage_address = storage_address
        self.path = None

    def get_attr_value(self, key: str):
        """
        Get value from key with film data

        :param key: str of key
        :return: valuer or None
        """
        return self.film.get(key)

    def upload_file(self):
        """
        Upload film

        :return:
        """
        letter = self.film['title'][0].upper()
        self.path = os.path.join('film_storage', letter, self.film['title'] + '.txt')

        with open(self.path, 'w', encoding='utf-8') as file:
            file.write('')

    def get_film_address(self):
        """
        Get ABS path of current film
        :return:
        """
        return os.path.abspath(self.path)

    def __str__(self):
        return f'{self.film["title"]})'


def main():
    data = {
        'title': 'Crazy, Stupid, Love.',
        'description': 'A middle-aged husband\'s life changes dramatically when his wife asks him for a divorce.',
        'country': 'United States',
        'Year': 2011

    }
    film = Film(film=data)
    film.upload_file()
    print(film.get_film_address())


if __name__ == '__main__':
    main()

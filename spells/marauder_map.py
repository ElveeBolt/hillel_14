import os
import json
import string
PATH_DIR_MAIN = 'Harry Potter'


class MapMagic:
    __map_open = "I solemnly swear that I am up to no good."
    __map_close = "Mischief managed."

    @staticmethod
    def map_open():
        print(MapMagic.__map_open)

    @staticmethod
    def map_close():
        print(MapMagic.__map_close)


class MarauderMap(MapMagic):
    def __init__(self, path):
        self.path = path
        self.__films_titles = {
            "results": [
                {
                    "imdb_id": "tt1201607",
                    "title": "Harry Potter and the Deathly Hallows: Part 2"
                },
                {
                    "imdb_id": "tt0241527",
                    "title": "Harry Potter and the Sorcerer's Stone"
                },
                {
                    "imdb_id": "tt0926084",
                    "title": "Harry Potter and the Deathly Hallows: Part 1"
                },
                {
                    "imdb_id": "tt0304141",
                    "title": "Harry Potter and the Prisoner of Azkaban"
                },
                {
                    "imdb_id": "tt0417741",
                    "title": "Harry Potter and the Half-Blood Prince"
                },
                {
                    "imdb_id": "tt0295297",
                    "title": "Harry Potter and the Chamber of Secrets"
                },
                {
                    "imdb_id": "tt0330373",
                    "title": "Harry Potter and the Goblet of Fire"
                },
                {
                    "imdb_id": "tt0373889",
                    "title": "Harry Potter and the Order of the Phoenix"
                }
            ]
        }

    def map_generator(self):
        self.map_open()

        # Open json
        with open(self.path, 'r') as file:
            data = json.load(file)

        # Create main dir and dir with film name
        os.mkdir(PATH_DIR_MAIN)

        for film in self.__films_titles['results']:
            path = os.path.join(PATH_DIR_MAIN, film['title'])
            os.mkdir(path)

        # Create dirs A-Z
        dirs = os.listdir(PATH_DIR_MAIN)

        for dir in dirs:
            for letter in string.ascii_uppercase:
                path = os.path.join(PATH_DIR_MAIN, dir, letter)
                os.mkdir(path)

        # Create new list
        films = {}

        for result in data:
            for film in result['results']:
                awards = {
                    'type': film['type'],
                    'award_name': film['award_name'],
                    'award': film['award']
                }

                title = film['movie']['title']

                if films.get(title):
                    films[title].append(awards)
                else:
                    films[title] = [awards]

        # Sort films
        sorted_films = {}

        for key, value in films.items():
            value = sorted(value, key=lambda val: val['award_name'])
            sorted_films[key] = value


        # Create dir
        for key, value in sorted_films.items():
            for award in value:
                letter = award['award_name'][0].upper()
                path = os.path.join(PATH_DIR_MAIN, key, letter, award['award_name'] + '.txt')

                with open(path, 'w') as file:
                    file.write('')

        # Create Files
        for key, value in sorted_films.items():
            for award in value:
                try:
                    letter = award['award'][0].upper()
                except IndexError:
                    continue

                path = os.path.join(PATH_DIR_MAIN, key, letter, award['award'] + '.txt')

                try:
                    with open(path, 'w') as file:
                        file.write('')
                except FileNotFoundError:
                    continue

        # Create Files
        for key, value in sorted_films.items():
            for award in value:
                letter = award['award_name'][0].upper()

                path = os.path.join(PATH_DIR_MAIN, key, letter, award['award_name'] + '.txt')

                with open(path, 'w+') as file:
                    file.write(award['award'] + '\n')

        self.map_close()




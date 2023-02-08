import os
import string
from data import films_awards, films_titles
from spells import unforgivable_сurses

PATH_DIR_MAIN = 'Harry Potter'


def create_main_dir():
    """
    Create dirs with film name in main path

    :return:
    """
    os.mkdir(PATH_DIR_MAIN)
    for film in films_titles['results']:
        path = os.path.join(PATH_DIR_MAIN, film['title'])
        os.mkdir(path)


def create_tek():
    """
    Create dirs with name A-Z in main path

    :return:
    """
    dirs = os.listdir(PATH_DIR_MAIN)

    for dir in dirs:
        for letter in string.ascii_uppercase:
            path = os.path.join(PATH_DIR_MAIN, dir, letter)
            os.mkdir(path)


def get_films_awards() -> dict:
    """
    Get all awards from films

    :return:
    """
    films = {}

    for result in films_awards:
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

    return films


def sort_films(films: dict) -> dict:
    """
    Sort dict of films by list of award_name

    :param films: dict of film
    :return: sorted dict
    """
    for key, value in films.items():
        value = sorted(value, key=lambda val: val['award_name'])
        films[key] = value

    return films


def create_file_award_name(films: dict):
    """
    Create files in A-Z dirs with first symbols in Award name

    :param films: dict of films
    :return:
    """
    for key, value in films.items():
        for award in value:
            letter = award['award_name'][0].upper()
            path = os.path.join(PATH_DIR_MAIN, key, letter, award['award_name'] + '.txt')

            with open(path, 'w') as file:
                file.write('')


def create_file_award(films: dict):
    """
    Create files in A-Z dirs with first symbols in Award

    :param films: dict of films
    :return:
    """
    for key, value in films.items():
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


def add_awards(films: dict):
    """
    Add awards in files with award name

    :param films: dict of films
    :return:
    """
    for key, value in films.items():
        for award in value:
            letter = award['award_name'][0].upper()

            path = os.path.join(PATH_DIR_MAIN, key, letter, award['award_name'] + '.txt')

            with open(path, 'w+') as file:
                file.write(award['award'] + '\n')


def main():
    # LESSON 12
    create_main_dir()
    create_tek()

    films_award = get_films_awards()
    sorted_films = sort_films(films_award)
    create_file_award_name(sorted_films)
    create_file_award(sorted_films)
    add_awards(sorted_films)

    # LESSON 14
    unforgivable_сurses.save_json(data=films_awards, path='film_awards.json')
    unforgivable_сurses.avada_kedavra(PATH_DIR_MAIN)
    unforgivable_сurses.imperius('film_awards.json')

if __name__ == '__main__':
    main()

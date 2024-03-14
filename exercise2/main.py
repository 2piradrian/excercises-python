import os
import click
import requests
import datetime
import pandas as pd

PATH = "trivia"


def get_trivia(url):
    response = requests.get(url).text
    # click.echo(response)

    return response


def set_path():
    if not os.path.exists(PATH):
        os.mkdir(PATH)

    os.chdir(PATH)


# @click.command()
# @click.option('--number', type=int, default=1, help='Number to search.')
# def main(number):
#    url = f'http://numbersapi.com/{number}/'
#    get_trivia(url)


def main():
    number = datetime.datetime.now().minute
    url = f'http://numbersapi.com/{number}/'

    trivia = get_trivia(url)
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    set_path()
    full_path = f'trivia_{timestamp}.txt'

    with open(full_path, "w") as file:
        file.write(trivia)
        file.close()


if __name__ == "__main__":
    main()

import click
import requests


def get_trivia(url):
    response = requests.get(url).text
    click.echo(response)


@click.command()
@click.option('--number', type=int, default=1, help='Number to search.')
def main(number):
    url = f'http://numbersapi.com/{number}/'
    get_trivia(url)


if __name__ == "__main__":
    main()

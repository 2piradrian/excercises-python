import requests
import re
import os

URL = 'https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python-Regular-Expressions/data.txt'
PATH = 'C:\\Users\\Adrian\\Documents\\Python\\exercise1\\data'


def get_data():
    request = requests.get(URL)
    return request.text


def get_patterns():
    return {
        "name": re.compile(r'^[A-Za-z]{3,} [A-Za-z\-]{3,}$'),
        "phone": re.compile(r'\d{3}-\d{3}-\d{4}'),
        "email": re.compile(r'^\w{4,}@\w{3,}.com'),
        "url": re.compile(r'[A-Z]{2}\s\d{5}'),

    }


def set_path():
    if not os.path.exists(PATH):
        os.mkdir(PATH)

    os.chdir(PATH)


def save_data(data, folder):
    full_path = os.path.join(PATH, folder)

    if not os.path.exists(full_path):
        os.mkdir(full_path)
    os.chdir(full_path)

    with open(f'${folder}.txt', "w") as file:
        for line in data:
            file.write(line + "\n")

    os.chdir(PATH)  # Remember come back


def process_and_save(response):
    patterns = get_patterns()

    names = re.findall(patterns["name"].pattern, response, re.MULTILINE)
    phones = re.findall(patterns["phone"].pattern, response, re.MULTILINE)
    emails = re.findall(patterns["email"].pattern, response, re.MULTILINE)

    save_data(phones, "phones")
    save_data(names, "names")
    save_data(emails, "emails")


def main():
    set_path()

    response = get_data()
    process_and_save(response)


if __name__ == "__main__":
    main()

# matches = pattern.findall(text)

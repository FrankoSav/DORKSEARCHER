import os
import requests
import re
from termcolor import colored
import pyfiglet


def banner():
    banner = "DORK-SEARCHER"
    print(banner)
    print("By:FrankoSav")


banner()


def menu():
    print("1. Find websites vulnerable to SQL injection")
    print("2. Salir")
    choice = input("Select A Option: ")
    if choice == "1":
        search_dorks()
    elif choice == "2":
        return
        exit()
    else:
        print("Invalid option. Try again")
        menu()


def search_dorks():
    try:
        with open("dorks.txt", "r") as file:
            dorks = file.read().splitlines()
    except FileNotFoundError:
        print("File not found, please create a dorks.txt file in your home directory.")
        exit()

    for dork in dorks:
        search_results = requests.get(
            "https://www.google.com/search?q=" + dork)
        search_results = search_results.text

        links = re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', search_results)

    for link in links:
        try:
            url = link + "'"
            response = requests.get(url)

            if "SQL" in response.text:
                print(colored("[+] " + url, 'green'))
            else:
                print(colored("[X] " + url, 'red'))
        except:
            print(colored("[X] " + url, 'red'))


menu()

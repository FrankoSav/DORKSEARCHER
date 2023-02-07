import os
import requests
import re
from termcolor import colored
import pyfiglet


def banner():
    banner = "L0C4L-SC4MM3R"
    print(banner)


banner()


def menu():
    print("1. Buscar sitios web vulnerables a inyección SQL")
    print("2. Salir")
    choice = input("Seleccione una opción: ")
    if choice == "1":
        search_dorks()
    elif choice == "2":
        return
        exit()
    else:
        print("Opción inválida. Intente de nuevo.")
        menu()


def search_dorks():
    try:
        with open("dorks.txt", "r") as file:
            dorks = file.read().splitlines()
    except FileNotFoundError:
        print("Archivo no encontrado, por favor crea un archivos dorks.txt en tu directorio home.")
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

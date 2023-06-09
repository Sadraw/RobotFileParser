#!/usr/bin/env python3
from urllib.robotparser import RobotFileParser
from termcolor import colored

while True:
    url = input(colored("Enter a website (or 'q' to quit): ", "blue"))

    if url == 'q':
        print(colored("Bye Bye!", "yellow"))
        break

    url = url if url.startswith("https://") else "https://" + url

    rp = RobotFileParser()
    rp.set_url(f"{url}/robots.txt")
    rp.read()

    if rp.can_fetch('*', url):
        print(colored("Web scraping is allowed", "green"))
    else:
        print(colored("Web scraping is NOT allowed", "red"))
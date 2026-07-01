import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("h3")

print("\nBook Titles:\n")

for book in books:
    print(book.a["title"])
with open("book_titles.txt", "w") as file:
    for book in books:
        file.write(book.a["title"] + "\n")
print("\nBook titles saved to book_titles.txt")
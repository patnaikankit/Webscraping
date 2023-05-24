from bs4 import BeautifulSoup
import requests
import time
import csv

def findBooks():
    html_text = requests.get('http://books.toscrape.com/').text
    soup = BeautifulSoup(html_text, 'lxml')
    books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for index, book in enumerate(books):
        name = book.h3.a.get('title')
        cost = book.find('p', class_='price_color').text
        link = book.h3.a['href']
        availability = book.find('p', class_='instock availability').text
        review = str(book.p.get('class'))
        if 'One' in review:
            rating = 1
        elif 'Two' in review:
            rating = 2
        elif 'Three' in review:
            rating = 3
        elif 'Four' in review:
            rating = 4
        else:
            rating = 5
        if 'In' in availability:
            with open(f'books/{index}.txt', 'w') as file:
                file.write(f"Book Name: {name} \n")
                file.write(f"Book Price: {cost} \n")
                file.write(f"Book Rating: {rating} stars\n")
                file.write(f"Book Link: https://books.toscrape.com/{link} \n")
            print(f"File Saved: {index}")

            with open(f'books/book.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([name, cost, rating, link])


if __name__ == "__main__":
    while True:
        findBooks()
        time_wait = 10
        print(f"Refreshing in {time_wait} minutes...")
        time.sleep(time_wait*60)
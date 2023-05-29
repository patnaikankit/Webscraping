from bs4 import BeautifulSoup
import csv
import requests
import time

def find_jobs():
    html_text = requests.get('https://internshala.com/internships/work-from-home-backend-development,front-end-development,full-stack-development-internships/').text
    soup = BeautifulSoup(html_text, 'lxml')
    internships = soup.find_all('div', class_='container-fluid individual_internship visibilityTrackerItem')
    for index, internship in enumerate(internships):
        company_name = internship.find('a', class_='link_display_like_text view_detail_button').text.replace(' ', '')
        stipend = internship.find('span', class_ = 'stipend').text.replace(' ', '')
        link = internship.h4.a['href']
        with open(f'internships/{index}.txt', 'w') as file:
            file.write(f"Company Name: {company_name.strip()} \n")
            file.write(f"Stipend: {stipend.strip()} \n")
            file.write(f"Link: https://internshala.com/internship/detail/{link.strip()} \n")
        print(f"File Saved: {index}")

        with open(f'internships/internship.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow([company_name, stipend, link])

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes..')
        time.sleep(time_wait*60)

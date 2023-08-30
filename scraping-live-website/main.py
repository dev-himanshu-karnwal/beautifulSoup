import requests
import time
from bs4 import BeautifulSoup


def strip(st):
    return st.strip()


def find_jobs():
    response = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=#')
    webpage_html = response.text

    soup = BeautifulSoup(webpage_html, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    complete_details = ''

    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' not in published_date:
            continue

        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = ', '.join(list(map(strip,
                                    job.find('span', class_='srp-skills').text.split(','))))
        if any(required_skill in unfamiliar_skills for required_skill in skills.lower().split(', ')):
            continue

        more_info = job.header.h2.a['href']

        # print(job)
        # print(company_name)
        # print(skills)
        # print(published_date)

    #     print(f'''Company Name: {company_name}
    # Required Skills: {skills}
    # Published Date: {published_date}
    # ''')
        complete_details += f'Company Name: {company_name}\n'
        complete_details += f'Key Skills: {skills}\n'
        complete_details += f'For more info (goto): {more_info}\n\n'

    with open('D:/Self Written & Practice/Python/Udemy/web scraping/beautiful soup/scraping-live-website/jobs.txt', 'w') as file:
        file.write(complete_details)
    print(complete_details)
    # file.write(f'Company Name: {company_name}\n')
    # file.write(f'Key Skills: {skills}\n')
    # file.write(f'For more info (goto): {more_info}\n\n')

    # print(f'Company Name: {company_name}')
    # print(f'Key Skills: {skills}')
    # print(f'For more info (goto): {more_info}\n')


if __name__ == '__main__':
    unfamiliar_skills = input(
        'Enter skills you are unfamiliar too\n> ').strip()
    print(f'Filtering out {unfamiliar_skills}..\n')

    while True:
        find_jobs()
        print('Wait for 10 seconds to get more latest jobs...\nSearching in Progress')
        time.sleep(10)

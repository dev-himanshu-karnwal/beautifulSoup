from bs4 import BeautifulSoup
import lxml
import requests

# with open('D:/Self Written & Practice/Python/Udemy/web scraping/beautiful soup/website.html', encoding='utf8') as html_file:
#     html_code = html_file.read()

# soup = BeautifulSoup(html_code, 'html.parser')
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.getText())

# all_a = soup.find_all(name='a')
# print(type(a))
# print(a)
# for a in all_a:
#     print(a, a.string, a.getText(), sep='\n', end='\n\n')
#     print(a.get('id'))
#     print(type(a.get('id')))

# print(soup.find(name='h1', id='name'))
# print(soup.select_one(selector='p a'))


# print(response.text)


# all_titles = soup.select('table tbody tr td table tbody tr td span a')
# print(all_titles)

# all_titles = soup.select(selector='.explore_problem__YUJcf .explore_problemContainerTxt__kyh8P div')
# print(all_titles)

# def get_all_articles(soup: BeautifulSoup):
#     # Get all article details
#     articles = soup.findAll(name="span", class_="titleline")

#     article_texts = []
#     article_links = []

#     for article in articles:
#         article_texts.append(article.getText())
#         article_links.append(article.contents[0].get("href"))

#     upvotes = soup.findAll(class_="score")
#     article_upvotes = [int(item.getText().strip(" points"))
#                        for item in upvotes]

#     return article_texts, article_links, article_upvotes


# def sort_results(lists):
#     # The list used as the sort index must be the first item in zip()
#     sorted_lists = [(x, y, z) for (z, x, y) in sorted(
#         zip(lists[2], lists[0], lists[1]), reverse=True)]

#     return sorted_lists


# response = requests.get(
#     'https://practice.geeksforgeeks.org/explore?page=1&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions&sprint_name=SDE%20Sheet')
# response.raise_for_status()

# soup = BeautifulSoup(response.text, 'html.parser')
# article_texts, article_links, article_upvotes = get_all_articles(soup=soup)
# print(article_texts, article_links, article_upvotes, sep='\n\n')


header = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,da;q=0.7,hi;q=0.6,pa;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}
response = requests.get(
    'https://www.amazon.in/realme-Wireless-Bluetooth-Headphones-Connection/dp/B0C8VJ1GQQ?ref_=Oct_DLandingS_D_4e701a43_2', headers=header)
response.raise_for_status()

# print(response.text)

soap = BeautifulSoup(response.text, 'lxml')
print(soap)

print(soap.select_one('.a-price-whole'))

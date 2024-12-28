# Parsing for sqlalchemy

# from databases.qyerysets import *
# from bs4 import BeautifulSoup 
# import requests

# def get_html(url):
#     headers = {'User-Agent':
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.text
#     else:
#         return None
    
# def get_movie_data(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     main_data = soup.find_all('div', class_="article-detail__content")
#     movies = []
#     for data in main_data:
#         titles = data.find('div', class_='article-detail_tag article-detail_tag_h2')
#         if titles == None:
#             continue
#         else:
#             titles2 = data.find_all('div', class_='article-detail_tag article-detail_tag_h2')
#             for title2 in titles2:
#                 title = title2.text.strip()
#             countries = data.find('div', class_='article-detail_tag article-detail_tag_p')
#             if country == None:
#                 continue
#             else:
#                 country2 = data.find('article', class_='article-detail_tag article-detail_tag_p')
#                 for country3 in country2:
#                     if 'Страна' in country3.text.strip():
#                         country = countries.text.tcrip()
#                     if 'В ролях' in country3.text.strip():
#                         actors =  countries.text.strip()
#             images = data.find_all('div', class_='article-element article-element_images')
#             if images == None:
#                 continue 
#             else:
#                 images2 = data.find_all('div', class_='article-element article-element_images')
#                 for image2 in images2:
#                     image = image2.find('img').get('src')
#     movies.append({
#         'title': title,
#         'country': country,
#         'description': actors,
#         'trailer': image,
#         'age_limit': 18,
#         'realese_date': '2024-01-01',
#         'image': image,
#         'url': 2

#     })  
#     return movies               


# def parsing_main():
#     url = "https://www.pravilamag.ru/entertainment/672783-100-luchshih-filmov-vseh-vremen-vybor-amerikanskogo-esquire/ "
#     html = get_html(url)
#     headers = {'User-Agent':
#                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
#     response = requests.get(url, headers=headers)
   
#     soup = BeautifulSoup(response.text, 'html.parser')
#     main_data = soup.find_all('div', class_="article-detail__content")
#     movies = []
#     for data in main_data:
#         titles = data.find('div', class_='article-detail_tag article-detail_tag_h2')
#         if titles == None:
#             continue
#         else:
#             titles2 = data.find_all('div', class_='article-detail_tag article-detail_tag_h2')
#             for title2 in titles2:
#                 title = title2.text.strip()
#             countries = data.find('div', class_='article-detail_tag article-detail_tag_p')
#             if country == None:
#                 continue
#             else:
#                 country2 = data.find('article', class_='article-detail_tag article-detail_tag_p')
#                 for country3 in country2:
#                     if 'Страна' in country3.text.strip():
#                         country = countries.text.strip()
#                     if 'В ролях' in country3.text.strip():
#                         actors =  countries.text.strip()
#             images = data.find_all('div', class_='article-element article-element_images')
#             if images == None:
#                 continue 
#             else:
#                 images2 = data.find_all('div', class_='article-element article-element_images')
#                 for image2 in images2:
#                     image = image2.find('img').get('src')

#     movies.append({
#         'title': title,
#         'country': country,
#         'description': actors,
#         'trailer': image,
#         'age_limit': 18,
#         'realese_date': '2024-01-01',
#         'image': image,
#         'url': 2

#     })  
#     return movies  

# from scrip.parsing import parsing_main
# async def add_movies():
#     movie = parsing_main()
#     async with async_session() as session:
#         for m in movie:
#             movies = Movies(poster=m['poster'],
#                              title=m['title'], 
#                              release_date=m['release_date'], 
#                              description=m['description'], 
#                              country=m['country'],
#                                age_limit=m['age_limit'], 
#                                trailer=m['trailer'], 
#                                url_id=m['url_id'])
#             session.add(movies)
#         await session.commit()






from databases.qyerysets import *
from bs4 import BeautifulSoup
import requests

def get_html(url):
    headers = {'User-Agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

def get_movie_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    main_data = soup.find_all('div', class_="article-detail__content")
    movies = []
    for data in main_data:
        title1 = None  # Инициализация переменной
        country = None  # Инициализация переменной
        actors = None  # Инициализация переменной
        image = None  # Инициализация переменной

        titles = data.find('div', class_='article-detail_tag article-detail_tag_h2')
        if titles:
            titles2 = data.find_all('div', class_='article-detail_tag article-detail_tag_h2')
            for title2 in titles2:
                title1 = title2.text.strip()  # Используем strip для удаления лишних пробелов

        countries = data.find('div', class_='article-detail_tag article-detail_tag_p')
        if countries:
            country2 = data.find_all('article', class_='article-detail_tag article-detail_tag_p')
            for country3 in country2:
                if 'Страна' in country3.text.strip():
                    country = countries.text.strip()
                if 'В ролях' in country3.text.strip():
                    actors = countries.text.strip()

        images = data.find_all('div', class_='article-element article-element_images')
        if images:
            for image2 in images:
                image = image2.find('img').get('src')

        # Добавляем данные фильма в список
        if title1 and country and actors and image:  # Проверяем, что все данные есть
            movies.append({
                'title': title1,
                'country': country,
                'description': actors,
                'trailer': image,
                'age_limit': 18,
                'realese_date': '2024-01-01',
                'image': image,
                'url': 2
            })
    return movies

def parsing_main():
    url = "https://www.pravilamag.ru/entertainment/672783-100-luchshih-filmov-vseh-vremen-vybor-amerikanskogo-esquire/"
    html = get_html(url)
    if html:
        return get_movie_data(html)
    else:
        return []

# Асинхронная часть
from scrip.parsing import parsing_main

async def add_movies():
    movie = parsing_main()  # Получаем данные о фильмах
    async with async_session() as session:
        for m in movie:
            movies = Movies(poster=m['image'],
                             title=m['title'], 
                             release_date=m['realese_date'], 
                             description=m['description'], 
                             country=m['country'],
                             age_limit=m['age_limit'], 
                             trailer=m['trailer'], 
                             url_id=m['url'])
            session.add(movies)
        await session.commit()

    













from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup,KeyboardButton,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from databases.qyerysets import *

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог фильмов')],
    [KeyboardButton(text='Каталог сериалов')],
    [KeyboardButton(text ='Каталог жанров')],
    [KeyboardButton(text = 'поиск по актерам')],
    [KeyboardButton(text = 'поиск по режиссерам')],
    [KeyboardButton(text='Поиск фильмов по названию')],
    [KeyboardButton(text='Поиск фильмов по актерам')],
     [KeyboardButton(text='Поиск фильмов по режиссеру')]
],  resize_keyboard=True, input_field_placeholder='Выберите кнопку')

PAGE_SIZE = 2
async def get_movies_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    movies = await all_movies(offset=offset,limit=PAGE_SIZE)
    for movie in movies:
        kb.add(InlineKeyboardButton(text=movie.title, callback_data=f'movie_{movie.id}'))

    if page > 1:
        kb.add(InlineKeyboardButton(text="◀️", callback_data=f'page_{page-1}'))

    if len(movies) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text="▶️", callback_data=f'page_{page+1}'))
    return kb.adjust(2).as_markup()

async def get_movies_kb_admin():
    kb = InlineKeyboardBuilder()
    movies = await all_movies()
    for movie in movies:
        kb.add(InlineKeyboardButton(text=movie.title, callback_data=f'movie2_admin_{movie.id}'))
    return kb.adjust(2).as_markup()

PAGE_SIZE = 2
async def get_series_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    series = await all_series(offset=offset,limit=PAGE_SIZE)
    for seria in series:
        kb.add(InlineKeyboardButton(text=seria.title, callback_data=f'seria_{seria.id}'))

    if page > 1:
        kb.add(InlineKeyboardButton(text="◀️", callback_data=f'page_{page-1}'))

    if len(series) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text="▶️", callback_data=f'page_{page+1}'))
    return kb.adjust(2).as_markup()

async def get_series_kb_admin():
    kb = InlineKeyboardBuilder()
    series = await all_series()
    for seria in series:
        kb.add(InlineKeyboardButton(text=seria.title, callback_data=f'seria2_admin_{seria.id}'))
    return kb.adjust(2).as_markup()




PAGE_SIZE = 2
async def get_genre_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    genre = await all_genre(offset=offset,limit=PAGE_SIZE)
    for gen in genre:
        kb.add(InlineKeyboardButton(text=gen.name, callback_data=f'genre_{gen.id}'))

    if page > 1 :
        kb.add(InlineKeyboardButton(text="◀️", callback_data=f'page_{page-1}'))

    if len(genre) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text="▶️", callback_data=f'page_{page+1}'))


    return kb.adjust(2).as_markup()

async def get_genre_kb_admin():
    kb = InlineKeyboardBuilder()
    genre = await all_genre()
    for gen in genre:
        kb.add(InlineKeyboardButton(text=gen.name, callback_data=f'genre2_admin_{gen.id}'))
    return kb.adjust(2).as_markup()

PAGE_SIZE = 2
async def get_actors_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    actors = await all_actor(offset=offset,limit=PAGE_SIZE)
    for actor in actors:
        kb.add(InlineKeyboardButton(text=f'{actor.first_name} {actor.last_name}', callback_data=f'actor_{actor.id}'))

    if page > 1:
        kb.add(InlineKeyboardButton(text="◀️", callback_data=f'page_{page-1}'))

    if len(actors) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text="▶️", callback_data=f'page_{page+1}'))
    return kb.adjust(2).as_markup()

async def get_actors_kb_admin():
    kb = InlineKeyboardBuilder()
    actors = await all_actor()
    for actor in actors:
        kb.add(InlineKeyboardButton(text=f'{actor.first_name} {actor.last_name}', callback_data=f'actors2_admin_{actor.id}'))
    return kb.adjust(2).as_markup()

PAGE_SIZE = 2
async def get_directors_kb(page):
    offset = (page - 1) * PAGE_SIZE
    kb = InlineKeyboardBuilder()
    directors = await all_actor(offset=offset,limit=PAGE_SIZE)
    for director in directors:
        kb.add(InlineKeyboardButton(text=f'{director.first_name} {director.last_name}', callback_data=f'director_{director.id}'))

    if page > 1:
        kb.add(InlineKeyboardButton(text="◀️", callback_data=f'page_{page-1}'))

    if len(directors) == PAGE_SIZE:
        kb.add(InlineKeyboardButton(text="▶️", callback_data=f'page_{page+1}'))
    return kb.adjust(2).as_markup()

async def get_directors_kb_admin():
    kb = InlineKeyboardBuilder()
    directors = await all_director()
    for director in directors:
        kb.add(InlineKeyboardButton(text=f'{director.first_name} {director.last_name} ', callback_data=f'directors2_admin_{director.id}'))
    return kb.adjust(2).as_markup()


PAGE_SIZE = 2

async def get_movies_by_genre_kb(genre_id):
    kb = InlineKeyboardBuilder()
    movies = await get_movies_by_genre(genre_id)
    for movie in movies:
        kb.add(InlineKeyboardButton(text=movie.title,
            callback_data=f"movie_{movie.id}"))
    kb.add(InlineKeyboardButton(text='Назад', callback_data=f'back_to_genre'))
    return kb.adjust(2).as_markup()

async def get_movies_by_actor_kb(actor_id):
    kb = InlineKeyboardBuilder()
    movies = await get_movies_by_actor(actor_id)
    for movie in movies:
        kb.add(InlineKeyboardButton(text=movie.title,
            callback_data=f"actor_{movie.id}"))
    kb.add(InlineKeyboardButton(text='Назад', callback_data=f'back_to_actor'))
    return kb.adjust(2).as_markup()

async def get_movies_by_director_kb(director_id):
    kb = InlineKeyboardBuilder()
    movies = await get_movies_by_director(director_id)
    for movie in movies:
        kb.add(InlineKeyboardButton(text=movie.title,
            callback_data=f"director_{movie.id}"))
    kb.add(InlineKeyboardButton(text='Назад', callback_data=f'back_to_director'))    

    return kb.adjust(2).as_markup()


async def back_kb():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text='Назад', callback_data=f'back_to_genre'))
    return kb.adjust(2).as_markup()

async def back1_kb():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text='Назад', callback_data=f'back_to_actor'))
    return kb.adjust(2).as_markup()

async def back2_kb():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text='Назад', callback_data=f'back_to_director'))
    return kb.adjust(2).as_markup()

    
# async def get_movies_by_title_kb(title):
#     kb = InlineKeyboardBuilder()
#     movies = await get_movies_by_title(title)
#     if movies:
#         for m in movies:
#             kb.add(InlineKeyboardButton(text=m.title, callback_data=f'movie_{m.id}'))
#             return kb.adjust(2).as_markup()
        

















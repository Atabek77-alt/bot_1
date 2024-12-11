from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup,KeyboardButton,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from databases.qyerysets import *

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог фильмов')],
    [KeyboardButton(text='Каталог сериалов')],
    [KeyboardButton(text ='Каталог жанров')],
    [KeyboardButton(text = 'поиск по актерам')],
    [KeyboardButton(text = 'поиск по режиссерам')],
    [KeyboardButton(text='Поиск фильмов по названию')]
],  resize_keyboard=True, input_field_placeholder='Выберите кнопку')

async def get_movies_kb():
    kb = InlineKeyboardBuilder()
    movies = await all_movies()
    for movie in movies:
        kb.add(InlineKeyboardButton(text=movie.title, callback_data=f'movie_{movie.id}'))
    return kb.adjust(2).as_markup()

async def get_series_kb():
    kb = InlineKeyboardBuilder()
    series = await all_series()
    for seria in series:
        kb.add(InlineKeyboardButton(text=seria.title, callback_data=f'seria_{seria.id}'))
    return kb.adjust(2).as_markup()

async def get_genre_kb():
    kb = InlineKeyboardBuilder()
    genre = await all_genre()
    for gen in genre:
        kb.add(InlineKeyboardButton(text=gen.name, callback_data=f'gen_{gen.id}'))
    return kb.adjust(2).as_markup()

async def get_actors_kb():
    kb = InlineKeyboardBuilder()
    actors = await all_actor()
    for actor in actors:
        kb.add(InlineKeyboardButton(text=f'{actor.first_name} {actor.last_name}', callback_data=f'actor_{actor.id}'))
    return kb.adjust(2).as_markup()

async def get_directors_kb():
    kb = InlineKeyboardBuilder()
    directors = await all_director()
    for director in directors:
        kb.add(InlineKeyboardButton(text=f'{director.first_name} {director.last_name} ', callback_data=f'director_{director.id}'))
    return kb.adjust(2).as_markup()




# ikb = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Форест Гамп', callback_data='hello')],
#     [InlineKeyboardButton(text='Бойцовский клуб', callback_data='bye' )]
# ])


















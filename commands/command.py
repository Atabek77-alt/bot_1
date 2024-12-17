from aiogram import Router, types
from aiogram.filters import Command,CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram import F
import re
from commands.keyboards_tg import *
from aiogram.utils.media_group import MediaGroupBuilder


command_router = Router()

# @command_router.message(F.text)
# async def srart_handler(message:Message):
#     if re.match(r'^/start$', message.text, re.IGNORECASE):
        # await message.answer(f"Hello, @{message.from_user.username}!")


# @command_router.message(F.text)
# async def echo(message: types.Message):
#     await message.answer(message.text)



@command_router.message(Command('start'))
async def message_handler(message:Message):
    await message.answer('Привет! Я бот по подборке фильмов', reply_markup=kb)

# @command_router.message(lambda message: message.text == 'Каталог')
# async def katalog_handler(message: types.Message):
#     await message.answer("Выберите фильм:", reply_markup=ikb)



@command_router.message(F.text == 'Каталог фильмов')
async def movies_handler(message: Message):
    await message.answer(f'Каталог фильмов', reply_markup=await get_movies_kb())

@command_router.message(F.text == 'Каталог сериалов')
async def series_handler(message: Message):
    await message.answer(f'Каталог сериалов', reply_markup=await get_series_kb())
                                   
@command_router.message(F.text == 'Каталог жанров')
async def genre_handler(message: Message):
    await message.answer(f'Каталог жанров', reply_markup=await get_genre_kb())

@command_router.message(F.text == 'поиск по актерам')
async def actors_handler(message: Message):
    await message.answer(f'поиск по актерам', reply_markup=await get_actors_kb())

@command_router.message(F.text == 'поиск по режиссерам')
async def directors_handler(message: Message):
    await message.answer(f'поиск по режиссерам', reply_markup=await get_directors_kb())

@command_router.callback_query(F.data.startswith('movie_'))
async def movie_detail_handler(callback: CallbackQuery):
    movie_id = callback.data.split('_')[1]  # movie_1
    movie = await get_movie_by_id(movie_id=movie_id)
    album = MediaGroupBuilder(caption=f'Название: {movie.title}\n'
                                                f'Год выпуска: {movie.release_date}\n'
                                                # f'Режиссер: {movie.movie_directors.directors.first_name} {movie.movie_directors.directors.last_name}\n'
                                                f'Описание: {movie.description}\n'
                                                f'Страна: {movie.country}\n'
                                                f'Возрастное ограничение: {movie.age_limit}')
    
    if movie.poster.startswith('http') or movie.poster.startswith('AgA'):
        album.add_photo(media=movie.poster)
       
    else:
         album.add_photo(media=FSInputFile(movie.poster))
         

    if movie.trailer.startswith('http') or movie.trailer.startswith('AgA'):
        album.add_video(media=movie.trailer)
    else:
        album.add_photo(media=FSInputFile(movie.trailer))

    await callback.message.answer_media_group(media=album.build())

@command_router.callback_query(F.data.startswith('seria_'))
async def seria_detail_handler(callback: CallbackQuery):
    seria_id = callback.data.split('_')[1]  # movie_1
   
    seria = await get_seria_by_id(seria_id=seria_id)
    album = MediaGroupBuilder(caption=f'Название: {seria.title}\n'
                                                f'Год выпуска: {seria.release_date}\n'
                                                # f'Режиссер: {movie.movie_directors.directors.first_name} {movie.movie_directors.directors.last_name}\n'
                                                f'Описание: {seria.description}\n'
                                                f'Страна: {seria.country}\n'
                                                f'Сезон: {seria.seasons}\n'
                                                f'Возрастное ограничение: {seria.age_limit}')
    
    if seria.poster.startswith('http') or seria.poster.startswith('AgA'):
        album.add_photo(media=seria.poster)
       
    else:
         album.add_photo(media=FSInputFile(seria.poster))
         

    if seria.trailer.startswith('http') or seria.trailer.startswith('AgA'):
        album.add_video(media=seria.trailer)
    else:
        album.add_photo(media=FSInputFile(seria.trailer))

    await callback.message.answer_media_group(media=album.build())

@command_router.callback_query(F.data.startswith('actors_'))
async def actors_detail_handler(callback: CallbackQuery):
    actors_id = callback.data.split('_')[1]  # movie_1
    
    actors = await get_seria_by_id(actors_id=actors_id)
    album = MediaGroupBuilder(caption=f'Имя: {f'{actors.first_name} {actors.last_name}'}\n'
                                                f'Год рождение: {actors.birth_day}\n'
                                                # f'Режиссер: {movie.movie_directors.directors.first_name} {movie.movie_directors.directors.last_name}\n'
                                                f'Описание: {actors.description}\n')
                                             
                                              
                                          
    
    if actors.poster.startswith('http') or actors.poster.startswith('AgA'):
        album.add_photo(media=actors.poster)
       
    else:
         album.add_photo(media=FSInputFile(actors.poster))
         

  

    await callback.message.answer_media_group(media=album.build())


@command_router.callback_query(F.data.startswith('directors_'))
async def directors_detail_handler(callback: CallbackQuery):
    directors_id = callback.data.split('_')[1]  # movie_1
    
    directors = await get_seria_by_id(directors_id=directors_id)
    album = MediaGroupBuilder(caption=f'Имя: {f'{directors.first_name} {directors.last_name}'}\n'
                                                f'Год рождение: {directors.birth_day}\n'
                                                # f'Режиссер: {movie.movie_directors.directors.first_name} {movie.movie_directors.directors.last_name}\n'
                                                f'Описание: {directors.description}\n')
                                             
                                              
                                          
    
    if directors.poster.startswith('http') or directors.poster.startswith('AgA'):
        album.add_photo(media=directors.poster)
       
    else:
         album.add_photo(media=FSInputFile(directors.poster))
         

  

    await callback.message.answer_media_group(media=album.build())



@command_router.callback_query(F.data.startswith('genre_'))
async def movie_by_genre_handler(callback: CallbackQuery):
    g_id = callback.data.split('_')[1]  # genre_1
    await callback.message.answer(f'Фильмы по жанру',
         reply_markup=await get_movies_by_genre_kb(g_id))
    
@command_router.callback_query(F.data.startswith('actor_'))
async def movie_by_actor_handler(callback: CallbackQuery):
    a_id = callback.data.split('_')[1]  # genre_1
    await callback.message.answer(f'Фильмы с актерами',
         reply_markup=await get_movies_by_actor_kb(a_id)) 

    
@command_router.callback_query(F.data.startswith('director_'))
async def movie_by_director_handler(callback: CallbackQuery):
    d_id = callback.data.split('_')[1]  # genre_1
    await callback.message.answer(f'Фильмы по режиссерам',
         reply_markup=await get_movies_by_director_kb(d_id)) 
    















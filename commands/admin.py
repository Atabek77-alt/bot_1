from aiogram import Router, types
from aiogram.filters import Command,CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram import F
import re
from commands.keyboards_tg import *
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from config import ADMIN_ID
from databases.qyerysets import *
admin_router = Router()


class AddMovie(StatesGroup):
    add_m_title = State()
    add_m_poster = State()
    add_m_release_date = State()
    add_m_description = State()
    add_m_country = State()
    add_m_age_limit = State()
    add_m_trailer = State()
    add_m_url = State()

async def check_admin(message: Message):
    return message.from_user.id == ADMIN_ID
   


@admin_router.message(Command('add_movie'))
async def add_movie_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer('Это команда только для Администратора')
        return
    await message.answer('Введите название фильма')
    await state.set_state(AddMovie.add_m_title)

@admin_router.message(AddMovie.add_m_title)
async def add_movie_title(message:Message, state: FSMContext):
    await state.update_data(add_m_title=message.text)
    await message.answer('Отправьте постер для фильма')
    await state.set_state(AddMovie.add_m_poster)

@admin_router.message(AddMovie.add_m_poster)
async def add_movie_poster(message:Message, state: FSMContext):
    await state.update_data(add_m_poster=message.photo[0].file_id)
    await message.answer('Отправьте постер для фильма \n Пример: Год-месяц-день')
    await state.set_state(AddMovie.add_m_release_date)

@admin_router.message(AddMovie.add_m_release_date)
async def add_movie_release_date(message:Message, state: FSMContext):
    await state.update_data(add_m_release_date=message.text)
    await message.answer('Введите описание фильма')
    await state.set_state(AddMovie.add_m_description)

@admin_router.message(AddMovie.add_m_description)
async def add_movie_description(message:Message, state: FSMContext):
    await state.update_data(add_m_description=message.text)
    await message.answer('Введите страну фильма')
    await state.set_state(AddMovie.add_m_country)

@admin_router.message(AddMovie.add_m_country)
async def add_movie_country(message:Message, state: FSMContext):
    await state.update_data(add_m_country=message.text)
    await message.answer('Введите возрастное ограничение фильма')
    await state.set_state(AddMovie.add_m_age_limit)   

@admin_router.message(AddMovie.add_m_age_limit)
async def add_movie_age_limit(message:Message, state: FSMContext):
    await state.update_data(add_m_age_limit=int(message.text))
    await message.answer('Отправьте трейлер фильма')
    await state.set_state(AddMovie.add_m_trailer) 

@admin_router.message(AddMovie.add_m_trailer)
async def add_movie_trailer(message:Message, state: FSMContext):
    await state.update_data(add_m_trailer=message.video.file_id)
    await message.answer('Отправьте ссылку на фильм')
    await state.set_state(AddMovie.add_m_url) 

@admin_router.message(AddMovie.add_m_url)
async def add_movie_url(message: Message, state: FSMContext):
    await add_url(message.text)
    urls = await get_url()
    urs = []
    for url in urls:
        urs.append(url.id)
    url_id =  urs[-1]
    await state.update_data(add_m_url=url_id)
    data = await state.get_data()
    movie = Movies(
        title=data['add_m_title'],
        poster=data['add_m_poster'],
        release_date=data['add_m_release_date'],
        description=data['add_m_description'],
        country=data['add_m_country'],
        age_limit=data['add_m_age_limit'],
        trailer=data['add_m_trailer'],
        url_id=data['add_m_url']
    )
    await add_movies(movie)
    await message.answer(f'Название: {data.get("add_m_title")}\n'
                         f'Постер: {data.get("add_m_poster")}\n'
                         f'Год выпуска: {data.get("add_m_release_date")}\n'
                         f'Описание: {data.get("add_m_description")}\n'
                         f'Страна: {data.get("add_m_country")}\n'
                         f'Возрастное ограничение: {data.get("add_m_age_limit")}\n'
                         f'Трейлер: {data.get("add_m_trailer")}\n'
                         f'Ссылка: {message.text}\n'
                         f'Фильм добавлен',
                         )
    
    await state.clear




class AddSeries(StatesGroup):
    add_s_title = State()
    add_s_poster = State()
    add_s_release_date = State()
    add_s_description = State()
    add_s_country = State()
    add_s_age_limit = State()
    add_s_trailer = State()
    add_s_seasons = State()
    add_s_url = State()
   

async def check_admin(message: Message):
    return message.from_user.id == ADMIN_ID
   


@admin_router.message(Command('add_seria'))
async def add_seria_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer('Это команда только для Администратора')
        return
    await message.answer('Введите название фильма')
    await state.set_state(AddSeries.add_s_title)

@admin_router.message(AddSeries.add_s_title)
async def add_seria_title(message:Message, state: FSMContext):
    await state.update_data(add_s_title=message.text)
    await message.answer('Отправьте постер для фильма')
    await state.set_state(AddSeries.add_s_poster)

@admin_router.message(AddSeries.add_s_poster)
async def add_seria_poster(message:Message, state: FSMContext):
    await state.update_data(add_s_poster=message.photo[0].file_id)
    await message.answer('Отправьте постер для фильма \n Пример: Год-месяц-день')
    await state.set_state(AddSeries.add_s_release_date)

@admin_router.message(AddSeries.add_s_release_date)
async def add_seria_release_date(message:Message, state: FSMContext):
    await state.update_data(add_s_release_date=message.text)
    await message.answer('Введите описание фильма')
    await state.set_state(AddSeries.add_s_description)

@admin_router.message(AddSeries.add_s_description)
async def add_seria_description(message:Message, state: FSMContext):
    await state.update_data(add_s_description=message.text)
    await message.answer('Введите страну фильма')
    await state.set_state(AddSeries.add_s_country)

@admin_router.message(AddSeries.add_s_country)
async def add_seria_country(message:Message, state: FSMContext):
    await state.update_data(add_s_country=message.text)
    await message.answer('Введите возрастное ограничение фильма')
    await state.set_state(AddSeries.add_s_age_limit)   

@admin_router.message(AddSeries.add_s_age_limit)
async def add_seria_age_limit(message:Message, state: FSMContext):
    await state.update_data(add_s_age_limit=int(message.text))
    await message.answer('Отправьте трейлер фильма, вводите только числа')
    await state.set_state(AddSeries.add_s_trailer)


 

@admin_router.message(AddSeries.add_s_trailer)
async def add_seria_trailer(message:Message, state: FSMContext):
    await state.update_data(add_s_trailer=message.video.file_id)
    await message.answer('Какой сезон?')
    await state.set_state(AddSeries.add_s_seasons) 

@admin_router.message(AddSeries.add_s_seasons)
async def add_seria_seasons(message:Message, state: FSMContext):
    await state.update_data(add_s_seasons=message.text)
    await message.answer('Отправьте ссылку на сериала')
    await state.set_state(AddSeries.add_s_url)

@admin_router.message(AddSeries.add_s_url)
async def add_seria_url(message: Message, state: FSMContext):
    await add_url(message.text)
    urls = await get_url()
    urs = []
    for url in urls:
        urs.append(url.id)
    url_id =  urs[-1]
    await state.update_data(add_s_url=url_id)
    data = await state.get_data()
    seria = Series(
        title=data['add_s_title'],
        poster=data['add_s_poster'],
        release_date=data['add_s_release_date'],
        description=data['add_s_description'],
        country=data['add_s_country'],
        age_limit=data['add_s_age_limit'],
        seasons=data['add_s_seasons'],
        trailer=data['add_s_trailer'],
        url_id=data['add_s_url']
    )
    await add_series(seria)
    await message.answer(f'Название: {data.get("add_s_title")}\n'
                         f'Постер: {data.get("add_s_poster")}\n'
                         f'Год выпуска: {data.get("add_s_release_date")}\n'
                         f'Описание: {data.get("add_s_description")}\n'
                         f'Страна: {data.get("add_s_country")}\n'
                         f'Возрастное ограничение: {data.get("add_s_age_limit")}\n'
                         f'Трейлер: {data.get("add_s_trailer")}\n'
                         f'Сезон: {data.get("add_s_seasons")}\n'
                         f'Ссылка: {message.text}\n'
                         f'Сериал добавлен',
                         )
    
    await state.clear



class AddActor(StatesGroup):
    add_a_first_name = State()
    add_a_last_name = State()
    add_a_image = State()
    add_a_birth_day = State()
    add_a_description = State()
    
   

async def check_admin(message: Message):
    return message.from_user.id == ADMIN_ID
   


@admin_router.message(Command('add_actor'))
async def add_actor_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer('Это команда только для Администратора')
        return
    await message.answer('Введите имя актера')
    await state.set_state(AddActor.add_a_first_name)
   
@admin_router.message(AddActor.add_a_first_name)
async def add_actor_first_name(message:Message, state: FSMContext):
    await state.update_data(add_a_first_name=message.text)
    await message.answer('Введите фамилию актера')
    await state.set_state(AddActor.add_a_last_name)

@admin_router.message(AddActor.add_a_last_name)
async def add_actor_last_name(message:Message, state: FSMContext):
    await state.update_data(add_a_last_name=message.text)
    await message.answer('Отправьте фото актера')
    await state.set_state(AddActor.add_a_image)


@admin_router.message(AddActor.add_a_image)
async def add_actor_image(message:Message, state: FSMContext):
    await state.update_data(add_a_image=message.photo[0].file_id)
    await message.answer('День рождение актера')
    await state.set_state(AddActor.add_a_birth_day)

@admin_router.message(AddActor.add_a_birth_day)
async def add_actor_birth_day(message:Message, state: FSMContext):
    await state.update_data(add_a_birth_day=message.text)
    await message.answer('Опищите актера')
    await state.set_state(AddActor.add_a_description)

@admin_router.message(AddActor.add_a_description)
async def add_actor_description(message:Message, state: FSMContext):
    await state.update_data(add_a_description=message.text)
#     
    data = await state.get_data()
    actor = Actors(
        first_name=data['add_a_first_name'],
        last_name=data['add_a_last_name'],
        image=data['add_a_image'],
        description=data['add_a_description'],
        birth_day=data['add_a_birth_day']
    )
    await add_actors(actor)
    await message.answer(f'Имя: {data.get("add_a_first_name")}\n'
                         f'Фамилия: {data.get("add_a_last_name")}\n'
                         f'Фото: {data.get("add_a_image")}\n'
                         f'Описание: {data.get("add_a_description")}\n'
                         f'День рождение: {data.get("add_a_birth_day")}'
                         f'Актер добавлен',
                         )
    
    await state.clear



class AddDirector(StatesGroup):
    add_d_first_name = State()
    add_d_last_name = State()
    add_d_image = State()
    add_d_birth_day = State()
    add_d_description = State()
    
   

async def check_admin(message: Message):
    return message.from_user.id == ADMIN_ID
   


@admin_router.message(Command('add_director'))
async def add_director_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer('Это команда только для Администратора')
        return
    await message.answer('Введите имя режиссера')
    await state.set_state(AddDirector.add_d_first_name)
   
@admin_router.message(AddDirector.add_d_first_name)
async def add_director_first_name(message:Message, state: FSMContext):
    await state.update_data(add_d_first_name=message.text)
    await message.answer('Введите фамилию режиссера')
    await state.set_state(AddDirector.add_d_last_name)

@admin_router.message(AddDirector.add_d_last_name)
async def add_director_last_name(message:Message, state: FSMContext):
    await state.update_data(add_d_last_name=message.text)
    await message.answer('Отправьте фото режиссера')
    await state.set_state(AddDirector.add_d_image)


@admin_router.message(AddDirector.add_d_image)
async def add_director_image(message:Message, state: FSMContext):
    await state.update_data(add_d_image=message.photo[0].file_id)
    await message.answer('День рождение режиссера')
    await state.set_state(AddDirector.add_d_birth_day)

@admin_router.message(AddDirector.add_d_birth_day)
async def add_director_birth_day(message:Message, state: FSMContext):
    await state.update_data(add_d_birth_day=message.text)
    await message.answer('Описание режиссера')
    await state.set_state(AddDirector.add_d_description)

@admin_router.message(AddDirector.add_d_description)
async def add_director_description(message:Message, state: FSMContext):
    await state.update_data(add_d_description=message.text)
#    
    data = await state.get_data()
    director = Directors(
        first_name=data['add_d_first_name'],
        last_name=data['add_d_last_name'],
        image=data['add_d_image'],
        description=data['add_d_description'],
        birth_day=data['add_d_birth_day']
    )
    await add_directors(director)
    await message.answer(f'Имя: {data.get("add_d_first_name")}\n'
                         f'Фамилия: {data.get("add_d_last_name")}\n'
                         f'Фото: {data.get("add_d_image")}\n'
                         f'Описание: {data.get("add_d_description")}\n'
                         f'День рождение: {data.get("add_d_birth_day")}'
                         f'Актер добавлен',
                         )
    
    await state.clear


# ADDING GENRES
class AddGenre(StatesGroup):
    add_g_name = State()
    add_g_description = State()

@admin_router.message(Command("add_genre"))  
async def add_genre_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return 
    await message.answer("Введите название жанра: ") 
    await state.set_state(AddGenre.add_g_name)   
@admin_router.message(AddGenre.add_g_name)  
async def add_genre_name(message: Message, state: FSMContext):
    await state.update_data(add_g_name=message.text)  

    await message.answer("Дайте короткое описание жанра: ")
    await state.set_state(AddGenre.add_g_description)  
@admin_router.message(AddGenre.add_g_description)  
async def add_genre_description(message: Message, state: FSMContext):
    await state.update_data(add_g_description=message.text)

    data = await state.get_data()
    genre = Genre(   
        name=data['add_g_name'],
        description=data['add_g_description'])   
    
    await add_genre(genre)    
    await message.answer(f'Название жанра: {data.get("add_g_name")}\n'
                         f'Описание жанра: {data.get("add_g_description")}\n' 
                         f'Жанр добавлен')
    await state.clear()


from commands.keyboards_tg import *

class MovieToGenre(StatesGroup):
    choice_movie = State()
    choice_genre = State()



@admin_router.message(Command("mg_rel"))  
async def choice_movie_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return 
    await message.answer("Выберите фильм: ", reply_markup= await get_movies_kb_admin())
    await state.set_state(MovieToGenre.choice_movie)

@admin_router.callback_query(MovieToGenre.choice_movie)
async def choice_movie_admin(callback: CallbackQuery, state:FSMContext):
    await state.update_data(choice_movie=callback.data.split('_')[2])
    await callback.message.answer("Выберите жанр: ", reply_markup= await get_genre_kb_admin())
    await state.set_state(MovieToGenre.choice_genre)

@admin_router.callback_query(MovieToGenre.choice_genre)
async def choice_genre_admin(callback: CallbackQuery, state:FSMContext):
    await state.update_data(choice_genre=callback.data.split('_')[2])
    data = await state.get_data()
    try:
        await add_movie_genre(data['choice_movie'], data['choice_genre'])
        await callback.message.answer(f'Фильм {data['choice_movie']} добавлен в жанр{data['choice_genre']}')
   
    except Exception as e:
        await callback.message.answer(f'Этот фильм и жанр уже имеют отношение')
        
    await state.clear

class SeriaToGenre(StatesGroup):
    choice_seria = State()
    choice_genre = State()



@admin_router.message(Command("sg_rel"))  
async def choice_seria_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return 
    await message.answer("Выберите сериал: ", reply_markup= await get_series_kb_admin())
    await state.set_state(SeriaToGenre.choice_seria)

@admin_router.callback_query(SeriaToGenre.choice_seria)
async def choice_seria_admin(callback: CallbackQuery, state:FSMContext):
    await state.update_data(choice_seria=callback.data.split('_')[2])
    await callback.message.answer("Выберите жанр: ", reply_markup= await get_genre_kb_admin())
    await state.set_state(SeriaToGenre.choice_genre)

@admin_router.callback_query(SeriaToGenre.choice_genre)
async def choice_genre_admin(callback: CallbackQuery, state:FSMContext):
    await state.update_data(choice_genre=callback.data.split('_')[2])
    data = await state.get_data()
    try:
        await add_series_genre(data['choice_seria'], data['choice_genre'])
        await callback.message.answer(f'Сериал {data['choice_seria']} добавлен в жанр{data['choice_genre']}')
   
    except Exception as e:
        await callback.message.answer(f'Этот сериал и жанр уже имеют отношение')
        
    await state.clear
 

class MovieToActor(StatesGroup):
    choice_movie = State()
    choice_actor = State()



@admin_router.message(Command("mac_rel"))  
async def choice_movie_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return 
    await message.answer("Выберите фильм: ", reply_markup= await get_movies_kb_admin())
    await state.set_state( MovieToActor.choice_movie)

@admin_router.callback_query( MovieToActor.choice_movie)
async def choice_movie_admin(callback: CallbackQuery, state:FSMContext):
    await state.update_data(choice_movie=callback.data.split('_')[2])
    await callback.message.answer("Выберите актера: ", reply_markup= await get_actors_kb_admin())
    await state.set_state( MovieToActor.choice_actor)

@admin_router.callback_query( MovieToActor.choice_actor)
async def choice_actor_admin(callback: CallbackQuery, state:FSMContext):
    await state.update_data(choice_actor=callback.data.split('_')[2])
    data = await state.get_data()
    try:
        await add_movie_actors(data['choice_movie'], data['choice_actor'])
        await callback.message.answer(f'Актер {data['choice_actor']} добавлен в фильм{data['choice_movie']}')
   
    except Exception as e:
        await callback.message.answer(f'Этот фильм и актер уже имеют отношение')
        
    await state.clear


class SeriaToActor(StatesGroup):
    choice_seria = State()
    choice_actor = State()



@admin_router.message(Command("sda_rel"))  
async def choice_seria_admin(message: Message, state: FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для админа!") 
        return 
    await message.answer("Выберите сериал: ", reply_markup= await get_series_kb_admin())
    await state.set_state(SeriaToActor.choice_seria)

@admin_router.callback_query( SeriaToActor.choice_seria)
async def choice_seria_admin(callback: CallbackQuery, state:FSMContext):
    await state.update_data(choice_seria=callback.data.split('_')[2])
    await callback.message.answer("Выберите актера: ", reply_markup= await get_actors_kb_admin())
    await state.set_state( SeriaToActor.choice_actor)

@admin_router.callback_query( SeriaToActor.choice_actor)
async def choice_actor_admin(callback: CallbackQuery, state:FSMContext):
    await state.update_data(choice_actor=callback.data.split('_')[2])
    data = await state.get_data()
    try:
        await add_movie_actors(data['choice_seria'], data['choice_actor'])
        await callback.message.answer(f'Актер {data['choice_actor']} добавлен в серию{data['choice_seria']}')
   
    except Exception as e:
        await callback.message.answer(f'Этот сериал и актер уже имеют отношение')
        
    await state.clear
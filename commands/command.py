from aiogram import Router, types
from aiogram.filters import Command,CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F
import re
from commands.keyboards_tg import *


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

















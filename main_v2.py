from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

EXE_PATH = r'chromedriver/chromedriver.exe'

bot = Bot(token='2140524776:AAGTP1vU-IAR3II-A0VT7dQ3eVxwhD8h0EU')
dp = Dispatcher(bot)

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')


async def connect(mes, driver):
    res = driver.get(f"https://www.kinopoisk.ru/index.php?kp_query={mes}")
    film_name = driver.find_element(By.CLASS_NAME, 'name')
    film_rating = driver.find_element(By.CLASS_NAME, 'rating')
    return f'{film_name.text}, {film_rating.text}'


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Введи название фильма, а я скажу его рейтинг')


@dp.message_handler()
async def info(message: types.Message):
    mes = message.text
    await message.reply(await connect(mes, driver))


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=EXE_PATH, options=options)
    executor.start_polling(dp)
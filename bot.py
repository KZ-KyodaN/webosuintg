import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
# Забираем токен из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")
# Проверка, чтобы не запускать бота без токена
if not TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения!")
# Создание экземпляров
bot = Bot(token=TOKEN)
dp = Dispatcher()
# Обработка команды /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет")
# Обработка любого текстового сообщения
@dp.message()
async def echo_handler(message: Message):
    await message.answer(f"Ты сказал: {message.text}")
# Запуск бота
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from db import Database
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

TOKEN = '6709959864:AAFakIbD5Gw-EQQz22XEUHf9DckQUv799qo'

dp = Dispatcher()

db = Database("users.db")

# @dp.message(CommandStart())
# async def start(message: Message):
#     db.add_user(message.from_user.id, message.from_user.full_name)
#     await message.answer("salom")

class Form(StatesGroup):
    name = State()
    username = State()
    password = State()
    finish = State()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Assalomu alekum! {message.from_user.full_name}")

    @dp.message()
    async def reg(message: Message, state: FSMContext):
        if message.text == "Register":
            await state.set_state(Form.name)
            await message.answer("Enter name")

@dp.message(Form.name)
async def usernames(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.username)
    await message.answer("Enter username")x


@dp.message(Form.username)
async def passwords(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
    await state.set_state(Form.password)
    await message.answer("Enter password")


@dp.message(Form.password)
async def finish(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(password=message.text)
    await state.set_state(Form.finish)
    data = await state.get_data()
    await state.clear()
    await message.answer(
        "You have successfully",
    )
    name = data.get("name", "Unknown")
    username = data.get("username", "Unknown")
    password = data.get("password", "Unknown")

    matn = f"🧑‍💻 Name: {name}\n⚡️ Username: {username}\n🔐 Password: {password}"
    await message.answer(text=matn)
    db.add_user(name, username, password)
async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
import asyncio


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.add(button)
kb.add(button2)

inline_kb = InlineKeyboardMarkup()
inline_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inline_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(inline_button)
inline_kb.add(inline_button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Бот запущен ✅', reply_markup=kb)

@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Данный бот рассчитывает калории.')


@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)


@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6,25 + рост (см) - 5 x возраст (г) - 161')
    await call.answer()

@dp.callback_query_handler(text = 'calories')
async def get_age(call):
    await call.answer()
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()



@dp.message_handler(state = UserState.age)
async def fms_handler(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(bouth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    calories = (10 * data['growth'] + 6.25 * data['weight'] - 5 * data['age'] + 5)
    await message.answer(f'Калории: {calories}')
    await state.finish()



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
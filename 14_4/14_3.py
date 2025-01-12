from crud_functions import *
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher import FSMContext
import asyncio


api = "7776605837:AAHI4zwhvCzTLjWYO-SIU-QUp75vWas0VPM"
bot = Bot(token=api)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')
        ],
        [
            KeyboardButton(text='Купить')
        ]
    ],
    resize_keyboard=True
)


inline_kb = InlineKeyboardMarkup()
inline_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inline_button2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(inline_button)
inline_kb.add(inline_button2)

inline_kb_buying = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Product1', callback_data='product_buying'),
            InlineKeyboardButton(text='Product2', callback_data='product_buying'),
            InlineKeyboardButton(text='Product3', callback_data='product_buying'),
            InlineKeyboardButton(text='Product4', callback_data='product_buying'),
            InlineKeyboardButton(text='Product5', callback_data='product_buying'),
            InlineKeyboardButton(text='Product6', callback_data='product_buying'),
        ]
    ]
)


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

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for product in get_all_products():
        with open('1.jpg', 'rb') as photo:
            await message.answer_photo(photo, f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
    await message.answer('Выберите продукт для покупки', reply_markup=inline_kb_buying)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
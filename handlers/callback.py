from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_buttons import questionnaire_one_keyboard, questionnaire_two_keyboard


async def start_questionnaire(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Ты девушка или парень?",
        reply_markup=await questionnaire_one_keyboard()
    )

async def male_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Сколько тебе лет?",
        reply_markup= await questionnaire_two_keyboard()
    )
async def female_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Сколько тебе лет?",
        reply_markup= await questionnaire_two_keyboard()
    )

async def no_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Опрос завершен"
    )

async def yes_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Опрос завершен"
    )


def rigister_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire,
                                lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(male_answer,
                                lambda call: call.data == "male")
    dp.register_callback_query_handler(female_answer,
                                lambda call: call.data == "female")
    dp.register_callback_query_handler(no_answer,
                                lambda call: call.data == "finished_one")
    dp.register_callback_query_handler(yes_answer,
                                lambda call: call.data == "finished_two")

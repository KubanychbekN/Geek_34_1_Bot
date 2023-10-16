from aiogram import types, Dispatcher
from config import bot

async def chat_actions(message: types.Message):
    ban_words = ['fuck', 'bitch', 'damn']

    print(message.chat.id)
    if message.chat.id == -1001941293549:
        for word in ban_words:
            if word in message.text.lower().replace(" ", ""):
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=message.message_id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"В этом чате не допустимы такие слова!!!\n"
                         f"Username: {message.from_user.username}\n"
                         f"First-name: {message.from_user.first_name}"
                )
    else:
        await message.reply(
            text="Такой команды нет\n"
                 "Возможно вы ошиблись"
        )



def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_actions)





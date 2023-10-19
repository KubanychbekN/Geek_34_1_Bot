from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Начать опрос",
        callback_data="start_questionnaire"
    )
    registration_button = InlineKeyboardButton(
        "Регистрация",
        callback_data="fsm_start"
    )
    my_profile_button = InlineKeyboardButton(
        "Мой провиль",
        callback_data="my_profile"
    )
    markup.add(questionnaire_button)
    markup.add(registration_button)
    markup.add(my_profile_button)
    return markup

async def questionnaire_one_keyboard():
    markup = InlineKeyboardMarkup()
    male_button = InlineKeyboardButton(
        "Парень",
        callback_data="male"
    )
    female_button = InlineKeyboardButton(
        "Девушка",
        callback_data="female"
    )
    markup.add(male_button)
    markup.add(female_button)
    return markup

async def questionnaire_two_keyboard():
    markup = InlineKeyboardMarkup()
    finished_one_button = InlineKeyboardButton(
        "от 16 до 20",
        callback_data="finished_one"
    )
    finished_two_button = InlineKeyboardButton(
        "от 20 до 25",
        callback_data="finished_two"
    )
    markup.add(finished_one_button)
    markup.add(finished_two_button)
    return markup

async def admin_keyboard():
    markup = InlineKeyboardMarkup()
    admin_user_list_button = InlineKeyboardButton(
        "Список пользователей",
        callback_data="admin_user_list"
    )
    markup.add(admin_user_list_button)
    return markup


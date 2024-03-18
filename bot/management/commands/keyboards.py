from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from apps.company.models import (
    Region,
    Filial,
    Vacancy
)
from bot.models import UserProfile
from apps.main.models import (
    Language,
    LanguageLevel,
    Education
)
from apps.main.models import (
    Contact,
    Answer
)


def language_menu(lan):
    keyboard = [
            [KeyboardButton("🇺🇿 UZ"), KeyboardButton("🇷🇺 RU"), KeyboardButton("🇬🇧 EN")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return reply_markup


def home_menu(lan):
    keyboard = [
        [KeyboardButton(lan['vacancy']), KeyboardButton(lan['main_office'])],
        [KeyboardButton(lan['contact']), KeyboardButton(lan['about_company'])],
        [KeyboardButton(lan['edit_language'])]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def regions_button(callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    regions = Region.objects.filter(user_profile=user_profile_filter, parent__isnull=True).order_by('order')
    keyboard = []
    c = 0
    b = []
    region_len = len(regions)
    if user.language == 'uz':
        for region in regions:
            a = KeyboardButton(str(region.name_uz))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    elif user.language == 'ru':
        for region in regions:
            a = KeyboardButton(str(region.name_ru))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    else:
        for region in regions:
            a = KeyboardButton(str(region.name_en))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    back = [
        KeyboardButton(lan['back'])
    ]
    keyboard.append(back)
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def filials_button(callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    region = user.region
    filials = Filial.objects.filter(user_profile=user_profile_filter, region=region).order_by('order')
    keyboard = []
    c = 0
    b = []
    region_len = len(filials)
    if user.language == 'uz':
        for filial in filials:
            a = KeyboardButton(str(filial.name_uz))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    elif user.language == 'ru':
        for filial in filials:
            a = KeyboardButton(str(filial.name_ru))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    else:
        for filial in filials:
            a = KeyboardButton(str(filial.name_en))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    back = [
        KeyboardButton(lan['back'])
    ]
    keyboard.append(back)
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def vacancies_button(callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    filial = user.filial
    vacancies = Vacancy.objects.filter(user_profile=user_profile_filter, filial=filial).order_by('order')
    keyboard = []
    c = 0
    b = []
    region_len = len(vacancies)
    if user.language == 'uz':
        for vacancies in vacancies:
            a = KeyboardButton(str(vacancies.name_uz))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    elif user.language == 'ru':
        for vacancies in vacancies:
            a = KeyboardButton(str(vacancies.name_ru))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    else:
        for vacancies in vacancies:
            a = KeyboardButton(str(vacancies.name_en))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    back = [
        KeyboardButton(lan['back'])
    ]
    keyboard.append(back)
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def vacancy_detail_button(lan):
    keyboard = [
        [KeyboardButton(lan['resume_start']), KeyboardButton(lan['back'])],
        # [KeyboardButton(lan['test_start'])],

    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return reply_markup


def footer_button(lan):
    keyboard = [
        [KeyboardButton(lan['home_menu']), KeyboardButton(lan['back'])],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return reply_markup


def gender_inline(lan):
    keyboard = [
        [InlineKeyboardButton(text=lan['mail'], callback_data="mail"),
         InlineKeyboardButton(text=lan['femail'], callback_data="femail")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def language_inline(callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    languages = Language.objects.filter(user_profile=user_profile_filter).order_by('order')
    languages_level = LanguageLevel.objects.filter(user_profile=user_profile_filter).order_by('order')
    language = languages[user.language_filter]
    keyboard = []
    if language:
        user.candidate_language = language
        user.save()
        key = []
        key2 = []
        if user.language == 'uz':
            language_inline_button = InlineKeyboardButton(text=language.name_uz, callback_data=str(language.id))
        elif user.language == 'ru':
            language_inline_button = InlineKeyboardButton(text=language.name_ru, callback_data=str(language.id))
        else:
            language_inline_button = InlineKeyboardButton(text=language.name_en, callback_data=str(language.id))
        key.append(language_inline_button)
        for language_level in languages_level:
            if user.language == 'uz':
                language_level_inline_button = InlineKeyboardButton(text=language_level.name_uz,
                                                                    callback_data='a' + str(language_level.id))
            elif user.language == 'ru':
                language_level_inline_button = InlineKeyboardButton(text=language_level.name_ru,
                                                                    callback_data='a' + str(language_level.id))
            else:
                language_level_inline_button = InlineKeyboardButton(text=language_level.name_en,
                                                                    callback_data='a' + str(language_level.id))
            key2.append(language_level_inline_button)
            user.inline_type = 'language_level'
            user.save()
        keyboard.append(key)
        keyboard.append(key2)
    else:
        pass
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def education_inline(callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    educations = Education.objects.filter(user_profile=user_profile_filter).order_by('order')
    keyboard = []
    a = []
    for education in educations:
        if user.language == 'uz':
            language_inline_button = InlineKeyboardButton(text=education.name_uz, callback_data=str(education.id))
        elif user.language == 'ru':
            language_inline_button = InlineKeyboardButton(text=education.name_ru, callback_data=str(education.id))
        else:
            language_inline_button = InlineKeyboardButton(text=education.name_en, callback_data=str(education.id))
        a.append(language_inline_button)
    keyboard.append(a)
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def check_candidate_button(lan):
    keyboard = [
        [KeyboardButton(lan['resume_start_check_success']), KeyboardButton(lan['back'])],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def resume_footer(lan):
    keyboard = [
        [KeyboardButton(lan['restart_resume']), KeyboardButton(lan['finish_resume'])],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def test_start_button(lan):
    keyboard = [
        [KeyboardButton(lan['test_start'])],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return reply_markup


def main_office_vacancies_button(callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    vacancies = Vacancy.objects.filter(user_profile=user_profile_filter, main_office=True)
    keyboard = []
    c = 0
    b = []
    region_len = len(vacancies)
    if user.language == 'uz':
        for vacancies in vacancies:
            a = KeyboardButton(str(vacancies.name_uz))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    elif user.language == 'ru':
        for vacancies in vacancies:
            a = KeyboardButton(str(vacancies.name_ru))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    else:
        for vacancies in vacancies:
            a = KeyboardButton(str(vacancies.name_en))
            b.append(a)
            c += 1
            if c == 2:
                keyboard.append(b)
                b = []
                c = 0
                region_len -= 2
            elif region_len == 1:
                keyboard.append(b)
            else:
                pass
    back = [
        KeyboardButton(lan['back'])
    ]
    keyboard.append(back)
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def contact_button(callback, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    contact = Contact.objects.filter(user_profile=user_profile_filter).first()
    keyboard = []
    a = []
    b = []
    c = []
    d = []
    if contact.instagram:
        a.append(InlineKeyboardButton(lan['instagram'], url=contact.instagram))
    if contact.facebook:
        a.append(InlineKeyboardButton(lan['facebook'], url=contact.facebook))
    if contact.telegram:
        b.append(InlineKeyboardButton(lan['telegram'], url=contact.telegram))
    if contact.linkedin:
        b.append(InlineKeyboardButton(lan['linkedin'], url=contact.linkedin))
    if contact.youtube:
        c.append(InlineKeyboardButton(lan['youtube'], url=contact.youtube))
    if contact.phone_number:
        d.append(InlineKeyboardButton(str(contact.phone_number), callback_data=str(contact.phone_number)))
    if a:
        keyboard.append(a)
    if b:
        keyboard.append(b)
    if c:
        keyboard.append(c)
    if d:
        keyboard.append(d)
    reply_markup = InlineKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def answer_button(user, lan):
    question = user.question
    answers = Answer.objects.filter(question=question)
    keyboard = []
    b = []
    for answer in answers:
        if user.language == 'uz':
            a = KeyboardButton(str(answer.title_uz))
            b.append(a)
            keyboard.append(b)
            b = []
        elif user.language == 'ru':
            a = KeyboardButton(str(answer.title_ru))
            b.append(a)
            keyboard.append(b)
            b = []
        else:
            a = KeyboardButton(str(answer.title_en))
            b.append(a)
            keyboard.append(b)
            b = []
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    return reply_markup


def footer_button_finish(lan):
    keyboard = [
        [KeyboardButton(lan['home_menu'])]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    return reply_markup


def send_contact_main_phone(lan):
    reply_keyboard = [[KeyboardButton(text=lan['send_main_phone'], request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    return reply_markup


def send_contact_extr_phone(lan):
    reply_keyboard = [[KeyboardButton(text=lan['send_extra_phone'], request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    return reply_markup

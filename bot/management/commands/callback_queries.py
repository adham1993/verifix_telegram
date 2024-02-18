from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, InputMediaPhoto
from .log import autorization
from .main import (
    birthday,
    education_inline_fun,
    your_resume
)
from .keyboards import (
    footer_button
)
from apps.company.models import (
    CandidateLanguages,
    Candidate
)
from apps.main.models import (
    Language,
    LanguageLevel,
    Education
)
import datetime


@autorization
def callback_query(update, callback, user, lan):
    query = update.callback_query
    print('query', query)
    print('query data', query.data)
    if user.type == 'gender_callback':
        if query.data == 'mail':
            candidate = user.candidate
            if user.language == 'uz':
                candidate.gender = "Erkak"
            elif user.language == 'ru':
                candidate.gender = "Мужчина"
            else:
                candidate.gender = "Mail"
            candidate.save()
            birthday(update, callback, user, lan)
        elif query.data == 'femail':
            candidate = user.candidate
            if user.language == 'uz':
                candidate.gender = "Ayol"
            elif user.language == 'ru':
                candidate.gender = "Женщины"
            else:
                candidate.gender = "Femail"
            candidate.save()
            birthday(update, callback, user, lan)
    elif user.type == 'language_inline_fun':
        if query.data == 'the_end_language':
            education_inline_fun(update, callback, user, lan)
        elif query.data.startswith('a') and query.data[1:].isdigit():
            language_level_id = int(query.data[1:])
            language_level = LanguageLevel.objects.filter(id=language_level_id).first()
            candidate_language_filter = CandidateLanguages.objects.filter(
                candidate=user.candidate,
                language=user.candidate_language
            ).first()
            if not candidate_language_filter:
                pass
            else:
                candidate_language_filter.language_level = language_level
                candidate_language_filter.save()
        else:
            language_filter = Language.objects.filter(id=int(query.data)).first()
            candidate_language_filter = CandidateLanguages.objects.filter(
                candidate=user.candidate,
                language=language_filter
            )
            if candidate_language_filter:
                user.candidate_language = language_filter
                user.save()
            else:
                candidate_language_create = CandidateLanguages.objects.create(
                    candidate=user.candidate,
                    language=language_filter
                )
                candidate_language_create.save()
                user.candidate_language = language_filter
                user.save()
    elif user.type == 'education_inline_fun':
        if query.data == 'the_end_education':
            your_resume(update, callback, user, lan)
        else:
            education_filter = Education.objects.filter(id=int(query.data)).first()
            if education_filter:
                candidate = user.candidate
                candidate.education.add(education_filter)
                candidate.save()
            else:
                pass
    else:
        pass


# def birthday(update, callback, user, lan):
#     print('update message', update.message)
#     if user.language == 'ru':
#         reply_text = "Tug'ilgan kuningizni manunadagidek kiriting \n\n Namuna: 2024-02-14"
#     elif user.language == 'en':
#         reply_text = "Tug'ilgan kuningizni manunadagidek kiriting \n\n Namuna: 2024-02-14 ru"
#     else:
#         reply_text = "Tug'ilgan kuningizni manunadagidek kiriting \n\n Namuna: 2024-02-14 en"
#     reply_markup = footer_button(lan)
#     update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
#     user.type = 'birthday'
#     user.save()
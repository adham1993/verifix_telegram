from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, InputMediaPhoto
from .log import autorization
from .main import (
    birthday,
    education_inline_fun,
    language_inline_fun,
    write_question_start
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
from bot.models import (
    UserProfile
)


@autorization
def callback_query(update, callback, user, lan):
    query = update.callback_query
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
        bot_username = callback.bot.username
        user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
        languages = Language.objects.filter(user_profile=user_profile_filter)
        if query.data == 'the_end_language':
            education_inline_fun(update, callback, user, lan)
        elif query.data.startswith('a') and query.data[1:].isdigit():
            language_level_id = int(query.data[1:])
            language_level = LanguageLevel.objects.filter(id=language_level_id).first()
            candidate_language_filter = CandidateLanguages.objects.filter(
                candidate=user.candidate,
                vacancy=user.vacancy,
                language=user.candidate_language
            ).first()
            if not candidate_language_filter:
                pass
            else:
                candidate_language_filter.language_level = language_level
                candidate_language_filter.save()
        else:
            language_filter = user.candidate_language
            candidate_language_filter = CandidateLanguages.objects.filter(
                candidate=user.candidate,
                vacancy=user.vacancy,
                language=language_filter
            )
            if candidate_language_filter:
                user.candidate_language = language_filter
                user.save()
            else:
                candidate_language_create = CandidateLanguages.objects.create(
                    user_profile=user.user_profile,
                    company=user.company,
                    candidate=user.candidate,
                    vacancy=user.vacancy,
                    language=language_filter
                )
                candidate_language_create.save()
                user.candidate_language = language_filter
                user.save()
        user.language_filter += 1
        user.save()
        if user.language_filter >= len(languages):
            education_inline_fun(update, callback, user, lan)
        else:
            language_inline_fun(update, callback, user, lan)
    elif user.type == 'education_inline_fun':
        education_filter = Education.objects.filter(id=int(query.data)).first()
        if education_filter:
            candidate = user.candidate
            candidate.education.add(education_filter)
            candidate.save()
        else:
            pass
        write_question_start(update, callback, user, lan)
    else:
        pass

from .log import log_errors, autorization, setLanguage
import os
from datetime import datetime, timedelta
import re
from bot.models import (
    UserBot,
    UserProfile
)
from .commands import start
from .main import (
    regions,
    filials,
    vacancies,
    vacancy_detail,
    resume_start,
    candidate_image,
    main_phone,
    email,
    address,
    legal_address,
    wage_expectation,
    node,
    language_inline_fun,
    gender,
    finish_resume,
    main_office_vacancies,
    contact,
    about_company,
    check_candidate,
    test_start,
    write_question_start
)
from apps.company.models import (
    Region,
    Filial,
    Vacancy,
    Candidate
)
from apps.main.models import (
    Answer,
    WrittenQuestion,
    WrittenAnswer
)
from apps.company.api.views import (
    send_candidate_data_to_api,
    candidate_photo_upload
)


def is_valid_date_format(date_text):
    date_pattern = re.compile(r'^\d{2}.\d{2}.\d{4}$')
    return bool(re.match(date_pattern, date_text))


@autorization
def handler(update, callback, user, lan):
    candidate = user.candidate
    # send_candidate_data_to_api(candidate)
    # candidate_photo_upload(candidate)
    chat_id = update.message.chat_id
    text = update.message.text
    bot_username = callback.bot.username
    if text == lan['home_menu']:
        start(update, callback)
    elif text == lan['edit_language']:
        setLanguage(update, callback, user, flag=True)
    elif text == lan['vacancy']:
        regions(update, callback, user, lan)
    elif text == lan['resume_start']:
        check_candidate(update, callback, user, lan)
    elif text == lan['resume_start_check_success']:
        resume_start(update, callback, user, lan)
    elif text == lan['finish_resume']:
        finish_resume(update, callback, user, lan)
    elif text == lan['main_office']:
        main_office_vacancies(update, callback, user, lan)
    elif text == lan['contact']:
        contact(update, callback, user, lan)
    elif text == lan['about_company']:
        about_company(update, callback, user, lan)
    elif text == lan['test_start']:
        test_start(update, callback, user, lan)
    elif text == lan['write_question_start']:
        write_question_start(update, callback, user, lan)
    elif text == lan['finish_back']:
        if user.type == 'test_start':
            finish_resume(update, callback, user, lan)
        else:
            finish_resume(update, callback, user, lan)
    elif text == lan['restart_resume']:
        resume_start(update, callback, user, lan)
    elif user.type == 'region':
        if text == lan['back']:
            start(update, callback)
        else:
            if user.language == 'uz':
                region = Region.objects.filter(name_uz=text).first()
                if region:
                    user.region = region
                    user.save()
                else:
                    pass
                filials(update, callback, user, lan)
            elif user.language == 'ru':
                region = Region.objects.filter(name_ru=text).first()
                if region:
                    user.region = region
                    user.save()
                else:
                    pass
                filials(update, callback, user, lan)
            else:
                region = Region.objects.filter(name_en=text).first()
                if region:
                    user.region = region
                    user.save()
                else:
                    pass
                filials(update, callback, user, lan)
    elif user.type == 'filials':
        if text == lan['back']:
            regions(update, callback, user, lan)
        else:
            if user.language == 'uz':
                filial = Filial.objects.filter(name_uz=text).first()
                if filial:
                    user.filial = filial
                    user.save()
                else:
                    pass
                vacancies(update, callback, user, lan)
            elif user.language == 'ru':
                filial = Filial.objects.filter(name_ru=text).first()
                if filial:
                    user.filial = filial
                    user.save()
                else:
                    pass
                vacancies(update, callback, user, lan)
            else:
                filial = Filial.objects.filter(name_en=text).first()
                if filial:
                    user.filial = filial
                    user.save()
                else:
                    pass
                vacancies(update, callback, user, lan)
    elif user.type == 'vacancies':
        if text == lan['back']:
            filials(update, callback, user, lan)
        else:
            if user.language == 'uz':
                vacancy = Vacancy.objects.filter(name_uz=text).first()
                if vacancy:
                    user.vacancy = vacancy
                    user.save()
                else:
                    pass
                vacancy_detail(update, callback, user, lan)
            elif user.language == 'ru':
                vacancy = Vacancy.objects.filter(name_ru=text).first()
                if vacancy:
                    user.vacancy = vacancy
                    user.save()
                else:
                    pass
                vacancy_detail(update, callback, user, lan)
            else:
                vacancy = Vacancy.objects.filter(name_en=text).first()
                if vacancy:
                    user.vacancy = vacancy
                    user.save()
                else:
                    pass
                vacancy_detail(update, callback, user, lan)
    elif user.type == 'vacancy_detail':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            pass
    elif user.type == 'check_candidate':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            pass
    elif user.type == 'check_candidate_main':
        if text == lan['back']:
            main_office_vacancies(update, callback, user, lan)
        else:
            pass
    elif user.type == 'resume_start':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            user_profile = UserProfile.objects.filter(bot_username=bot_username).first()
            candidate_filter = Candidate.objects.filter(user_profile=user_profile, vacancy=user.vacancy,
                                                        company=user.company, bot_user=user).first()
            if not candidate_filter:
                candidate = Candidate.objects.create(
                    user_profile=user_profile,
                    bot_user=user,
                    company=user.company,
                    region=user.region,
                    filial=user.filial,
                    vacancy=user.vacancy,
                    full_name=text,
                    chat_id=user.chat_id
                )
                candidate.save()
                user.candidate = candidate
                user.save()
            else:
                candidate_filter.full_name = text
                candidate_filter.save()
                user.candidate = candidate_filter
                user.save()
            print(candidate.full_name)
            print(candidate.extra_phone)
            gender(update, callback, user, lan)
    elif user.type == 'last_name':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            candidate = user.candidate
            candidate.last_name = text
            candidate.save()
    elif user.type == 'full_name':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            candidate = user.candidate
            candidate.middle_name = text
            candidate.save()
            gender(update, callback, user, lan)
    elif user.type == 'birthday':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            if is_valid_date_format(text):
                candidate = user.candidate
                candidate.birthday = text
                candidate.save()
                candidate_image(update, callback, user, lan)
            else:
                if user.language == 'uz':
                    error_message = lan['date_format_error_text']
                    update.message.reply_text(error_message)
                elif user.language == 'ru':
                    error_message = lan['date_format_error_text']
                    update.message.reply_text(error_message)
                else:
                    error_message = lan['date_format_error_text']
                    update.message.reply_text(error_message)
    elif user.type == 'candidate_image':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            if text:
                main_phone(update, callback)
            else:
                image(update, callback, user, lan)
    elif user.type == 'extra_phone':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            if text:
                candidate = user.candidate
                candidate.main_phone = text
                candidate.save()
            else:
                phone = update.message.contact.phone_number
                candidate = user.candidate
                candidate.main_phone = phone
                candidate.save()
            main_phone(update, callback)
    elif user.type == 'extra_phone2':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            if text:
                candidate = user.candidate
                candidate.extra_phone = text
                candidate.save()
            else:
                phone = update.message.contact.phone_number
                candidate = user.candidate
                candidate.extra_phone = phone
                candidate.save()
            email(update, callback, user, lan)
    elif user.type == 'email':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            candidate = user.candidate
            candidate.email = text
            candidate.save()
            address(update, callback, user, lan)
    elif user.type == 'address':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            candidate = user.candidate
            candidate.address = text
            candidate.save()
            legal_address(update, callback, user, lan)
    elif user.type == 'legal_address':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            candidate = user.candidate
            candidate.legal_address = text
            candidate.save()
            wage_expectation(update, callback, user, lan)
    elif user.type == 'wage_expectation':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            candidate = user.candidate
            candidate.wage_expectation = text
            candidate.save()
            node(update, callback, user, lan)
    elif user.type == 'node':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            candidate = user.candidate
            candidate.note = text
            candidate.save()
            language_inline_fun(update, callback, user, lan)
    elif user.type == 'language_inline_fun':
        if text == lan['back']:
            vacancies(update, callback, user, lan)
        else:
            candidate = user.candidate
            language_inline_fun(update, callback, user, lan)
    elif user.type == 'main_vacancies':
        if text == lan['back']:
            start(update, callback)
        else:
            if user.language == 'uz':
                vacancy = Vacancy.objects.filter(name_uz=text).first()
                if vacancy:
                    user.vacancy = vacancy
                    user.save()
                else:
                    pass
                vacancy_detail(update, callback, user, lan)
            elif user.language == 'ru':
                vacancy = Vacancy.objects.filter(name_ru=text).first()
                if vacancy:
                    user.vacancy = vacancy
                    user.save()
                else:
                    pass
                vacancy_detail(update, callback, user, lan)
            else:
                vacancy = Vacancy.objects.filter(name_en=text).first()
                if vacancy:
                    user.vacancy = vacancy
                    user.save()
                else:
                    pass
                vacancy_detail(update, callback, user, lan)
    elif user.type == 'vacancy_detail_detail':
        if text == lan['back']:
            main_office_vacancies(update, callback, user, lan)
        else:
            pass
    elif user.type == 'question':
        if text == lan['back']:
            start(update, callback)
        else:
            if user.language == 'uz':
                answer = Answer.objects.filter(title_uz=text).first()
                if answer:
                    if answer.current_answer:
                        user.true_count += 1
                    user.answer = answer
                    user.save()
                else:
                    pass
                test_start(update, callback, user, lan)
            elif user.language == 'ru':
                answer = Answer.objects.filter(title_ru=text).first()
                if answer:
                    if answer.current_answer:
                        user.true_count += 1
                    user.answer = answer
                    user.save()
                else:
                    pass
                test_start(update, callback, user, lan)
            else:
                answer = Answer.objects.filter(title_en=text).first()
                if answer:
                    user.answer = answer
                    user.save()
                else:
                    pass
                test_start(update, callback, user, lan)
    elif user.type == 'write_question_not':
        if text == lan['back']:
            finish_resume(update, callback, user, lan)
        else:
            pass
    elif user.type == 'write_question':
        bot_username = callback.bot.username
        user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
        questions = WrittenQuestion.objects.filter(user_profile=user_profile_filter).order_by('order')
        write_question = questions[user.write_number]
        if write_question:
            if user.language == 'uz':
                write_answer_filter = WrittenAnswer.objects.filter(candidate=user.candidate,
                                                                   write_question=write_question,
                                                                   user_profile=user_profile_filter)
                if write_answer_filter:
                    write_answer = WrittenAnswer.objects.filter(candidate=user.candidate, write_question=write_question,
                                                                user_profile=user_profile_filter).first()
                    write_answer.title = text
                    write_answer.save()
                else:
                    write_answer_create = WrittenAnswer.objects.create(
                        user_profile=user_profile_filter,
                        candidate=user.candidate,
                        write_question=write_question,
                        title=text
                    )
                    write_answer_create.save()
            elif user.language == 'ru':
                write_answer_filter = WrittenAnswer.objects.filter(candidate=user.candidate,
                                                                   write_question=write_question,
                                                                   user_profile=user_profile_filter)
                if write_answer_filter:
                    write_answer = WrittenAnswer.objects.filter(candidate=user.candidate, write_question=write_question,
                                                                user_profile=user_profile_filter).first()
                    write_answer.title = text
                    write_answer.save()
                else:
                    write_answer_create = WrittenAnswer.objects.create(
                        user_profile=user_profile_filter,
                        candidate=user.candidate,
                        write_question=write_question,
                        title=text
                    )
                    write_answer_create.save()
            else:
                write_answer_filter = WrittenAnswer.objects.filter(candidate=user.candidate,
                                                                   write_question=write_question,
                                                                   user_profile=user_profile_filter)
                if write_answer_filter:
                    write_answer = WrittenAnswer.objects.filter(candidate=user.candidate, write_question=write_question,
                                                                user_profile=user_profile_filter).first()
                    write_answer.title = text
                    write_answer.save()
                else:
                    write_answer_create = WrittenAnswer.objects.create(
                        user_profile=user_profile_filter,
                        candidate=user.candidate,
                        write_question=write_question,
                        title=text
                    )
                    write_answer_create.save()
            user.write_number += 1
            user.save()
            write_question_start(update, callback, user, lan)
        else:
            pass
    elif user.type == 'write_answer':
        if text == lan['back']:
            finish_resume(update, callback, user, lan)
        else:
            pass


@autorization
def image(update, callback, user, lan):
    text = update.message.text
    bot_username = callback.bot.username
    candidate = user.candidate
    file = callback.bot.get_file(update.message.photo[-1].file_id)
    directory = 'static/candidate/images/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    candidate.image = file.download(
        'static/candidate/images/' + str(candidate.first_name) + str(candidate.last_name) + '.jpg')
    candidate.save()
    user.type = 'main_phone'
    user.save()
    main_phone(update, callback)


@log_errors
def set_language(update, callback):
    bot_username = callback.bot.username
    chat_id = update.message.chat_id
    message_id = update.message.message_id
    text = update.message.text
    text = text.split(' ')[1]
    user = UserBot.objects.get(chat_id=chat_id, bot_username=bot_username)
    languages = (('uz', 'UZ'), ('ru', 'RU'), ('en', 'EN'))
    lan = 'uz'
    for key, value in enumerate(languages):
        (lowercase, uppercase) = value
        if uppercase == text:
            lan = lowercase
    if user:
        user.language = lan
        user.save()
        user.type = 'set_lang'
        user.save()
        start(update, callback)


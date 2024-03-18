from .log import autorization
from apps.content.models import (
    FilialMessage,
    RegionMessage,
    VacancyMessage,
    MainOfficeVacancyMessage,
    ContactMessage,
    WriteQuestionMessage
)
from bot.models import UserProfile
from .keyboards import (
    regions_button,
    filials_button,
    vacancies_button,
    vacancy_detail_button,
    footer_button,
    gender_inline,
    language_inline,
    education_inline,
    resume_footer,
    finish_resume_button,
    main_office_vacancies_button,
    contact_button,
    home_menu,
    check_candidate_button,
    answer_button,
    footer_button_finish,
    write_question_button,
    footer_back_button,
    send_contact_main_phone,
    send_contact_extr_phone
)
from apps.company.models import (
    CandidateLanguages,
    Candidate,
    ResumeFilter
)
from apps.main.models import (
    Education,
    Contact,
    Question,
    Answer,
    AboutCompany,
    SuccessCandidate,
    FailedCandidate,
    WrittenQuestion,
    WrittenAnswer
)
from apps.company.api.views import send_candidate_data_to_api


def regions(update, callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    filial_message = RegionMessage.objects.filter(user_profile=user_profile_filter).first()
    if user.language == 'uz':
        reply_text = filial_message.title_uz + '\n\n'
    elif user.language == 'en':
        if filial_message.title_en:
            reply_text = filial_message.title_en + '\n\n'
        else:
            reply_text = filial_message.title_uz + '\n\n'
    else:
        if filial_message.title_ru:
            reply_text = filial_message.title_ru + '\n\n'
        else:
            reply_text = filial_message.title_uz + '\n\n'
    image = '{}'.format(filial_message.image)
    reply_markup = regions_button(callback, user, lan)
    if filial_message.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption='', reply_markup=None, parse_mode=None)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')

    user.type = 'region'
    user.save()


def filials(update, callback, user, lan):
    # bot_username = callback.bot.username
    # user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    # filial_message = FilialMessage.objects.filter(user_profile=user_profile_filter).first()
    region = user.region
    if user.language == 'uz':
        reply_text = region.title_uz + '\n\n'
    elif user.language == 'en':
        if region.title_en:
            reply_text = region.title_en + '\n\n'
        else:
            reply_text = region.title_uz + '\n\n'
    else:
        if region.title_ru:
            reply_text = region.title_ru + '\n\n'
        else:
            reply_text = region.title_uz + '\n\n'
    image = '{}'.format(region.image)
    reply_markup = filials_button(callback, user, lan)
    if region.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
        # update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')

    user.type = 'filials'
    user.save()


def vacancies(update, callback, user, lan):
    # bot_username = callback.bot.username
    # user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    # vacancy_message = VacancyMessage.objects.filter(user_profile=user_profile_filter).first()
    filial = user.filial
    if user.language == 'uz':
        reply_text = filial.title_uz + '\n\n'
    elif user.language == 'en':
        if filial.title_en:
            reply_text = filial.title_en + '\n\n'
        else:
            reply_text = filial.title_uz + '\n\n'
    else:
        if filial.title_ru:
            reply_text = filial.title_ru + '\n\n'
        else:
            reply_text = filial.title_uz + '\n\n'
    image = '{}'.format(filial.image)
    reply_markup = vacancies_button(callback, user, lan)
    if filial.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
        # update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')

    user.type = 'vacancies'
    user.save()


def vacancy_detail(update, callback, user, lan):
    vacancy = user.vacancy
    if user.language == 'uz':
        reply_text = vacancy.description_uz + '\n\n'
    elif user.language == 'ru':
        if vacancy.description_ru:
            reply_text = vacancy.description_ru + '\n\n'
        else:
            reply_text = vacancy.description_uz + '\n\n'
    else:
        if vacancy.description_en:
            reply_text = vacancy.description_en + '\n\n'
        else:
            reply_text = vacancy.description_uz + '\n\n'
    # if user.language == 'uz':
    #     vacancy = user.vacancy
    #     reply_text = ('Vakasiya Malumotlari🧾:' + '\n\n' + 'Vakansiya nomi: ' + vacancy.name_uz + '\n' +
    #             'Lavozim: ' + vacancy.job_name_uz + '\n' + 'Ish vaqti: ' + vacancy.schedule_uz + '\n' +
    #             'Oylig maosh: ' + vacancy.wage_limit_uz + '\n' + "Bilish kerak bo'lgan tillar: " + vacancy.lang_uz +
    #             '\n\n' + "Bu shartlar sizga maqul bo'lsa. O'z malumotlaringizni qoldirishingiz mumkin.✏️")
    # elif user.language == 'ru':
    #     vacancy = user.vacancy
    #     reply_text = ('Информация О Вакансии🧾:' + '\n\n' + 'Название вакансии: ' + vacancy.name_uz + '\n' +
    #             'Позиция: ' + vacancy.job_name_uz + '\n0' + 'Рабочее время: ' + vacancy.schedule_uz + '\n' +
    #             'Ежемесячная зарплата: ' + vacancy.wage_limit_uz + '\n' + "Языки, которые нужно знать: " + vacancy.lang_uz +
    #             '\n\n' + "Это условия, если у вас есть маки. Вы можете оставить свои данные.✏️")
    # else:
    #     vacancy = user.vacancy
    #     reply_text = ('Vacancy data🧾:' + '\n\n' + 'Vacancy name: ' + vacancy.name_uz + '\n' +
    #             'Position: ' + vacancy.job_name_uz + '\n' + 'Work time: ' + vacancy.schedule_uz + '\n' +
    #             'Salary: ' + vacancy.wage_limit_uz + '\n' + "Languages to know: " + vacancy.lang_uz +
    #             '\n\n' + "If these conditions are applicable to you. You can leave your data.✏️")
    image = '{}'.format(vacancy.image)
    reply_markup = vacancy_detail_button(lan)
    if vacancy.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption='', reply_markup=reply_markup,
                                   parse_mode='HTML')
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')

    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    if user.vacancy.main_office:
        user.type = 'vacancy_detail_detail'
        user.save()
    else:
        user.type = 'vacancy_detail'
        user.save()


def check_candidate(update, callback, user, lan):
    bot_username = callback.bot.username
    user_profile = UserProfile.objects.filter(bot_username=bot_username).first()
    candidate_filter = Candidate.objects.filter(user_profile=user_profile, vacancy=user.vacancy).first()
    if candidate_filter:
        if user.language == 'uz':
            reply_text = lan['already_resume']
        elif user.language == 'ru':
            reply_text = lan['already_resume']
        else:
            reply_text = lan['already_resume']
    else:
        if user.language == 'uz':
            reply_text = lan['not_blank']
        elif user.language == 'ru':
            reply_text = lan['not_blank']
        else:
            reply_text = lan['not_blank']
    reply_markup = check_candidate_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    if user.vacancy.main_office:
        user.type = 'check_candidate_main'
        user.save()
    else:
        user.type = 'check_candidate'
        user.save()


def resume_start(update, callback, user, lan):
    user.language_filter = 1
    user.save()
    bot_username = callback.bot.username
    user_profile = UserProfile.objects.filter(bot_username=bot_username).first()
    resume_filter = user.resume_filter
    if not resume_filter:
        resume_filter = ResumeFilter.objects.filter(user_profile=user_profile, company=user.company).first()
        user.resume_filter = resume_filter
        user.save()
    else:
        pass
    if not resume_filter.full_name:
        gender(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = lan['send_full_name']
        elif user.language == 'ru':
            reply_text = lan['send_full_name']
        else:
            reply_text = lan['send_full_name']
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'resume_start'
        user.save()


def last_name(update, callback, user, lan):
    resume_filter = user.resume_filter
    if not resume_filter.last_name:
        middle_name(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Familyangizni kiriting✍️"
        elif user.language == 'ru':
            reply_text = "Введите свою фамилию✍️"
        else:
            reply_text = "Enter your last name✍️"
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'last_name'
        user.save()


def middle_name(update, callback, user, lan):
    resume_filter = user.resume_filter
    if not resume_filter.middle_name:
        gender(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Sharifingizni kiriting👇"
        elif user.language == 'ru':
            reply_text = "Введите свое второе имя👇"
        else:
            reply_text = "Enter your middle name👇"
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'middle_name'
        user.save()


def gender(update, callback, user, lan):
    resume_filter = user.resume_filter
    if not resume_filter.gender:
        birthday(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = lan['send_gender']
        elif user.language == 'ru':
            reply_text = lan['send_gender']
        else:
            reply_text = lan['send_gender']
        reply_markup = gender_inline(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'gender_callback'
        user.save()


def birthday(update, callback, user, lan):
    resume_filter = user.resume_filter
    if not resume_filter.birthday:
        candidate_image(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = lan['send_birthday']
        elif user.language == 'ru':
            reply_text = lan['send_birthday']
        else:
            reply_text = lan['send_birthday']
        reply_markup = footer_button(lan)
        if update.callback_query:
            update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        else:
            update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'birthday'
        user.save()


def candidate_image(update, callback, user, lan):
    resume_filter = user.resume_filter
    if not resume_filter.image:
        main_phone(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = lan['send_photo']
        elif user.language == 'ru':
            reply_text = lan['send_photo']
        else:
            reply_text = lan['send_photo']
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'candidate_image'
        user.save()


@autorization
def main_phone(update, callback, user, lan):
    text = update.message.text
    if user.type == 'main_phone':
        resume_filter = user.resume_filter
        if not resume_filter.main_phone:
            email(update, callback, user, lan)
        else:
            if user.language == 'uz':
                reply_text = lan['send_main_phone_text']
            elif user.language == 'ru':
                reply_text = lan['send_main_phone_text']
            else:
                reply_text = lan['send_main_phone_text']
            reply_markup = send_contact_main_phone(lan)
            update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
            user.type = 'extra_phone'
            user.save()
    elif user.type == 'extra_phone':
        resume_filter = user.resume_filter
        if not resume_filter.extra_phone:
            email(update, callback, user, lan)
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
            if user.language == 'uz':
                reply_text = lan['send_extra_phone_text']
            elif user.language == 'ru':
                reply_text = lan['send_extra_phone_text']
            else:
                reply_text = lan['send_extra_phone_text']
            reply_markup = send_contact_extr_phone(lan)
            update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
            user.type = 'extra_phone2'
            user.save()
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


# @autorization
# def extra_phone(update, callback, user, lan):
#     resume_filter = user.resume_filter
#     if not resume_filter.extra_phone:
#         email(update, callback, user, lan)
#     else:
#         if user.language == 'uz':
#             reply_text = "Qo'shimcha telefon raqamingizni yuboring.📱"
#         elif user.language == 'ru':
#             reply_text = "Отправьте свой дополнительный номер телефона.📱"
#         else:
#             reply_text = "Send your additional phone number.📱"
#         reply_markup = send_contact_extr_phone(lan)
#         update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
#         user.type = 'extra_phone'
#         user.save()


def email(update, callback, user, lan):
    resume_filter = user.resume_filter
    if not resume_filter.email:
        address(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = lan['send_email']
        elif user.language == 'ru':
            reply_text = lan['send_email']
        else:
            reply_text = lan['send_email']
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'email'
        user.save()


def address(update, callback, user, lan):
    resume_filter = user.resume_filter
    if not resume_filter.address:
        legal_address(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = lan['send_address']
        elif user.language == 'ru':
            reply_text = lan['send_address']
        else:
            reply_text = lan['send_address']
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'address'
        user.save()


def legal_address(update, callback, user, lan):
    resume_filter = user.resume_filter
    if not resume_filter.legal_address:
        wage_expectation(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = lan['send_legal_address']
        elif user.language == 'ru':
            reply_text = lan['send_legal_address']
        else:
            reply_text = lan['send_legal_address']
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'legal_address'
        user.save()


def wage_expectation(update, callback, user, lan):
    resume_filter = user.resume_filter
    if not resume_filter.wage_expectation:
        node(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "send_wage_expectation"
        elif user.language == 'ru':
            reply_text = "send_wage_expectation"
        else:
            reply_text = "send_wage_expectation"
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'wage_expectation'
        user.save()


def node(update, callback, user, lan):
    resume_filter = user.resume_filter
    if not resume_filter.note:
        language_inline_fun(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = lan['send_note']
        elif user.language == 'ru':
            reply_text = lan['send_note']
        else:
            reply_text = lan['send_note']
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'node'
    user.save()


def language_inline_fun(update, callback, user, lan):
    resume_filter = user.resume_filter
    if not resume_filter.language:
        education_inline_fun(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = lan['send_language']
        elif user.language == 'ru':
            reply_text = lan['send_language']
        else:
            reply_text = lan['send_language']
        reply_markup = language_inline(callback, user, lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'language_inline_fun'
        user.save()


def education_inline_fun(update, callback, user, lan):
    resume_filter = user.resume_filter
    if not resume_filter.education:
        your_resume(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = lan['send_education']
        elif user.language == 'ru':
            reply_text = lan['send_education']
        else:
            reply_text = lan['send_education']
        reply_markup = education_inline(callback, user, lan)
        if update.callback_query:
            if resume_filter.language:
                update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
            else:
                update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        else:
            if resume_filter.language:
                update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
            else:
                update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'education_inline_fun'
        user.save()


def your_resume(update, callback, user, lan):
    candidate = user.candidate
    candidate_languages = CandidateLanguages.objects.filter(candidate=candidate)
    languages_text = ''
    for candidate_language in candidate_languages:
        if user.language == 'uz':
            candidate_language1 = candidate_language.language.name_uz
            candidate_language_level1 = candidate_language.language_level.name_uz
        elif user.language == 'ru':
            candidate_language1 = candidate_language.language.name_ru
            candidate_language_level1 = candidate_language.language_level.name_ru
        else:
            candidate_language1 = candidate_language.language.name_en
            candidate_language_level1 = candidate_language.language_level.name_en
        languages_text += '\n' + candidate_language1 + ' ' + candidate_language_level1
    if user.language == 'uz':
        reply_text = ('Sizning Malumotlaringiz👇👇' + '\n\n' +
                      'Ismingiz: ' + (candidate.first_name or 'N/A') + '\n' +
                      'Familyangiz: ' + (candidate.last_name or 'N/A') + '\n0' +
                      'Sharifingiz: ' + (candidate.middle_name or 'N/A') + '\n' +
                      'Jinsingiz: ' + (candidate.gender or 'N/A') + '\n' +
                      "Tug'ilgan kuningiz: " + (str(candidate.birthday) or 'N/A') + '\n' +
                      "Telefon 1: " + (candidate.main_phone or 'N/A') + '\n' +
                      'Telefon 2: ' + (candidate.extra_phone or 'N/A') + '\n' +
                      'Email: ' + (candidate.email or 'N/A') + '\n' +
                      'Adres: ' + (candidate.address or 'N/A') + '\n' +
                      'Qonuniy adres: ' + (candidate.legal_address or 'N/A') + '\n' +
                      'Oylig maosh: ' + (candidate.wage_expectation or 'N/A') + '\n' +
                      'Tavsif: ' + (candidate.note or 'N/A') + '\n' +
                      'Tillar: ' + languages_text)
    elif user.language == 'ru':
        reply_text = ('Ваши Данные👇👇' + '\n\n' +
                      'Ваше имя: ' + (candidate.first_name or 'N/A') + '\n' +
                      'Твоя фамилия: ' + (candidate.last_name or 'N/A') + '\n0' +
                      'Ваш шериф: ' + (candidate.middle_name or 'N/A') + '\n' +
                      'Ваш пол: ' + (candidate.gender or 'N/A') + '\n' +
                      "Твой день рождения: " + (str(candidate.birthday) or 'N/A') + '\n' +
                      "Телефон 1: " + (candidate.main_phone or 'N/A') + '\n' +
                      'Телефон 2: ' + (candidate.extra_phone or 'N/A') + '\n' +
                      'Электронная почта: ' + (candidate.email or 'N/A') + '\n' +
                      'Адрес: ' + (candidate.address or 'N/A') + '\n' +
                      'Юридический адрес: ' + (candidate.legal_address or 'N/A') + '\n' +
                      'Зарплата: ' + (candidate.wage_expectation or 'N/A') + '\n' +
                      'Описание: ' + (candidate.note or 'N/A') + '\n' +
                      'Языки: ' + languages_text)
    else:
        reply_text = ('Your Data👇👇' + '\n\n' +
                      'First name: ' + (candidate.first_name or 'N/A') + '\n' +
                      'Last name: ' + (candidate.last_name or 'N/A') + '\n0' +
                      'Middle name: ' + (candidate.middle_name or 'N/A') + '\n' +
                      'Gender: ' + (candidate.gender or 'N/A') + '\n' +
                      "Your birthday: " + (str(candidate.birthday) or 'N/A') + '\n' +
                      "Phone 1: " + (candidate.main_phone or 'N/A') + '\n' +
                      'Phone 2: ' + (candidate.extra_phone or 'N/A') + '\n' +
                      'Email: ' + (candidate.email or 'N/A') + '\n' +
                      'Adress: ' + (candidate.address or 'N/A') + '\n' +
                      'Legal address: ' + (candidate.legal_address or 'N/A') + '\n' +
                      'Salary: ' + (candidate.wage_expectation or 'N/A') + '\n' +
                      'Node: ' + (candidate.note or 'N/A') + '\n' +
                      'Languages: ' + languages_text)

    reply_markup = resume_footer(lan)
    image = '{}'.format(candidate.image)
    if update.callback_query:
        if candidate.image:
            update.callback_query.message.reply_photo(photo=open(image, 'rb'), caption='', reply_markup=reply_markup,
                                                      parse_mode='HTML')
            update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        else:
            update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    else:
        print('aaa')
        if candidate.image:
            update.message.reply_photo(photo=open(image, 'rb'), caption='', reply_markup=reply_markup,
                                                      parse_mode='HTML')
            update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        else:
            update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'your_resume'
    user.save()


def finish_resume(update, callback, user, lan):
    candidate = user.candidate
    send_candidate_data_to_api(candidate)
    if user.language == 'uz':
        reply_text = lan['send_finish_resume']
    elif user.language == 'ru':
        reply_text = lan['send_finish_resume']
    else:
        reply_text = lan['send_finish_resume']
    candidate_languages = CandidateLanguages.objects.filter(candidate=candidate)
    text = ''
    for candidate_language in candidate_languages:
        text += (candidate_language.language.name_uz + ' (' + candidate_language.language_level.name_uz + ').' + '\n')
    candidate.language_data = text
    education_list = candidate.education.all()
    text1 = ''
    for education in education_list:
        text1 += education.name_uz + 'n'
    candidate.education_data = text1
    user.q_number = 0
    user.true_count = 0
    user.write_number = 0
    user.save()
    candidate.save()
    reply_markup = finish_resume_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'finish_resume'
    user.save()


def main_office_vacancies(update, callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    vacancy_message = MainOfficeVacancyMessage.objects.filter(user_profile=user_profile_filter).first()
    if user.language == 'uz':
        reply_text = vacancy_message.title_uz + '\n\n'
    elif user.language == 'en':
        if vacancy_message.title_en:
            reply_text = vacancy_message.title_en + '\n\n'
        else:
            reply_text = vacancy_message.title_uz + '\n\n'
    else:
        if vacancy_message.title_ru:
            reply_text = vacancy_message.title_ru + '\n\n'
        else:
            reply_text = vacancy_message.title_uz + '\n\n'
    image = '{}'.format(vacancy_message.image)
    reply_markup = main_office_vacancies_button(callback, user, lan)
    if vacancy_message.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption='', reply_markup=None, parse_mode=None)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')

    user.type = 'main_vacancies'
    user.save()


def contact(update, callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    contact_message = ContactMessage.objects.filter(user_profile=user_profile_filter).first()
    if user.language == 'uz':
        reply_text = contact_message.title_uz + '\n\n'
    elif user.language == 'ru':
        reply_text = contact_message.title_ru + '\n\n'
    else:
        reply_text = contact_message.title_en + '\n\n'
    reply_markup = contact_button(callback, lan)
    image = '{}'.format(contact_message.image)
    if contact_message.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption='', parse_mode='HTML')
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'home_menu'
    user.save()


def about_company(update, callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    content = AboutCompany.objects.filter(user_profile=user_profile_filter).first()
    if user.language == 'uz':
        reply_text = content.title_uz + '\n\n' + str(content.link)
    elif user.language == 'ru':
        reply_text = content.title_ru + '\n\n' + str(content.link)
    else:
        reply_text = content.title_en + '\n\n' + str(content.link)
    image = '{}'.format(content.image)
    video = '{}'.format(content.video)
    reply_markup = home_menu(lan)
    if content.image and content.video:
        update.message.reply_video(video=open(video, 'rb'))
        update.message.reply_photo(photo=open(image, 'rb'), caption='', reply_markup=None, parse_mode=None)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    elif content.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption='', reply_markup=None, parse_mode=None)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    elif content.video:
        update.message.reply_video(video=open(video, 'rb'), caption='', reply_markup=reply_markup,
                                   parse_mode='HTML')
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'home_menu'
    user.save()


def test_start(update, callback, user, lan):
    vacancy = user.vacancy
    questions = Question.objects.filter(vacancy=vacancy)
    if questions:
        if user.q_number == len(questions):
            user.q_number = 0
            user.save()
            answer_fun(update, callback, user, lan)
        else:
            for question in range(user.q_number, len(questions)):
                if user.language == 'uz':
                    user.question = questions[user.q_number]
                    user.save()
                    reply_text = str(user.q_number + 1) + '. ' + questions[user.q_number].title_uz
                    reply_markup = answer_button(user, lan)
                    update.message.reply_text(text=reply_text, reply_markup=reply_markup)
                    user.q_number += 1
                    user.save()
                    break
                elif user.language == 'ru':
                    user.question = questions[user.q_number]
                    user.save()
                    reply_text = str(user.q_number + 1) + '. ' + questions[user.q_number].title_ru
                    reply_markup = answer_button(user, lan)
                    update.message.reply_text(text=reply_text, reply_markup=reply_markup)
                    user.question = questions[user.q_number]
                    user.q_number += 1
                    user.save()
                    break
                else:
                    user.question = questions[user.q_number]
                    user.save()
                    reply_text = str(user.q_number + 1) + '. ' + questions[user.q_number].title_en
                    reply_markup = answer_button(user, lan)
                    update.message.reply_text(text=reply_text, reply_markup=reply_markup)
                    break
        user.type = 'question'
        user.save()
    else:
        if user.language == 'uz':
            reply_text = lan['test_not_found']
        elif user.language == 'ru':
            reply_text = lan['test_not_found']
        else:
            reply_text = lan['test_not_found']
        reply_markup = footer_back_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'test_start'
        user.true_count = 0
        user.save()


def answer_fun(update, callback, user, lan):
    vacancy = user.vacancy
    candidate = user.candidate
    questions = Question.objects.filter(vacancy=vacancy)
    question_count = len(questions)
    check_result = question_count - user.true_count
    if check_result >= 2:
        failed_candidate_create = FailedCandidate.objects.create(
            user_profile=candidate.user_profile,
            bot_user=candidate.bot_user,
            company=candidate.company,
            region=candidate.region,
            filial=candidate.filial,
            vacancy=candidate.vacancy,
            first_name=candidate.first_name,
            last_name=candidate.last_name,
            middle_name=candidate.middle_name,
            gender=candidate.gender,
            birthday=candidate.birthday,
            image=candidate.image,
            main_phone=candidate.main_phone,
            extra_phone=candidate.extra_phone,
            email=candidate.email,
            address=candidate.address,
            legal_address=candidate.legal_address,
            wage_expectation=candidate.wage_expectation,
            note=candidate.note,
            language_data=candidate.language_data,
            education_data=candidate.education_data
        )
        failed_candidate_create.save()
    else:
        success_candidate_create = SuccessCandidate.objects.create(
            user_profile=candidate.user_profile,
            bot_user=candidate.bot_user,
            company=candidate.company,
            region=candidate.region,
            filial=candidate.filial,
            vacancy=candidate.vacancy,
            first_name=candidate.first_name,
            last_name=candidate.last_name,
            middle_name=candidate.middle_name,
            gender=candidate.gender,
            birthday=candidate.birthday,
            image=candidate.image,
            main_phone=candidate.main_phone,
            extra_phone=candidate.extra_phone,
            email=candidate.email,
            address=candidate.address,
            legal_address=candidate.legal_address,
            wage_expectation=candidate.wage_expectation,
            note=candidate.note,
            language_data=candidate.language_data,
            education_data=candidate.education_data
        )
        success_candidate_create.save()
    if user.language == 'uz':
        reply_text = ('Sizning javoblaringiz qabul qilindi.' + '\n' + "Siz " + str(question_count) + ' testdan ' +
                      str(user.true_count) + ' ta bajardingiz.🥳🥳')
    elif user.language == 'ru':
        reply_text = ('Ваши ответы приняты.' + '\n' + "Вы " + str(question_count) + ' из теста    ' +
                      str(user.true_count) + ' вы сделали.🥳🥳')
    else:
        reply_text = ('Your answers were accepted.' + '\n' + "You " + str(question_count) + ' from the test ' +
                      str(user.true_count) + ' you did.🥳🥳')
    reply_markup = footer_back_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'home_menu'
    user.true_count = 0
    user.save()


def write_question_fun(update, callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    write_question_message = WriteQuestionMessage.objects.filter(user_profile=user_profile_filter).first()
    if user.language == 'uz':
        reply_text = write_question_message.title_uz + '\n\n'
    elif user.language == 'uz':
        reply_text = write_question_message.title_ru + '\n\n'
    else:
        reply_text = write_question_message.title_en + '\n\n'
    reply_markup = write_question_button(lan)
    image = '{}'.format(write_question_message.image)
    if write_question_message.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'write_question_fun'
    user.save()


def write_question_start(update, callback, user, lan):
    vacancy = user.vacancy
    questions = WrittenQuestion.objects.filter(vacancy=vacancy)
    if questions:
        if user.write_number == len(questions):
            user.write_number = 0
            user.save()
            write_answer(update, callback, user, lan)
        else:
            for question in range(user.write_number, len(questions)):
                if user.language == 'uz':
                    user.write_question = questions[user.write_number]
                    user.save()
                    reply_text = str(user.write_number + 1) + '. ' + questions[user.write_number].title_uz
                    update.message.reply_text(text=reply_text)
                    break
                elif user.language == 'ru':
                    user.write_question = questions[user.write_number]
                    user.save()
                    reply_text = str(user.write_number + 1) + '. ' + questions[user.write_number].title_ru
                    update.message.reply_text(text=reply_text)
                    break
                else:
                    user.write_question = questions[user.write_number]
                    user.save()
                    reply_text = str(user.write_number + 1) + '. ' + questions[user.write_number].title_en
                    update.message.reply_text(text=reply_text)
                    break
        user.type = 'write_question'
        user.save()
    else:
        if user.language == 'uz':
            reply_text = lan['write_question_not_found']
        elif user.language == 'ru':
            reply_text = lan['write_question_not_found']
        else:
            reply_text = lan['write_question_not_found']
        reply_markup = footer_back_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'write_question_not'
        user.true_count = 0
        user.save()


def write_answer(update, callback, user, lan):
    if user.language == 'uz':
        reply_text = lan['write_answer_text']
    elif user.language == 'ru':
        reply_text = lan['write_answer_text']
    else:
        reply_text = lan['write_answer_text']
    reply_markup = footer_back_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'write_answer'
    user.save()

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
    footer_back_button
)
from apps.company.models import (
    CandidateLanguages,
    Candidate,
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
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    filial_message = FilialMessage.objects.filter(user_profile=user_profile_filter).first()
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
    reply_markup = filials_button(callback, user, lan)
    if filial_message.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption='', reply_markup=None, parse_mode=None)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')

    user.type = 'filials'
    user.save()


def vacancies(update, callback, user, lan):
    bot_username = callback.bot.username
    user_profile_filter = UserProfile.objects.filter(bot_username=bot_username).first()
    vacancy_message = VacancyMessage.objects.filter(user_profile=user_profile_filter).first()
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
    reply_markup = vacancies_button(callback, user, lan)
    if vacancy_message.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption='', reply_markup=None, parse_mode=None)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')

    user.type = 'vacancies'
    user.save()


def vacancy_detail(update, callback, user, lan):
    if user.language == 'uz':
        vacancy = user.vacancy
        reply_text = ('Vakasiya Malumotlari🧾:' + '\n\n' + 'Vakansiya nomi: ' + vacancy.name_uz + '\n' +
                'Lavozim: ' + vacancy.job_name_uz + '\n' + 'Ish vaqti: ' + vacancy.schedule_uz + '\n' +
                'Oylig maosh: ' + vacancy.wage_limit_uz + '\n' + "Bilish kerak bo'lgan tillar: " + vacancy.lang_uz +
                '\n\n' + "Bu shartlar sizga maqul bo'lsa. O'z malumotlaringizni qoldirishingiz mumkin.✏️")
    elif user.language == 'ru':
        vacancy = user.vacancy
        reply_text = ('Информация О Вакансии🧾:' + '\n\n' + 'Название вакансии: ' + vacancy.name_uz + '\n' +
                'Позиция: ' + vacancy.job_name_uz + '\n0' + 'Рабочее время: ' + vacancy.schedule_uz + '\n' +
                'Ежемесячная зарплата: ' + vacancy.wage_limit_uz + '\n' + "Языки, которые нужно знать: " + vacancy.lang_uz +
                '\n\n' + "Это условия, если у вас есть маки. Вы можете оставить свои данные.✏️")
    else:
        vacancy = user.vacancy
        reply_text = ('Vacancy data🧾:' + '\n\n' + 'Vacancy name: ' + vacancy.name_uz + '\n' +
                'Position: ' + vacancy.job_name_uz + '\n' + 'Work time: ' + vacancy.schedule_uz + '\n' +
                'Salary: ' + vacancy.wage_limit_uz + '\n' + "Languages to know: " + vacancy.lang_uz +
                '\n\n' + "If these conditions are applicable to you. You can leave your data.✏️")
    reply_markup = vacancy_detail_button(lan)
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
            reply_text = ("Oldin bu vakansiya uchun so'rov qoldirgansiz.✅✅\n Hr hodimlarimiz siz bilan bo'lanishadi.📞 \n\n "
                          "Malumotlaringizni yangilash imkonyatingiz ham mavjud.♻️")
        elif user.language == 'ru':
            reply_text = ("Раньше вы оставляли отклик на эту вакансию.✅✅\n Наши сотрудники отдела кадров делятся с вами.📞 \n\n "
                          "У вас также есть возможность обновить свои данные.♻️")
        else:
            reply_text = ("You've left a postcard for this vacancy before✅✅.\n Our HR staff will be with you.📞 \n\n "
                          "You also have the opportunity to update your data.♻️")
    else:
        if user.language == 'uz':
            reply_text = "Oldin bu vakansiya uchun so'ro'v qoldirmagansiz. So'ro'vnomani to'ldirishingiz mumkin.📝"
        elif user.language == 'ru':
            reply_text = "Раньше вы не оставляли отклик на эту вакансию. Вы можете заполнить анкету.📝"
        else:
            reply_text = "You haven't left a postcard for this vacancy before. You can fill out the questionnaire.📝"
    reply_markup = check_candidate_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    if user.vacancy.main_office:
        user.type = 'check_candidate_main'
        user.save()
    else:
        user.type = 'check_candidate'
        user.save()


def resume_start(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.first_name:
        last_name(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Ismingini yuboring👇"
        elif user.language == 'ru':
            reply_text = "Отправить свое имя👇"
        else:
            reply_text = "Send your first name👇"
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'resume_start'
        user.save()


def last_name(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.last_name:
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
    if resume_filter.middle_name:
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
    if resume_filter.gender:
        birthday(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Jinsingizni belgilang👇"
        elif user.language == 'ru':
            reply_text = "Укажите свой пол👇"
        else:
            reply_text = "Mark your gender👇"
        reply_markup = gender_inline(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'gender_callback'
        user.save()


def birthday(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.birthday:
        candidate_image(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Tug'ilgan kuningizni manunadagidek kiriting.🔖 \n\n Namuna: 2024-02-14👈👈"
        elif user.language == 'ru':
            reply_text = "Введите дату своего рождения, как в примере.🔖 \n\n Пример: 2024-02-14👈👈"
        else:
            reply_text = "Enter your birthday as in the sample.🔖 \n\n Sample: 2024-02-14👈👈"
        reply_markup = footer_button(lan)
        update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'birthday'
        user.save()


def candidate_image(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.image:
        main_phone(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Rasmingizni yuboring.📤 \n\n Agar bo'lmasa yo'q dey yozing.🖌"
        elif user.language == 'ru':
            reply_text = "Отправьте свою фотографию.📤 \n\n Напишите нет, если нет.🖌"
        else:
            reply_text = "Send your photo.📤 \n\n If not write no dey.🖌"
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'candidate_image'
        user.save()


def main_phone(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.main_phone:
        extra_phone(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Asosiy telefon raqamingizni yuboring📱"
        elif user.language == 'ru':
            reply_text = "Отправьте свой основной номер телефона📱"
        else:
            reply_text = "Send your main phone number📱"
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'main_phone'
        user.save()


def extra_phone(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.extra_phone:
        email(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Qo'shimcha telefon raqamingizni yuboring.📱 \n\n Agar bo'lmasa yo'q dey yozing.🖊"
        elif user.language == 'ru':
            reply_text = "Отправьте свой дополнительный номер телефона.📱 \n\n Напишите нет, если нет.🖊"
        else:
            reply_text = "Send your additional phone number.📱 \n\n If not write no dey.🖊"
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'extra_phone'
        user.save()


def email(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.email:
        address(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Email adresingizni yuboring📧 \n\n Agar bo'lmasa yo'q dey yozing.🖊"
        elif user.language == 'ru':
            reply_text = "Отправить свой адрес электронной почты📧 \n\n Напишите нет, если нет.🖊"
        else:
            reply_text = "Send your Email address📧 \n\n If not write no dey.🖊"
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'email'
        user.save()


def address(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.address:
        legal_address(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Hozir yashab turgan adresingizni to'liq yozib yuboring.🪧🪧"
        elif user.language == 'ru':
            reply_text = "Напишите полный адрес, по которому вы сейчас живете.🪧🪧"
        else:
            reply_text = "Write down the full address you are currently living in.🪧🪧"
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'address'
        user.save()


def legal_address(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.legal_address:
        wage_expectation(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Qonuniy adresingizni to'liq yozib yuboring🪧"
        elif user.language == 'ru':
            reply_text = "Напишите полный юридический адрес🪧"
        else:
            reply_text = "Write down your legal address in full🪧"
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'legal_address'
        user.save()


def wage_expectation(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.wage_expectation:
        node(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Siz ush ushbu vakansiya uchun qancha oylig talab qilasiz.💸💰"
        elif user.language == 'ru':
            reply_text = "Сколько месяцев вам потребуется для этой вакансии.💸💰"
        else:
            reply_text = "How many months do you require ush for this vacancy.💸💰"
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'wage_expectation'
        user.save()


def node(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.note:
        language_inline_fun(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "O'zingiz haqingida qo'shimcha malumotlar. Ustunlik jihatlarinigiz hamda kamchiklaringizni yuboring.📝📝"
        elif user.language == 'ru':
            reply_text = "Дополнительная информация о себе. Опубликуйте свои преимущества, а также недостатки.📝📝"
        else:
            reply_text = "Additional information about yourself. Send your preference aspects as well as your ventricles.📝📝"
        reply_markup = footer_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'node'
    user.save()


def language_inline_fun(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.language:
        education_inline_fun(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Biladigan tilingizni va darajangizni belgilang👇👇"
        elif user.language == 'ru':
            reply_text = "Установите язык и уровень, который вы знаете👇👇"
        else:
            reply_text = "Mark the language and level you know👇👇"
        reply_markup = language_inline(callback, user, lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'language_inline_fun'
        user.save()


def education_inline_fun(update, callback, user, lan):
    resume_filter = user.resume_filter
    if resume_filter.education:
        your_resume(update, callback, user, lan)
    else:
        if user.language == 'uz':
            reply_text = "Bilim darajangizni belgilang"
        elif user.language == 'ru':
            reply_text = "Установите свой уровень знаний"
        else:
            reply_text = "Set your level of knowledge"
        reply_markup = education_inline(callback, user, lan)
        if resume_filter.language:
            update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        else:
            update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
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
        reply_text = ('Sizning Malumotlaringiz👇👇' + '\n\n' + 'Ismingiz: ' + candidate.first_name + '\n' +
                'Familyangiz: ' + candidate.last_name + '\n0' + 'Sharifingiz: ' + candidate.middle_name + '\n' +
                'Jinsingiz: ' + candidate.gender + '\n' + "Tug'ilgan kuningiz: " + str(candidate.birthday) + '\n' +
                "Telefon 1: " + candidate.main_phone + '\n' + 'Telefon 2: ' + candidate.extra_phone + '\n' +
                'Email: ' + candidate.email + '\n' + 'Adres: ' + candidate.address + '\n' +
                'Qonuniy adres: ' + candidate.legal_address + '\n' + 'Oylig maosh: ' + candidate.wage_expectation + '\n' +
                'Tavsif: ' + candidate.note + '\n' + 'Tillar: ' + languages_text)
    elif user.language == 'ru':
        reply_text = ('Ваши Данные👇👇' + '\n\n' + 'Ваше имя: ' + candidate.first_name + '\n' +
                'Твоя фамилия: ' + candidate.last_name + '\n0' + 'Ваш шериф: ' + candidate.middle_name + '\n' +
                'Ваш пол: ' + candidate.gender + '\n' + "Твой день рождения: " + str(candidate.birthday) + '\n' +
                "Телефон 1: " + candidate.main_phone + '\n' + 'Телефон 2: ' + candidate.extra_phone + '\n' +
                'Электронная почта: ' + candidate.email + '\n' + 'Адрес: ' + candidate.address + '\n' +
                'Юридический адрес: ' + candidate.legal_address + '\n' + 'Зарплата: ' + candidate.wage_expectation + '\n' +
                'Описание: ' + candidate.note + '\n' + 'Языки: ' + languages_text)
    else:
        reply_text = ('Your Data👇👇' + '\n\n' + 'First name: ' + candidate.first_name + '\n' +
                'Last name: ' + candidate.last_name + '\n0' + 'Middle name: ' + candidate.middle_name + '\n' +
                'Gender: ' + candidate.gender + '\n' + "Your birthday: " + str(candidate.birthday) + '\n' +
                "Phone 1: " + candidate.main_phone + '\n' + 'Phone 2: ' + candidate.extra_phone + '\n' +
                'Email: ' + candidate.email + '\n' + 'Adress: ' + candidate.address + '\n' +
                'Legal address: ' + candidate.legal_address + '\n' + 'Salary: ' + candidate.wage_expectation + '\n' +
                'Node: ' + candidate.note + '\n' + 'Lanuages: ' + languages_text)
    reply_markup = resume_footer(lan)
    image = '{}'.format(candidate.image)
    if candidate.image:
        update.callback_query.message.reply_photo(photo=open(image, 'rb'), caption='', reply_markup=reply_markup,
                                                  parse_mode='HTML')
        update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_markup[:4096], parse_mode='HTML')
    else:
        update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_markup[:4096], parse_mode='HTML')
    user.type = 'your_resume'
    user.save()


def finish_resume(update, callback, user, lan):
    candidate = user.candidate
    send_candidate_data_to_api(candidate)
    if user.language == 'uz':
        reply_text = ("Tabriklaymiz sizning malumotlaringiz qabul qilindi.✅✅ \n\n Yozma savollar hamda shu vakansiya"
                      " bo'yicha qisqa test bajarishingiz kerak bo'ladi👇👇")
    elif user.language == 'ru':
        reply_text = ("Tabriklaymiz sizning malumotlaringiz qabul qilindi.✅✅ \n\n Вам нужно будет выполнить "
                      "письменные вопросы, а также короткий тест на эту вакансию👇👇")
    else:
        reply_text = ("Congratulations your information received.✅✅ \n\n You will need to do written questions as "
                      "well as a short test on the same vacancy👇👇")
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
    elif user.language == 'uz':
        reply_text = contact_message.title_ru + '\n\n'
    else:
        reply_text = contact_message.title_en + '\n\n'
    reply_markup = contact_button(lan)
    image = '{}'.format(contact_message.image)
    if contact_message.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption='', reply_markup=None, parse_mode=None)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'home_menu'
    user.save()


def about_company(update, callback, user, lan):
    content = AboutCompany.objects.all()
    content = content[0]
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
            reply_text = 'Test savollari kiritilmagan.'
        elif user.language == 'ru':
            reply_text = 'Тестовые вопросы не включены'
        else:
            reply_text = 'Test questions not included'
        reply_markup = footer_button_finish(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'home_menu'
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
            reply_text = 'Savollar kiritilmagan. Orqaga qaytib test ishlashingiz kerak.👇'
        elif user.language == 'ru':
            reply_text = 'Вопросы не включены. Вы должны работать в обратном тестировании.👇'
        else:
            reply_text = 'Questions not included. You have to work the test back👇'
        reply_markup = footer_back_button(lan)
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
        user.type = 'write_question_not'
        user.true_count = 0
        user.save()


def write_answer(update, callback, user, lan):
    if user.language == 'uz':
        reply_text = ("Javoblaringiz qabul qilindi. Orqaga qaytib test ishlashingiz kerak."
                      " \n\n Agar ishlagan bo'lsangiz orqaga qaytib bosh sahifaga o'ting👇👇")
    elif user.language == 'ru':
        reply_text = ("Ваши ответы приняты. Вы должны работать в обратном тестировании. "
                      " \n\n Вернитесь на домашнюю страницу, если вы работали👇👇")
    else:
        reply_text = ("Your answers were accepted. You have to work the test back. "
                      " \n\n Go back to the home page if you've worked👇👇")
    reply_markup = footer_back_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'write_answer'
    user.save()

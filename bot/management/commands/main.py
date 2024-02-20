from apps.content.models import (
    FilialMessage,
    RegionMessage,
    VacancyMessage,
    MainOfficeVacancyMessage,
    ContactMessage
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
    check_candidate_button
)
from apps.company.models import (
    CandidateLanguages,
    Candidate
)
from apps.main.models import (
    Education,
    Contact,
    AboutCompany
)


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
        update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
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
        update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
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
        update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')

    user.type = 'vacancies'
    user.save()


def vacancy_detail(update, callback, user, lan):
    if user.language == 'ru':
        vacancy = user.vacancy
        reply_text = ('Vakasiya Malumotlari' + '\n\n' + 'Vakansiya nomi: ' + vacancy.name_uz + '\n' +
                'Lavozim: ' + vacancy.job_name_uz + '\n0' + 'Ish vaqti: ' + vacancy.schedule_uz + '\n' +
                'Oylig moash: ' + vacancy.wage_limit_uz + '\n' + "Bilish kerak bo'lgan tillar: " + vacancy.lang_uz +
                '\n\n' + "Bu shartlar sizga maqul bo'lsa. O'z malumotlaringizni qoldirishingiz mumkin.")
    elif user.language == 'en':
        vacancy = user.vacancy
        reply_text = ('Vakasiya Malumotlari' + '\n\n' + 'Vakansiya nomi: ' + vacancy.name_uz + '\n' +
                'Lavozim: ' + vacancy.job_name_uz + '\n0' + 'Ish vaqti: ' + vacancy.schedule_uz + '\n' +
                'Oylig moash: ' + vacancy.wage_limit_uz + '\n' + "Bilish kerak bo'lgan tillar: " + vacancy.lang_uz +
                '\n\n' + "Bu shartlar sizga maqul bo'lsa. O'z malumotlaringizni qoldirishingiz mumkin.")
    else:
        vacancy = user.vacancy
        reply_text = ('Vakasiya Malumotlari' + '\n\n' + 'Vakansiya nomi: ' + vacancy.name_uz + '\n' +
                'Lavozim: ' + vacancy.job_name_uz + '\n' + 'Ish vaqti: ' + vacancy.schedule_uz + '\n' +
                'Oylig moash: ' + vacancy.wage_limit_uz + '\n' + "Bilish kerak bo'lgan tillar: " + vacancy.lang_uz +
                '\n\n' + "Bu shartlar sizga maqul bo'lsa. O'z malumotlaringizni qoldirishingiz mumkin.")
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
        if user.language == 'ru':
            reply_text = ("Oldin bu vakansiya uchun otklik qoldirgansiz. Hr hodimlarimiz siz bilan bo'lanishadi. \n\n "
                          "Malumotlaringizni yangilash imkonyatingiz ham mavjud.")
        elif user.language == 'en':
            reply_text = ("Oldin bu vakansiya uchun otklik qoldirgansiz. Hr hodimlarimiz siz bilan bo'lanishadi. \n\n "
                          "Malumotlaringizni yangilash imkonyatingiz ham mavjud. ru")
        else:
            reply_text = ("Oldin bu vakansiya uchun otklik qoldirgansiz. Hr hodimlarimiz siz bilan bo'lanishadi. \n\n "
                          "Malumotlaringizni yangilash imkonyatingiz ham mavjud. en")
    else:
        if user.language == 'ru':
            reply_text = "Oldin bu vakansiya uchun otklik qoldirmagansiz. Hr hodimlarimiz siz bilan bo'lanishadi. \n\n "
        elif user.language == 'en':
            reply_text = "Oldin bu vakansiya uchun otklik qoldirmagansiz. Hr hodimlarimiz siz bilan bo'lanishadi. \n\n ru"
        else:
            reply_text = "Oldin bu vakansiya uchun otklik qoldirmagansiz. Hr hodimlarimiz siz bilan bo'lanishadi. \n\n en"
    reply_markup = check_candidate_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    if user.vacancy.main_office:
        user.type = 'check_candidate_main'
        user.save()
    else:
        user.type = 'check_candidate'
        user.save()


def resume_start(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Ismingini kiritish"
    elif user.language == 'en':
        reply_text = "Ismingini kiritish ru"
    else:
        reply_text = "Ismingini kiritish en"
    reply_markup = footer_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'resume_start'
    user.save()


def last_name(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Familyangizni kiriting"
    elif user.language == 'en':
        reply_text = "Familyangizni kiriting ru"
    else:
        reply_text = "Familyangizni kiriting en"
    reply_markup = footer_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'last_name'
    user.save()


def middle_name(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Sharifingizni kiriting"
    elif user.language == 'en':
        reply_text = "Sharifingizni kiriting ru"
    else:
        reply_text = "Sharifingizni kiriting en"
    reply_markup = footer_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'middle_name'
    user.save()


def gender(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Jinsingizni kiriting"
    elif user.language == 'en':
        reply_text = "Jinsingizni kiriting ru"
    else:
        reply_text = "Jinsingizni kiriting en"
    reply_markup = gender_inline(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'gender_callback'
    user.save()


def birthday(update, callback, user, lan):
    print('update message', update.message)
    if user.language == 'ru':
        reply_text = "Tug'ilgan kuningizni manunadagidek kiriting \n\n Namuna: 2024-02-14"
    elif user.language == 'en':
        reply_text = "Tug'ilgan kuningizni manunadagidek kiriting \n\n Namuna: 2024-02-14 ru"
    else:
        reply_text = "Tug'ilgan kuningizni manunadagidek kiriting \n\n Namuna: 2024-02-14 en"
    reply_markup = footer_button(lan)
    update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'birthday'
    user.save()


def candidate_image(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Rasmingizni yuboring"
    elif user.language == 'en':
        reply_text = "Rasmingizni yuboring ru"
    else:
        reply_text = "Rasmingizni yuboring en"
    reply_markup = footer_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'candidate_image'
    user.save()


def main_phone(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Asosiy telefon raqamingizni yuboring"
    elif user.language == 'en':
        reply_text = "Asosiy telefon raqamingizni yuboring ru"
    else:
        reply_text = "Asosiy telefon raqamingizni yuboring en"
    reply_markup = footer_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'main_phone'
    user.save()


def extra_phone(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Ikkinchi telefon raqamingizni yuboring"
    elif user.language == 'en':
        reply_text = "Ikkinchi telefon raqamingizni yuboring ru"
    else:
        reply_text = "Ikkinchi telefon raqamingizni yuboring en"
    reply_markup = footer_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'extra_phone'
    user.save()


def email(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Emailingizni yuboring"
    elif user.language == 'en':
        reply_text = "Emailingizni yuboring ru"
    else:
        reply_text = "Emailingizni yuboring en"
    reply_markup = footer_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'email'
    user.save()


def address(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Adresingizni to'liq yuboring"
    elif user.language == 'en':
        reply_text = "Adresingizni to'liq yuboring ru"
    else:
        reply_text = "Adresingizni to'liq yuboring en"
    reply_markup = footer_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'address'
    user.save()


def legal_address(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Qonuniy adresingizni to'liq yuboring"
    elif user.language == 'en':
        reply_text = "Qonuniy adresingizni to'liq yuboring ru"
    else:
        reply_text = "Qonuniy adresingizni to'liq yuboring en"
    reply_markup = footer_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'legal_address'
    user.save()


def wage_expectation(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Siz kutayotgan oyligni yuboring"
    elif user.language == 'en':
        reply_text = "Siz kutayotgan oyligni yuboring ru"
    else:
        reply_text = "Siz kutayotgan oyligni yuboring en"
    reply_markup = footer_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'wage_expectation'
    user.save()


def node(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "O'zingiz uchun eslatma yuboring"
    elif user.language == 'en':
        reply_text = "O'zingiz uchun eslatma yuboring ru"
    else:
        reply_text = "O'zingiz uchun eslatma yuboring en"
    reply_markup = footer_button(lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'node'
    user.save()


def language_inline_fun(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Biladigan tilingizni va darajangizni belgilang"
    elif user.language == 'en':
        reply_text = "Biladigan tilingizni va darajangizni belgilang ru"
    else:
        reply_text = "Biladigan tilingizni va darajangizni belgilang en"
    reply_markup = language_inline(user, lan)
    update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'language_inline_fun'
    user.save()


def education_inline_fun(update, callback, user, lan):
    if user.language == 'ru':
        reply_text = "Biladigan tilingizni va darajangizni belgilang"
    elif user.language == 'en':
        reply_text = "Biladigan tilingizni va darajangizni belgilang ru"
    else:
        reply_text = "Biladigan tilingizni va darajangizni belgilang en"
    reply_markup = education_inline(user, lan)
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
        languages_text += '\n' + candidate_language1 + candidate_language_level1
    reply_text = ('Vakasiya Malumotlari' + '\n\n' + 'Ismingiz: ' + candidate.first_name + '\n' +
            'Familyangiz: ' + candidate.last_name + '\n0' + 'Sharifingiz: ' + candidate.middle_name + '\n' +
            'Jinsingiz: ' + candidate.gender + '\n' + "Tug'ilgan kuningiz: " + str(candidate.birthday) + '\n' +
            "Telefon 1: " + candidate.main_phone + '\n' + 'Telefon 2: ' + candidate.extra_phone + '\n' +
            'Email: ' + candidate.email + '\n' + 'Adres: ' + candidate.address + '\n' +
            'Qoduniy adres: ' + candidate.legal_address + '\n' + 'Oylig maosh: ' + candidate.wage_expectation + '\n' +
            'Tavsif: ' + candidate.node + '\n' + 'Tillar:' + languages_text,
            '\n\n' + "Malumotlaringiz to'g'ri bo'lsa Yakunlash tugamasini bosing. \n Agar malumotlar hato bo'lsa qayta"
                     " boshlash tugamasini bosing")

    image = '{}'.format(candidate.image)
    reply_markup = resume_footer(lan)
    if candidate.image:
        update.callback_query.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                                  parse_mode='HTML')
    else:
        update.callback_query.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'your_resume'
    user.save()


def finish_resume(update, callback, user, lan):
    if user.language == 'uz':
        reply_text = "Sizning malumotlaringiz qabul qilindi. \n Marhamat sinov testini bajarishingiz mumkin."
    elif user.language == 'ru':
        reply_text = "Sizning malumotlaringiz qabul qilindi. \n Marhamat sinov testini bajarishingiz mumkin. ru"
    else:
        reply_text = "Sizning malumotlaringiz qabul qilindi. \n Marhamat sinov testini bajarishingiz mumkin.en"
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
        update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
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
        update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
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
        update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
    elif content.image:
        update.message.reply_photo(photo=open(image, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
    elif content.video:
        update.message.reply_video(video=open(video, 'rb'), caption=reply_text, reply_markup=reply_markup,
                                   parse_mode='HTML')
    else:
        update.message.reply_text(text=reply_text, reply_markup=reply_markup, parse_mode='HTML')
    user.type = 'home_menu'
    user.save()
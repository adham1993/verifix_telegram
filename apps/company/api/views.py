from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from apps.company.models import (
    Region,
    Filial
)
import requests
import json
from datetime import datetime, date
from apps.main.models import (
    WrittenAnswer
)


class RegionCreateView(APIView):

    def post(self, request, format=None):
        url = "https://app.verifix.com/b/vhr/api/v1/pro/region$list"
        username = "askoishbot@pro"
        password = "123456"
        print(self.request.headers.get('region_id'))
        response = requests.get(url, auth=(username, password))
        print('response', response)
        if response.status_code == 200:
            vacancies_data = response.json().get('data', [])

            for data1 in vacancies_data:
                region_name = data1.get('vacancy_name', '')
                print('data1', data1)
            res = {
                'status': 1,
                'msg': 'Vacancies created successfully'
            }
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {
                'status': 0,
                'msg': 'Vacancies not found'
            }
            return Response(res, status=status.HTTP_200_OK)


class FilialCreateView(APIView):

    def post(self, request, format=None):
        url = "https://app.verifix.com/b/vhr/api/v1/core/division$list"
        username = "askoishbot@pro"
        password = "123456"
        print(self.request.headers.get('region_id'))
        response = requests.get(url, auth=(username, password))
        print('response', response)
        if response.status_code == 200:
            vacancies_data = response.json().get('data', [])

            for data1 in vacancies_data:
                vacancy_name = data1.get('vacancy_name', '')
                print('data1', data1)
            res = {
                'status': 1,
                'msg': 'Vacancies created successfully'
            }
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {
                'status': 0,
                'msg': 'Vacancies not found'
            }
            return Response(res, status=status.HTTP_200_OK)


class VacancyCreateView(APIView):

    def post(self, request, format=None):
        url = "https://app.verifix.com/b/vhr/api/v1/rec/vacancy$vacancies"
        username = "askoishbot@pro"
        password = "123456"
        print(self.request.headers.get('region_id'))
        response = requests.get(url, auth=(username, password))
        print('response', response)
        if response.status_code == 200:
            vacancies_data = response.json().get('data', [])

            for data1 in vacancies_data:
                vacancy_name = data1.get('vacancy_name', '')
                print('data1', data1)
            res = {
                'status': 1,
                'msg': 'Vacancies created successfully'
            }
            return Response(res, status=status.HTTP_200_OK)
        else:
            res = {
                'status': 0,
                'msg': 'Vacancies not found'
            }
            return Response(res, status=status.HTTP_200_OK)


def send_candidate_data_to_api(candidate):
    username = candidate.company.login
    password = candidate.company.password
    birthday_str = candidate.birthday.strftime('%d.%m.%Y')
    gender = candidate.gender
    if gender == 'Erkak' or gender == 'Мужчина' or gender == 'Mail':
        gender = 'M'
    elif gender == 'Ayol' or gender == 'Женщины' or gender == 'Femail':
        gender = 'F'
    else:
        gender = None

    write_answers = WrittenAnswer.objects.filter(candidate=candidate)
    write_answer_list = []
    for write_answer in write_answers:
        a = {
            'code': write_answer.write_question.write_integration_code,
            'value': write_answer.title
            }
        write_answer_list.append(a)
    if candidate.test_status:
        test_failed = 'N'
    else:
        test_failed = 'Y'
    if candidate.full_name:
        name = candidate.full_name
        parts = name.split(maxsplit=3)
        if len(parts) >= 3:
            first, last = parts[:2]
            middle = ' '.join(parts[2:])
        elif len(parts) == 2:
            first, last = parts
            middle = ""
        else:
            first = parts[0]
            last = ""
            middle = ""
    else:
        first = ''
        last = ''
        middle = ''
    if not candidate.chat_id:
        chat_id = 1
    else:
        chat_id = candidate.chat_id
    data = {
        "first_name": first,
        "last_name": last,
        "middle_name": middle,
        "gender": gender,
        "birthday": birthday_str,
        "region_id": candidate.region.integration_code,
        "main_phone": candidate.main_phone,
        "extra_phone": candidate.extra_phone,
        "email": candidate.email,
        "address": candidate.address,
        "legal_address": candidate.legal_address,
        "wage_expectation": candidate.wage_expectation,
        "note": candidate.note,
        "edu_stage_ids": list(candidate.education.all().values_list('integration_code', flat=True)),
        "job_ids": [],
        "langs": [
            {"lang_id": lang.language.integration_code, "level_id": lang.language_level.integration_code}
            for lang in candidate.candidate_languages.all()
        ],
        "fields": write_answer_list,
        "contact_code": chat_id,
        "vacancy_id": candidate.vacancy.vacancy_integration_code,
        "test_failed": test_failed,
        "test_score": candidate.test_score
    }
    print(data)
    api_url = "https://app.verifix.com/b/vhr/api/v1/pro/candidate$telegram_create"
    headers = {
        'filial_id': str(candidate.company.filial_id),
        'project_code': 'vhr'
    }
    response = requests.post(api_url, json=data, auth=(username, password), headers=headers)
    print(response.status_code)
    print(response.text)
    try:
        json_response = response.json()
        print(json_response)
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        print(response.text)


def candidate_photo_upload(candidate):
    username = candidate.company.login
    password = candidate.company.password

    url = "https://app.verifix.com/b/vhr/api/v1/pro/candidate$telegram_photo_set"

    payload = {'param': f'{{"contact_code": "{candidate.chat_id}", "photo_sha": "\\u00000"}}'}
    files = [
        ('files[0]',
         ('photo_2024-02-15_14-56-06.jpg', open(candidate.image.path, 'rb'), 'image/jpeg'))
    ]
    headers = {
        'filial_id': '55302',
        'project_code': 'vhr',
        'BiruniUpload': 'param',
        # 'Authorization': 'Basic dGVsZWdyYW1AcHJvOjE='
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files, auth=(username, password))
    print(response.status_code)
    print(response.text)

    try:
        json_response = response.json()
        print(json_response)
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        print(response.text)

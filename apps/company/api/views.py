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
    username = "askoishbot@pro"
    password = "123456"
    birthday_str = candidate.birthday.strftime('%d.%m.%Y')
    data = {
        "first_name": candidate.first_name,
        "last_name": candidate.last_name,
        "middle_name": candidate.middle_name,
        "gender": candidate.gender,
        "birthday": birthday_str,
        "region_id": candidate.region.id,
        "main_phone": candidate.main_phone,
        "extra_phone": candidate.extra_phone,
        "email": candidate.email,
        "address": candidate.address,
        "legal_address": candidate.legal_address,
        "wage_expectation": candidate.wage_expectation if candidate.wage_expectation else None,
        "note": candidate.note,
        "edu_stage_ids": list(candidate.education.all().values_list('id', flat=True)),
        "job_ids": None,
        "langs": [
            {"lang_id": lang.language.id, "level_id": lang.language_level.id}
            for lang in candidate.candidate_languages.all()
        ]
    }
    print(data)
    api_url = "https://app.verifix.com/b/vhr/api/v1/pro/candidate$create"

    response = requests.post(api_url, json=data, auth=(username, password))
    print(response.text)
    try:
        json_response = response.json()
        print(json_response)
    except requests.exceptions.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        print(response.text)

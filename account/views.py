import json
import bcrypt
import jwt
import random

from .models import Account, Label
from .settings import SECRET_KEY

from django.views import View
from django.http import HttpResponse, JsonResponse


class SignUpAPI(View):
    '''
        회원가입
    '''

    def post(self, request):
        '''
            새로운 아이디 회원가입
            body: {
                email: string;
                password: string;
            }
        '''
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email=data['email']).exists():
                return JsonResponse({"message": "EXISTS_EMAIL"}, status=400)

            password = bcrypt.hashpw(data["password"].encode(
                "UTF-8"), bcrypt.gensalt()).decode("UTF-8")
            Account.objects.create(
                email=data['email'],
                password=password
            ).save()
            user = Account.objects.get(email=data["email"])
            return JsonResponse({"user_id": user.id}, status=200)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)

    def get(self, request):
        '''
            모든 회원정보 불러오기
        '''
        account_data = Account.objects.values()
        return JsonResponse({'accounts': list(account_data)}, status=200)


class SignInAPI(View):
    '''
        로그인
    '''

    def post(self, request):
        '''
            로그인
            body: {
                email: string;
                password: string;
            }
        '''
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email=data["email"]).exists():
                user = Account.objects.get(email=data["email"])
                if bcrypt.checkpw(data['password'].encode('UTF-8'), user.password.encode('UTF-8')):
                    token = jwt.encode({'user': user.id},
                                       SECRET_KEY, algorithm='HS256')
                    return JsonResponse({"token": token, "user_id": user.id}, status=200)
                return HttpResponse(status=400)
            return HttpResponse(status=400)
        except KeyError as E:
            return JsonResponse({'message': "INVALID_KEYS"}, status=400)


class LabelAPI(View):
    '''
        라벨링
    '''

    def post(self, request):
        '''
            유저의 새로운 label 등록
            body: {
                account_id: int;
                name: string;
            }
        '''
        data = json.loads(request.body)
        try:
            if not Account.objects.filter(id=data['account_id']).exists():
                return JsonResponse({"message": "NOT_EXISTS_ID"}, status=400)
            # generate random color_code
            color_code = "#" + \
                "".join([random.choice("0123456789ABCDEF") for j in range(6)])
            Label.objects.create(
                account_id=data['account_id'],
                name=data['name'],
                color_code=color_code
            ).save()
            label_data = Label.objects.filter(
                account_id=data['account_id']).values()
            return JsonResponse({'labels': list(label_data)}, status=200)
        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)

    def get(self, request):
        '''
            유저의 label들 불러오기
            querystring: {
                account_id: int;
            }
        '''
        account_id = request.GET.get('account_id', None)
        label_data = Label.objects.filter(account_id=account_id).values()
        return JsonResponse({'labels': list(label_data)}, status=200)

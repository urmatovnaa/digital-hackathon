from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from account_app.models import Account


class LoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        login = request.data.get('email')
        if login != None:
            if not Account.objects.filter(email=login).exists():
                return Response(
                    f'{login} - этого пользователя нет'
                    , status=400)
        elif login == None:
            return Response(
                f'Введите email или пароль'
                , status=400)
        user = Account.objects.get(email=login)
        password = request.data.get('password')
        pass_check = user.check_password(password)
        if not pass_check:
            return Response('Неверный пароль и/или email', status=400)
        return Response('Hello', status=201)

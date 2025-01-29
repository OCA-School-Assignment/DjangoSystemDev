from django.shortcuts import redirect
from django.urls import reverse

class SessionAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 以下の条件でセッションが存在しないユーザーをログインページにリダイレクト
        if not request.session.get('employee_id') and request.path not in self.get_exempt_paths():
            return redirect(reverse('index'))  # ログインページにリダイレクト
        return self.get_response(request)

    def get_exempt_paths(self):
        return [
            reverse('index'),
        ]

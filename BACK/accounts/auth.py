from accounts.models import User
from django.contrib.auth.hashers import check_password, make_password


class Authentication:
    def signin(self, username: str, password: str) -> User | bool:
        user = User.objects.filter(username=username).first()

        if user and check_password(password, user.password):
            return user

        return False

    def signup(self, name: str, username: str, email: str, password: str) -> User | bool:
        if User.objects.filter(username=username).exists():
            return False

        user = User.objects.create(
            name=name,
            username=username,
            email=email,
            password=make_password(password)
        )

        return user
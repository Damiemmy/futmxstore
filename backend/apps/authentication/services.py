from django.db import transaction
from .models import User, Role, UserRole


@transaction.atomic
def register_user(*, email, password, username=None):
    """
    Business workflow for user registration.

    Responsibilities:
    - Create user
    - Assign Customer role
    - Return created user

    Future:
    - Send verification email
    """

    user = User.objects.create_user(
        email=email,
        password=password,
        username=username,
    )

    customer_role = Role.objects.get(name="Customer")

    UserRole.objects.create(
        user=user,
        role=customer_role,
        is_active=True,
        is_approved=True,
    )

    return user
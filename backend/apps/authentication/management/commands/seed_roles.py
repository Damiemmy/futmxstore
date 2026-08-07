from django.core.management.base import BaseCommand

from apps.authentication.models import Role


class Command(BaseCommand):

    help = "Seed default system roles."

    def handle(self, *args, **options):

        roles = [
            "Customer",
            "Course Representative",
            "Lecturer",
            "Vendor",
            "Admin",
        ]

        for role_name in roles:

            Role.objects.get_or_create(
                name=role_name
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Roles seeded successfully."
            )
        )

# future upgrade to inform the developer what happened
'''
role, created = Role.objects.get_or_create(
    name=role_name
)

if created:
    self.stdout.write(
        self.style.SUCCESS(
            f"Created: {role_name}"
        )
    )
else:
    self.stdout.write(
        self.style.WARNING(
            f"Already exists: {role_name}"
        )
    )

'''
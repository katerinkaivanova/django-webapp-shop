from django.core.management.base import BaseCommand
from authapp.models import ShopUser
from authapp.models import ShopUserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        update_users = ShopUser.objects.filter(shopuserprofile__isnull=True)

        for user in update_users:
            users_profile = ShopUserProfile.objects.create(user=user)
            users_profile.save()

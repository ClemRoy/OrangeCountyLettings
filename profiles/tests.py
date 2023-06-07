import pytest

from django.urls import reverse
from django.test import Client
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_url_title_template_profiles_index():
    client = Client()

    User.objects.create(
        username="MrDetective",
        password="Watson",
        email="Detective@england.com",
        first_name="Sherlock",
        last_name="Holmes"
    )

    user_id = User.objects.last().pk

    Profile.objects.create(
        user_id=user_id,
        favorite_city="London"
    )

    response = client.get(reverse("profiles:index"))
    content = response.content.decode()

    expected_content = "<title>Profiles</title>"
    expected_template = "profiles/index.html"

    assert response.status_code == 200
    assert expected_content in content
    assert expected_template in [t.name for t in response.templates]


@pytest.mark.django_db
def test_url_title_template_profiles():
    client = Client()

    User.objects.create(
        username="MrDetective",
        password="Watson",
        email="Detective@england.com",
        first_name="Sherlock",
        last_name="Holmes"
    )

    user_id = User.objects.last().pk

    Profile.objects.create(
        user_id=user_id,
        favorite_city="London"
    )

    profile_username = Profile.objects.last()

    response = client.get(reverse("profiles:profile", args=[profile_username]))
    content = response.content.decode()

    expected_content = f"<title>{profile_username}</title>"
    expected_template = "profiles/profile.html"

    assert response.status_code == 200
    assert expected_content in content
    assert expected_template in [t.name for t in response.templates]

import pytest

from django.urls import reverse
from django.test import Client
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_url_title_template_lettings_index():
    client = Client()

    Address.objects.create(
        number=221,
        street="B,Baker street",
        city="London",
        state="England",
        zip_code=1,
        country_iso_code="GBR"
    )

    Letting.objects.create(
        title="Sherlock's Home",
        address_id=1
    )

    response = client.get(reverse("lettings:index"))
    content = response.content.decode()

    expected_content = "<title>Lettings</title>"
    expected_template = "lettings/index.html"

    assert response.status_code == 200
    assert expected_content in content
    assert expected_template in [t.name for t in response.templates]


@pytest.mark.django_db
def test_url_title_template_lettings():
    client = Client()

    Address.objects.create(
        number=221,
        street="B,Baker street",
        city="London",
        state="England",
        zip_code=1,
        country_iso_code="GBR"
    )

    Letting.objects.create(
        title="Sherlock Home",
        address_id=1
    )

    id = Letting.objects.last().pk
    response = client.get(reverse("lettings:letting", args=[id]))
    content = response.content.decode()

    expected_content = "<title>Sherlock Home</title>"
    expected_template = "lettings/letting.html"

    assert response.status_code == 200
    assert expected_content in content
    assert expected_template in [t.name for t in response.templates]

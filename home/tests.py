import pytest

from django.urls import reverse
from django.test import Client


def test_url_title_content_home():
    client = Client()
    response = client.get(reverse("home:index"))
    content = response.content.decode()
    expected_content = "<title>Holiday Homes</title>"
    expected_template = "home/index.html"

    assert response.status_code == 200
    assert expected_content in content
    assert expected_template in [t.name for t in response.templates]

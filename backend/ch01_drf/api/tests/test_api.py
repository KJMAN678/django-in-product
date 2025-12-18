import pytest
from rest_framework.test import APIRequestFactory

from ch01_drf.api.views import HelloWorldView


class TestHelloWorldView:
    def test_get_success(self):
        factory = APIRequestFactory()
        view = HelloWorldView.as_view()

        url = "http://127.0.0.1:8000/v1/api/hello-world/"
        request = factory.get(url)

        # pyrefly: ignore [not-callable]
        response = view(request, version="v1")
        assert response.status_code == 200

    @pytest.mark.parametrize("version", ["v1", "v2"])
    def test_get_success_version(self, version):
        factory = APIRequestFactory()
        view = HelloWorldView.as_view()

        url = f"http://127.0.0.1:8000/{version}/api/hello-world/"
        request = factory.get(url)

        # pyrefly: ignore [not-callable]
        response = view(request, version=version)
        assert response.data == {"message": f"Hello, World! {version}"}

    def test_get_fail_version(self):
        factory = APIRequestFactory()
        view = HelloWorldView.as_view()
        version = "v3"

        url = f"http://127.0.0.1:8000/{version}/api/hello-world/"
        request = factory.get(url)

        # pyrefly: ignore [not-callable]
        response = view(request, version=version)
        assert response.data == {"detail": "URLパス内のバージョンが不正です。"}

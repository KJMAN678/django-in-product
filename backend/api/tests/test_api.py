import pytest
from rest_framework.test import APIRequestFactory

from api.views import HelloWorldView


class TestHelloWorldView:
    @pytest.mark.parametrize("version", ["v1", "v2"])
    def test_get(self, version):
        factory = APIRequestFactory()
        view = HelloWorldView.as_view()

        url = f"http://127.0.0.1:8000/{version}/api/hello-world/"
        request = factory.get(url)

        response = view(request, version=version)
        assert response.data == {"message": f"Hello, World! {version}"}

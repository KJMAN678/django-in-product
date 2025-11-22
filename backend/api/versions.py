from rest_framework.versioning import URLPathVersioning


class Versioning(URLPathVersioning):
    allowed_versions = ["v1", "v2"]

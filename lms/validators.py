import re

from rest_framework import serializers


def validate_video_link(value):
    pattern = re.compile("youtube.com")
    if not re.findall(pattern, value):
        raise serializers.ValidationError("Ссылка на сторонние образовательные платформы или личные сайты запрещена")

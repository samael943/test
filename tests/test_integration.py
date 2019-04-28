import pytest
import requests


base_url = "http://127.0.0.1:5000"


def test_get_method_reverse_string():
    r = requests.get(base_url + "/reverse-string/example")
    assert r.text == "elpmaxe"

def test_post_method_square():
    r = requests.post(base_url + "/square/123")
    assert r.text == "15129"

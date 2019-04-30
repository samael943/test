import pytest
import requests


base_url = "http://127.0.0.1:8081"


def test_get_method_reverse_string():
    r = requests.get(base_url + "/reverse-string/example")
    assert r.text == "elpmaxe"

def test_get_method_reverse_string_with_space():
    r = requests.get(base_url + "/reverse-string/space%20space")
    assert r.text == "ecaps ecaps"

def test_get_method_reverse_string_cyrillic():
    r = requests.get(base_url + "/reverse-string/тест")
    assert r.text == "тсет"

@pytest.mark.skip(reason="for some reason")
def test_get_method_reverse_string_spec_symbols_simple():
    r = requests.get(base_url + "/reverse-string/!@#$%^&*(),.")
    assert r.text == ".,)(*&^%$#@!"

def test_post_method_square():
    r = requests.post(base_url + "/square/123")
    assert r.text == "15129"

def test_post_method_square_starts_with_zero():
    r = requests.post(base_url + "/square/0123")
    assert r.text == "15129"

def test_post_method_square_with_minus():
    r = requests.post(base_url + "/square/-123")
    assert r.text == "15129"
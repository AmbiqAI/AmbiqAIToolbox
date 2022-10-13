"""
Unit tests for hello.py
"""

from change_me import hello


def test_hello(capfd):
    """unit test hello function"""
    hello.hello("me")

    out, _ = capfd.readouterr()
    assert out == "hello me\n"

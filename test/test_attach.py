
import pytest
from dataclasses import dataclass

from viagee import GMailURL


@dataclass
class Case:
    urlstr: str
    result: str

base_url = "mailto:joe@example.com?"

cases = (
    Case("attachment=foo", ["foo"]),
    Case("attach=foo", ["foo"]),
    Case("attach=foo&attach=bar", ["foo", "bar"]),
    Case("baz=baz&attach=foo&attach=bar", ["foo", "bar"]),
)


@pytest.mark.parametrize("case", cases)
def test_attachment(case):
    pass
    url = base_url + case.urlstr

    gmail_obj = GMailURL(url, "me@example.com")
    maildict = gmail_obj.mail_dict

    assert "attachment" not in maildict

    assert maildict["attach"] == case.result


def test_no_attachment():
    gmail_obj = GMailURL(base_url, "me@example.com")
    maildict = gmail_obj.mail_dict

    with pytest.raises(KeyError):
        maildict["attach"]

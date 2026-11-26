"""Checks for the mark book.

From the 12_testing folder:

    pytest
"""

import sys
from pathlib import Path

import pytest

# marks.py is one folder up, in 12_testing
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from marks import MarkBook


@pytest.fixture
def book():
    # a new Issath before every test
    return MarkBook("Issath")


def test_a_new_book_has_the_student_name(book):
    assert book.name == "Issath"
    assert book.marks == []


def test_total_adds_two_marks(book):
    book.add(40)
    book.add(60)
    assert book.total() == 100
    assert book.passed() is True


def test_total_adds_three_marks(book):
    book.add(20)
    book.add(30)
    book.add(50)
    assert book.total() == 100
    assert book.passed() is False


def test_one_mark_is_its_own_total(book):
    book.add(75)
    assert book.total() == 75
    assert book.passed() is True


def test_fifty_passes(book):
    book.add(50)
    assert book.passed() is True


def test_one_hundred_passes(book):
    book.add(100)
    assert book.passed() is True


def test_forty_nine_does_not_pass(book):
    book.add(49)
    assert book.passed() is False


def test_a_mark_above_100_raises(book):
    with pytest.raises(ValueError, match="a mark is from 0 to 100"):
        book.add(150)
    assert book.marks == []


def test_a_negative_mark_raises(book):
    with pytest.raises(ValueError, match="a mark is from 0 to 100"):
        book.add(-1)
    assert book.marks == []

"""Lessons and words kept from the early Credit & Debt unit. Do not edit the
lesson ids or step ids. Later scripts move some of these lessons into new units."""
import json, os

_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'preserved_lessons.json')
_DATA = json.load(open(_PATH, encoding='utf-8'))


def kept(lesson_id):
    return _DATA['lessons'][lesson_id]


def kept_term(term_id):
    return _DATA['terms'][term_id]

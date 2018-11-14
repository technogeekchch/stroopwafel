import asyncio
import json

import codecs
import os
import random
import re

from cloudbot import hook
from cloudbot.util import textgen

nick_re = re.compile("^[A-Za-z0-9_|.\-\]\[\{\}]*$", re.I)

def is_valid(target):
    """ Checks if a string is a valid IRC nick. """
    if nick_re.match(target):
        return True
    else:
        return True

@asyncio.coroutine
@hook.command
def present(text, action):
    """<user> - <method> a <detail>, <wrap> coloured wrapped present to <user> """
    user = text.strip()

    if not is_valid(user):
        return "I can't give a present to that user."

    size = random.choice(['small', 'little', 'huge', 'large', 'gigantic'])
    detail = random.choice(['heavy', 'light', 'wet'])
    wrap = random.choice(['violet', 'purple', 'pink','orange', 'red', 'green', 'blue', 'yellow','rainbow', 'red', 'green'])
    method = random.choice(['gives', 'throws', 'hands'])

    action("{} a {}, {} coloured wrapped present to {}!".format(method, detail, wrap, user))


@asyncio.coroutine
@hook.command
def pepernoten(text, action):
    """<user> - gives <user> a <size> amount of pepernoten!"""
    user = text.strip()

    if not is_valid(user):
        return "I can't give a pepernoten to that user."

    size = random.choice(['small', 'little', 'huge', 'large', 'gigantic'])

    action("gives {} a {} amount of pepernoten!".format(user, size))


@asyncio.coroutine
@hook.command
def snowball(text, action):
    """<user> - throws a <type> snowball at <user>!"""
    user = text.strip()

    if not is_valid(user):
        return "I can't throw snowballs at that user."

    type = random.choice(['small', 'little', 'wet', 'icey', 'large', 'gigantic'])

    action("throws a {} snowball at {}!".format(type, user))


@asyncio.coroutine
@hook.command
def hug(text, action):
    """<user> - gives <user> a cookie"""
    user = text.strip()

    if not is_valid(user):
        return "I can't give hugs to that user."

    hug = random.choice(['hug', 'cuddle'])
    type = random.choice(['friendly ', 'tight ', '', 'long ', 'super '])

    action("gives a {}{} to {}!".format(type, hug, user))

from typing import Any

import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def my_list(x):
    l = list()
    for i in range(101):
        if x:
            if i % 2 == 0:
                l.append(i)
        else:
            if i % 2 == 1:
                l.append(i)
    print(l)




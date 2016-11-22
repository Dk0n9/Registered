# coding: utf-8

import sys


class DBConnectionError(Exception):
    pass


class DBAuthenticatedError(Exception):
    pass


def printException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    print '[!] {filename} LINE {line} Error: {error}'.format(filename=filename, line=lineno, error=exc_obj)

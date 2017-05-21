# coding=utf-8

import os
from flask import render_template
from functools import wraps
from urllib.parse import urlparse, urljoin


def is_safe_url(host_url, target):
    ref_url = urlparse(host_url)
    test_url = urlparse(urljoin(host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def disable_it(yes=False):
    """关闭接口"""

    def wrapper(f):
        @wraps(f)
        def check(*args, **kwargs):
            if yes:
                return render_template('info_board.html', res={
                    'title': "status",
                    'info': "接口暂时关闭"
                })
            return f(*args, **kwargs)

        return check

    return wrapper


def get_file_mtime(path):
    try:
        st = os.stat(path)
        return st.st_mtime
    except OSError:
        return 0


# coding=utf-8

from flask.ext.admin import expose, AdminIndexView
from flask.ext.login import current_user


class IndexView(AdminIndexView):
    @expose("/")
    def index(self):
        res = {
            'info': '后台管理'
        }
        return self.render('admin/index.html', res=res)

    def is_accessible(self):
        return current_user.is_authenticated() and current_user.is_administrator()

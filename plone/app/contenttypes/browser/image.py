# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView


class RedirectToScale(BrowserView):

    def __call__(self):
        scale = self.__name__.split('image_')[-1]
        self.request.response.redirect('{0}/@@images/image/{1}'.format(
            self.context.absolute_url(), scale))

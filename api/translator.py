# -*- coding: utf-8 -*-
from util.settings import settings
from mstranslator import Translator

class Translation(object):

    def __init__(self):
        keys = settings.get_translation_conf()
        self.tw = Translator(keys['CLIENT_ID'],keys['CLIENT_SECRET'])

    def ja_to_tw(self,text):
        return self.tw.translate(text,'ja','zh-tw')

translation = Translation()

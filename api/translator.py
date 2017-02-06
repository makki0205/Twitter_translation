# -*- coding: utf-8 -*-
from util.settings import settings
from mstranslator import Translator
from util.logging import logger

class Translation(object):

    def __init__(self):
        keys = settings.get_translation_conf()
        self.tw = Translator(keys['CLIENT_ID'],keys['CLIENT_SECRET'])

    def ja_to_tw(self,text):
        try:
            return self.tw.translate(text,'ja','zh-tw')
        except Exception as e:
            logger.info("翻訳エラー")
            return ""

translation = Translation()

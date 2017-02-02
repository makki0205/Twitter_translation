# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser

_directory_path = os.path.abspath(os.path.dirname(__file__))
_conf_path = "{0}/../settings.conf".format(_directory_path)


def _load_conf_file(conf_file_path) -> ConfigParser:
    config = ConfigParser()
    config.read(conf_file_path, encoding='utf-8')
    return config


class Settings(object):
    """環境依存の設定を保持するクラス"""

    _twtter = "twtter"

    def __init__(self):
        self.config_parser = _load_conf_file(_conf_path)

    def get_twtter_conf(self):
        return {
            'CONSUMER_KEY':self.config_parser.get(Settings._twtter, "CONSUMER_KEY"),
            'CONSUMER_SECRET':self.config_parser.get(Settings._twtter, "CONSUMER_SECRET"),
            'ACCESS_TOKEN':self.config_parser.get(Settings._twtter, "ACCESS_TOKEN"),
            'ACCESS_SECRET':self.config_parser.get(Settings._twtter, "ACCESS_SECRET"),
        }
        
settings = Settings()

# -*- coding: utf-8 -*-
from lxml import etree

import json
import re

article_list_re = re.compile('var msgList = (.*?)}}]};')

class Parser:

    def __init__(self):
        pass

    @classmethod
    def parse_gzh(cls, text):
        page = etree.HTML(text);
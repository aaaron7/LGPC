# author:aaron
# filename:db_movie_rule.py
# date: "2021-02-08"

import string
import sys
import json
import os
from os import listdir
from os.path import isfile, join
import requests
import time
import random
import json
import urllib
from LGPC.parser import rule
from LGPC.utils import status
from bs4 import BeautifulSoup

class DBMovieRule(rule.Rule):
    def __init__(self):
        super().__init__()

    def process(self, context: rule.RuleContext, config: rule.RuleConfig) -> status.Status:
        packet = context.get_input(0)
        if not packet.can_get_type(type(string)):
            return status.ParameterInvalidStatus()
        page_source = packet.payload()
        print(page_source)
        # if page_source
        return status.OkStatus()

if __name__ == "__main__":
    pass

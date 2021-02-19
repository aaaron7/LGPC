# author:aaron
# filename:parser.py
# date: "2021-02-05"

import sys
import json
import os
from os import listdir, stat
from os.path import isfile, join
import requests
import time
import random
import json
import urllib
from bs4 import BeautifulSoup
from LGPC.downloader import downloader
from LGPC.utils import packet, status
from LGPC.parser import rule
from LGPC.parser.rules import  db_movie_rule 

class Parser:
    """
    mediapipe-like dag architure.

    why don't we just use simple gpuimage pipeline? because i want a Rule can receive and produce multiply inputs and outputs.
    """

    def __init__(self) -> None:
        self.rules = []
        self.context = rule.RuleContext()

    def add_rule(self, rule : rule.Rule, rule_config: rule.RuleConfig) -> status.Status:
        self.rules.append((rule, rule_config))

    def remove_rule(self, rule) -> status.Status:
        self.rules = [x for x in self.rules if x[0] != rule]

    def send_packet(self, packet, stream_name) -> status.Status:
        self.context.add_packet(packet, stream_name)
        pass 

    def notify_rule_run(self, input_stream_name) -> status.Status:
        for rule,config in self.rules:
            if config.input_names.contains(input_stream_name):
                rule.process(self.context, config)

        self.context.pop_packet(input_stream_name)
    
    
    

if __name__ == "__main__":

    p = Parser()
    db_rule = db_movie_rule.DBMovieRule()
    rule_config = rule.RuleConfig("db_movie", ["page_source"],["movies"])
    p.add_rule(rule, rule_config)


    def get_content(source):
        p.send_packet(packet.Packet(source), "page_source")

    ld = downloader.SeleDownloader()
    test_url = "https://movie.douban.com/tv/#!type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=recommend&page_limit=20&page_start=0"
    req = downloader.Request(test_url, get_content)
    ld.start_download(req)
    pass

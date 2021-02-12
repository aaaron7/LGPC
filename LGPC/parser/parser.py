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


    pass

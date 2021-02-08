# author:aaron
# filename:parser.py
# date: "2021-02-05"

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
from bs4 import BeautifulSoup
from LGPC.downloader import downloader
from LGPC.utils import packet
class RuleContext:
    def __init__(self):
        self.streams = {}
        pass
    
    def add_packet(packet, name):
        if self.streams[name] is None:
            self.streams[name] = []
        self.streams[name].append(packet)
        

    def get_input(self, index):
        pass

    def write_output(self, index, packet):
        pass

class Rule:
    def __init__(self, input_names, output_names):
        self.input_names = input_names
        self.output_names = output_names

    @staticmethod
    def name():
        return "DefaultParserRule"

    def prepare(self, rule_context):
        pass

    def process(self, rule_context):
        pass

    def close(self, rule_context):
        pass

class Parser:
    """
    GPUImage-like rules execution engine. 

    Why not use mediapipe-like DAG arch? 
    Config-driven may bring additional work, pros side is it looks much clear along with some of complex graph structure, but we don't have such scenario in this project. 

    So, we simply use GPUImage style pipeline, and make the pipeline building process more readable by functional techniques.

    """

    def __init__(self):
        self.rules = []
        self.context = RuleContext()

    def add_rule(self, rule):
        self.rules.append(rule)

    def remove_rule(self, rule):
        self.rules.remove(rule)

    def send_packet(self, packet, name):
        self.context.add_packet(packet, name)
        pass 
    
    

if __name__ == "__main__":
    pass

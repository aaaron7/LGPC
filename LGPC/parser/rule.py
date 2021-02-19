# author:aaron
# filename:rule.py
# date: "2021-02-08"

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
from LGPC.utils import packet,status

class RuleContext:
    def __init__(self) -> None:
        self.streams = {}
        pass
    
    def add_packet(self, packet, stream_name) -> None:
        if stream_name not in self.streams:
            self.streams[stream_name] = []
        self.streams[stream_name].append(packet)
    
    def pop_packet(self, stream_name) -> None:
        self.streams[stream_name].pop()
    
    def get_input(self , index : int) -> packet.Packet:

        pass

    def write_output(self, index : int, packet : packet.Packet) -> status.Status:
        pass

class RuleConfig:
    def __init__(self,name, input_names, output_names) -> None:
        self.name = name
        self.input_names = input_names
        self.output_names = output_names
        pass

class Rule:
    """
    All rules are using immediate input policy by default. it means that process will be called any of input is ready.
    """
    def __init__(self):
        pass

    def prepare(self, context : RuleContext, config : RuleConfig) -> status.Status:
        pass

    def process(self, context : RuleContext, config : RuleConfig) -> status.Status:
        pass

    def close(self, context : RuleContext, config : RuleConfig) -> status.Status:
        pass

if __name__ == "__main__":
    pass

# author:aaron
# filename:packet.py
# date: "2021-02-06"

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

class Packet:
    def __init__(self, obj = None):
        self.payload = obj
    
    def can_get_type(self, type_i):
        return type(self.payload) is type_i
        

if __name__ == "__main__":
    pass

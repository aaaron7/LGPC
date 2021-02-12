# author:aaron
# filename:downloader.py
# date: "2021-01-31"

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
import threading
from selenium import webdriver
from LGPC.utils import status
from fn import F,_

class Downloader:
    def __init__(self):
        pass

    def start_download(self, request):
        pass

class SeleDownloader(Downloader): 
    def __init__(self): 
        pass

    def start_download(self, request):
        brow = webdriver.Chrome()
        brow.get(request.url)
        task = threading.Timer(request.wait_time, request.completion, (brow.page_source,))
        task.start()
    
        
    
class Request:
    def __init__(self, url, completion, wait_time = 2.0):
        self.url = url
        self.status = status.Status()
        self.completion = completion
        self.wait_time = wait_time

def get_content(source):
    print(source.find("终极笔记"))        

if __name__ == "__main__":
    print("Hello")
    test_url = "https://movie.douban.com/tv/#!type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=recommend&page_limit=20&page_start=0"
    request = Request(test_url, get_content)
    downloader = SeleDownloader()
    downloader.start_download(request)
    input("prompt……")
    pass


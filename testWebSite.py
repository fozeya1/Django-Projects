#!/usr/bin/env python

import os
import sys
import django

from django.test.utils import setup_test_environment
from django.test import Client
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print("Start tag:", tag)
        for attr in attrs:
            if 'value' in attr:
                print("     attr:", attr)
        return
        
    def handle_endtag(self, tag):
        #print("End tag  :", tag)
        return

    def handle_data(self, data):
        data = data.encode('ascii', 'ignore').decode('ascii')
        data = data.replace("\n", '').strip()
        if data:
            print("Data     :", data) 

    def handle_comment(self, data):
        #print("Comment  :", data)
        return


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wgt_site.settings")
    django.setup()
    setup_test_environment()
    client = Client()
    client.login(username='wgt_admin', password='golftour')
    response = client.get (sys.argv[1])
    print(response)
    parser = MyHTMLParser()
    parser.feed (str (response.content, "UTF-8"))
    parser.close() 

#main
main()    
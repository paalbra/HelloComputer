#!/usr/bin/env python

import ConfigParser
import os
import urllib
import urllib2

script_dir = os.path.dirname(os.path.realpath(__file__)) 
config_path = os.path.join(script_dir, "hello-server.ini")

config = ConfigParser.RawConfigParser()
config.read(config_path)

url = config.get("HelloServer", "url")
computer_name = config.get("HelloServer", "computer_name")
secret = config.get("HelloServer", "secret")

print url, computer_name, secret 

data = urllib.urlencode({"computer_name": computer_name, "secret": secret})

result = urllib2.urlopen(url, data)
response = result.read()

print response

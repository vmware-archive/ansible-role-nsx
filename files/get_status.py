#!/usr/bin/env python

import sys
from sys import argv

script, in_file = argv

stat = True

for line in open(in_file):
	if "Success" in line:
		print "Success"
		stat = False
	if "Failure" in line:
		print "Failure"
		stat = False

if stat:
	print "Waiting"

#!/usr/bin/python
import os
import sys
import csv
from datetime import datetime
import time
from elasticsearch import Elasticsearch

def test():
	#run speedtest
	#print 'running test'
	a = os.popen("python /bin/speedtest-cli --simple").read()
	#print 'ran'
	lines = a.split('\n')
	#print a
	ts = time.time()
	date = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
	#if speedtest could not connecto, set the speeds to 0
	if "Could not" in a:
		p = 100
		d = 0
		u = 0
	#extract the values for ping down and up
	else:
		p = lines[0][6:11]
		d = lines[1][10:14]
		u = lines[2][8:12]
	#print date, p, d, u

	#write the data to ES
	es = Elasticsearch(["localhost"])
	doc = {
		'@timestamp': date,
		'ping': float(p),
		'upload': float(u)*1048576,
		'download': float(d)*1048576,
	}
	res = es.index(index="speedcheck", doc_type="check", body=doc)
	#print(res['created'])

if __name__ == '__main__':
    test()
    #print 'completed'

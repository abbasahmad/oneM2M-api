#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import os
from socket import error
from xml.dom.minidom import parse, parseString
import sys

PORT = 6000

class myHandler(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()

	def do_POST(self):
		self._set_headers()
		content_len = int(self.headers['Content-Length'])
		post_body = self.rfile.read(content_len)

		dom2 = parseString(post_body)
		print(dom2.toxml())

try :
	httpd = socketserver.TCPServer(('',PORT),myHandler)
	print("Serving at port ",PORT)
	httpd.serve_forever()
except error as e:
		print(e)


#!/usr/bin/python3
import http.server

server_address = ("", 8002)
handler_class = http.server.CGIHTTPRequestHandler
server = http.server.HTTPServer(server_address, handler_class)
server.serve_forever()

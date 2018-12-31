#!/usr/bin/python
import os.path
p = "curl 'http://localhost:8002/cgi-bin/GPIO21onoff.py?switch=on'"
req = os.system(p)

print "Content-type: text/html\n"
print "<html><body>"
print "On"
print "</body></html>"

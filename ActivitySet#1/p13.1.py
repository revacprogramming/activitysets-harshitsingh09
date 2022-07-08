# Network Programming
# https://www.py4e.com/lessons/network
'''
Exploring the HyperText Transport Protocol

You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

http://data.pr4e.org/intro-short.txt
There are three ways that you might retrieve this web page and look at the response headers:

Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the values are different for each URL.
Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
Enter the header values in each of the fields below and press "Submit".
'''

from socket import *

soc = socket(AF_INET,SOCK_STREAM)
soc.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
soc.send(cmd)

while True:
   data = soc.recv(512)
   if(len(data)<1):
      break
   print(data.decode())
soc.close()
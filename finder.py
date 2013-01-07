#!/usr/bin/python

import re
import socket
import sys
import time

PORT = 43
SERVER = 'whois.nic.io'
WORD_FILE = '/usr/share/dict/words'

def whois(query) :
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    try:
        s.connect((SERVER , 43))
    except socket.error, msg:
        print 'Socket connection error ' + msg
        sys.exit();
    s.send(query + '\r\n')	
    msg = ''
    while len(msg) < 1000:
        chunk = s.recv(100)
        if chunk == '':
            break
        msg = msg + chunk
    return msg	
    s.close()
    return msg

# Check if available 
def parse_response(resp):
    expr = r'Available'
    found = re.search(expr, resp)
    if found:
        return True
    return False
        
def search(domain):
    result = whois(domain)
    return result.splitlines()[0]

def make_full_domain(word):
    full_domain = "%s.io" % (word)
    return full_domain.lower()

def word_starts_with(word, letter):
    return word[0] == letter

# Save the search result to disk
def save_result(domain, letter):
    file_name = "%s.txt" % letter
    with open(file_name, "a") as f:
        f.write(domain + '\n')

def main(word_file, letter='a'):
    try:
      with open(word_file, 'r') as file:
          for line in file:
              if line[0] is letter:
                  word = line.strip()
                  if (len(word) > 4):
                      domain = make_full_domain(word)
                      try:
                        response = parse_response(search(domain))
                        if response: 
                            print "Found domain %s" % (domain)
                            save_result(domain, letter)
                      except: pass

    except KeyboardInterrupt:
        sys.exit(1)

if __name__ == '__main__':
    if len (sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        sys.exit('Usage: python finder.py word_file letter')


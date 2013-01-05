#!/usr/bin/python

import socket, sys

PORT = 43
REFERER = 'whois.nic.io'

def whois(server , query) :
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    try:
        s.connect((server , 43))
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

def parse_response(resp):
    expr = r'Available'
    found = re.search(expr, resp)
    if found:
        return True
    return False
        
def search(domain):
    result = whois(REFERER, domain)
    return result.splitlines()[0]

def make_full_domain(word):
    return "%s.io" % (word)

def run_search():
    results = { }
    with open('words.txt', 'r') as file:
        for line in file:
            domain = make_full_domain(line.strip())
            print domain
            response = parse_response(search(domain))
            if response:
                print "Found domain %s" % (domain)
            else:
                print "Domain %s Not available" % (domain)
        
        

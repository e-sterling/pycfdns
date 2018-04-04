# pycfdns
A simple Python wrapper for the Cloudflare DNS over HTTP service, leverages 1.1.1.1 to provide DNS resolution over HTTPS

## Description
Provides a function to query the Cloudflare DNS over HTTPS service, performs type validation before submitting query and returns answer as a dict

## Example
```
>>> from pycfdns import *
>>> c = pycfdns()
>>> c.query('www.google.co.uk','AAAA')
{u'Status': 0, u'AD': False, u'Question': [{u'type': 28, u'name': u'google.com.'}], u'CD': False, u'RD': True, u'RA': True, u'Answer': [{u'data': u'2a00:1450:4009:803::200e', u'type': 28, u'name': u'google.com.', u'TTL': 29}], 'elapsed': 318.507, u'TC': False}
>>> resp = c.query('google.co.uk', 'NS')
ns2.google.com.
ns3.google.com.
ns4.google.com.
>>> for r in resp['Answer']:
...     print r['data']
... 
ns1.google.com.
ns2.google.com.
ns3.google.com.
ns4.google.com.
>>>
```

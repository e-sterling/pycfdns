#!/usr/bin/env python
import requests
import json

class InvalidTyp(Exception):
   """Raised when the DNS record type is invalid"""
   pass

class TypNotSupported(Exception):
    """Raised when an unsupported record type is passed (ANY, 256)"""
    pass

class pycfdns:

    types = ['A','AAAA','AFSDB','APL','CAA','CDNSKEY','CDS','CERT','CNAME',
        'DHCID','DLV','DNAME','DNSKEY','DS','HIP','IPSECKEY','KEY','KX',
        'LOC','MX','NAPTR','NS','NSEC','NSEC3','NSEC3PARAM','OPENPGPKEY',
        'PTR','RP','RRSIG','SIG','SOA','SRV','SSHFP','TA','TKEY','TLSA','TSIG','TXT','URI',
        '1','28','18','42','257','60','59','37','5','49','32769','39','48','43','55','45',
        '25','36','29','15','35','2','47','50','51','61','12','17','46','24','6','33','44',
        '32768','249','52','250','16','256']

    def query(self, name, typ='A'):

        if isinstance(typ, (int, long, float)): typ = str(typ)
        typ = typ.upper()
        if typ == 'ANY' or typ == '256':
            raise TypNotSupported("Record type not supported: {0}".format(typ))
        elif typ not in self.types:
            raise InvalidTyp("Invalid record type: {0}".format(typ))
        else:
            params = {
                'ct' : 'application/dns-json',
                'type' : typ,
                'name' : name
            }
            r = requests.get("https://cloudflare-dns.com/dns-query", params=params)
            ret = r.json()
            ret.update({"elapsed":(float(r.elapsed.microseconds) / 1000)})
            return ret

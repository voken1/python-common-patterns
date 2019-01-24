#!/usr/bin/env python
# encoding: utf-8

import common_patterns

print(common_patterns.is_public_ip('8.8.8.8'))
print(common_patterns.find_asn('This is a text sample with AS1234 for test'))
print(common_patterns.findall_ssr_urls('ssr://aaaaadd-BB_3321aZ'))

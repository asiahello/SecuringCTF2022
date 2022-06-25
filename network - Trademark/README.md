# Trademark - 120 pts

> Our law deparment already prepared the papers for trademark registration. Soon, we will be able to use the CursedNova™! We need to hurry and register the proper domains. We already registered cursednova.PL, but there will be many more! TLDr: go for it!

We have a description and a hint: `If you found 2 out of 3, try 4.2.2.1.` given. 

You can notice TLDR written TLDr - TLD stands for Top Level Domain. Everything looks like wee need to find 3 domains. 
<!-- First, I set my DNS to 4.2.2.1 -->
I used `godaddy.com` to search for reserved `cursednova domains` and found three which match the plot:
- `cursednova.space`
- `cursednova.fun`
- `cursednova.click`
All created 6th of May by SecuRing.

As there was nothing served on these domains (`nmap` shows all ports are closed), I used `dnsdumpster.com` to search for any dns records and... found TXR records:
- "\"You are on the right track!\" - l__k __r __e __b__m__n_"
- "\"You are on the right track!\" - _o__ f_ t__ s__d__a__s"

`lok for the subdomains`, ok but how? 
Tried many ways for domain enumerations: `dig`, `nslookup`, some online webscanners gave no results.
Finally found a `subbrute` script: [subbrute](https://github.com/TheRook/subbrute) which needed to be run few times for each domain to finally found a desired subdomain:
- `portal.cursednova.space`
- `cursednova.fun` - found nothing
- `gatekeeper.cursednova.click` 

Tried again `dnsdumpster.com` to check TXT records but no luck, 

CURSEDNOVA{}

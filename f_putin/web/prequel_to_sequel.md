page is including file
LFI to show /etc/passwd
as is php can try view page source by encoding page as base64 https://medium.com/@nyomanpradipta120/local-file-inclusion-vulnerability-cfd9e62d12cb

php://filter/convert.base64-encode/resource=wc.php

looking at page can see some info

checked robots.txt = another page which looks interesting checkpass.php

decoded that page and found the password for a cookie password on / page

set cookie password to equals secret password, loaded up secret page with wordcount functionality

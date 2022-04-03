# Forensics

## PDFCrypt

[<img src="img/encrypted_pdf_chall.png"
  style="width: 600px;"/>](img/encrypted_pdf_chall.png)

I downloaded the PDF and attempted to open it.  It asked for a password. 

I generated a hash using pdf2john and then used john with rockyou.txt to brute force the password for the pdf.

[<img src="img/encrypted_pdf.png"
  style="width: 800px;"/>](img/encrypted_pdf.png)

Upon opening the PDF you can see the flag.

[<img src="img/encrypted_pdf_sol.png"
  style="width: 800px;"/>](img/encrypted_pdf_sol.png)


## The Hills are alive!

[<img src="img/the_hills_are_alive_chall.png"
  style="width: 800px;"/>](img/the_hills_are_alive.png)

All that is provided is an image which is .HEIC format. I was not able to open it. 

I found a tool online which allowed me to convert the image into a JPG

[<img src="img/the_hills_are_alive_convert.png"
  style="width: 800px;"/>](img/the_hills_are_alive_convert.png)

[<img src="img/IMG_3526.jpg"
  style="width: 800px;"/>](img/IMG_3526.jpg)

After putting the image through a google image reverse search I didn't really find much.  I looked closely at the photo and noticed that there was an arched railway bridge to the left of the photo which looked quite unique.  I did a quick google search to see if I could find something.  I used York too as I knew the creators of the CTF were based in that area.

[<img src="img/the_hills_google.png"
  style="width: 800px;"/>](img/the_hills_google.png)

The first image of `Ribblehead Viaduct` looked promising. So I went to google maps to take a look. 

[<img src="img/the_hills_google2.png"
  style="width: 800px;"/>](img/the_hills_google2.png)

So I was sure this could be it, but the challenge asked for the hill the photo was taken from. I couldn't see anything on google maps so one more google search was required to get the flag.

[<img src="img/the_hills_google3.png"
  style="width: 800px;"/>](img/the_hills_google3.png)

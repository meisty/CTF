# Web Challenge - Cafe

Challenge Description:
--------------------------

```
You can enjoy this cafe :)

upload text, youtube, ...
```

[<img src="images/challenge.png"
  style="width: 800px;"/>](images/challenge.png)

With a file to zip file to download.  

I downloaded the file and then started to look at the website.  

[<img src="images/home.png"
  style="width: 800px;"/>](images/home.png)

I registered an account and tried to acquire a cookie from an admin who may be logging in and looking at the page.  This did not work.  

[<img src="images/my_user.png"
  style="width: 800px;"/>](images/my_user.png)

I then checked the zip file I had downloaded.  Unzipped it and had a read through some of the files.  

What caught my interest in the `bot.py` file was potential admin credentials.  

[<img src="images/admin_creds.png"
  style="width: 800px;"/>](images/admin_creds.png)

I tried those on the website and sure enough I was logged in.

[<img src="images/admin_home.png"
  style="width: 800px;"/>](images/admin_home.png)  

Looking at the file `db.sql` I could see the flag would be stored in a post entitled `flag` so I viewed the first post with this and found the flag.

[<img src="images/flag_location.png"
  style="width: 800px;"/>](images/flag_location.png)

[<img src="images/flag.png"
  style="width: 800px;"/>](images/flag.png)
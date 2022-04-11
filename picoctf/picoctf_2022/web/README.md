# PicoCTF 2022

## Web challenges

### Includes

[<img src="img/includes_challenge.png"
  style="width: 800px;"/>](img/includes_challenge.png)

This challenge hinted at the flag being present in some included files.  I had a hunch this could be in a javascript file or CSS and found that half the flag was included in both of these included files

[<img src="img/includes_source.png"
  style="width: 800px;"/>](img/includes_source.png)

[<img src="img/includes_css.png"
  style="width: 800px;"/>](img/includes_css.png)

[<img src="img/includes_js.png"
  style="width: 800px;"/>](img/includes_js.png)

### SQL direct

[<img src="img/sql_direct_challenge.png"
  style="width: 800px;"/>](img/sql_direct_challenge.png)

After connecting to the postgres instance and having a look around I found the flags table.  After dumping all the information in that table the flag was visible. 

[<img src="img/psql_table.png"
  style="width: 800px;"/>](img/psql_table.png)

### Forbidden Paths

[<img src="img/forbidden_paths_chall.png"
  style="width: 800px;"/>](img/forbidden_paths_chall.png)

Looking at the page and the title it looks like its going to be path traversal to read the flag. 

[<img src="img/forbidden_paths_sol.png"
  style="width: 800px;"/>](img/forbidden_paths_sol.png)

`../../../../../../../flag.txt`

[<img src="img/forbidden_paths_ans.png"
  style="width: 800px;"/>](img/forbidden_paths_ans.png)
  
### Local Authority

[<img src="img/local_authority_chall.png"
  style="width: 800px;"/>](img/local_authority_chall.png)

My initial thoughts for this challenge was that it was going to be a SQL injection challenge.  Tried a few payloads and got nowhere.  

[<img src="img/local_authority_page.png"
  style="width: 800px;"/>](img/local_authority_page.png)
  
So I thought I would take a look at the source code in case there was anything interesting. 

[<img src="img/local_authority_source.png"
  style="width: 800px;"/>](img/local_authority_source.png)
  
[<img src="img/local_authority_credentials.png"
  style="width: 800px;"/>](img/local_authority_credentials.png)

And there we have it, the credentials we need to login.  Once logged in the flag is provided to us. 

[<img src="img/local_authority_ans.png"
  style="width: 800px;"/>](img/local_authority_ans.png)
  
### Roboto Sans

[<img src="img/roboto_sans_chall.png"
  style="width: 800px;"/>](img/roboto_sans_chall.png)
  
With this challenge I guessed it could be something to do with the robots.txt file which things are hidden in during the usual CTFs. 

[<img src="img/roboto_sans_robots.png"
  style="width: 800px;"/>](img/roboto_sans_robots.png)
  
Looks like base64.  Time to decode it

`echo <base64_string> | base64 -d`

[<img src="img/roboto_sans_base64.png"
  style="width: 800px;"/>](img/roboto_sans_base64.png)
  
Another hidden file.  When taking a look at the hidden file I found the flag.

[<img src="img/roboto_sans_ans.png"
  style="width: 800px;"/>](img/roboto_sans_ans.png)
  
### SQL Lite

[<img src="img/sql_lite_chall.png"
  style="width: 800px;"/>](img/sql_lite_chall.png)
  
So this time, this has to be a SQL injection challenge right?


[<img src="img/sql_lite_sol.png"
  style="width: 800px;"/>](img/sql_lite_sol.png)
  
[<img src="img/sql_lite_answer_page.png"
  style="width: 800px;"/>](img/sql_lite_answer_page.png)
  
Yup we are in.  But no flag? What gives?  Sneaky.  Looks like it may be hidden, lets check the source code. 

[<img src="img/sql_lite_answer_source.png"
  style="width: 800px;"/>](img/sql_lite_answer_source.png)

### Search Source

[<img src="img/search_source_chall.png"
  style="width: 800px;"/>](img/search_source_chall.png)
  
So this one made it sound like it was easy right?  Look through the source code and find the flag.  

I spent a lot longer than I should have on this one.  Manually searched the source code and couldn't see anything.  Eventually realised I could just download the source code and then use grep to look through it a lot quicker. 

[<img src="img/search_source_ans.png"
  style="width: 800px;"/>](img/search_source_ans.png)

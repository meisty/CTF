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
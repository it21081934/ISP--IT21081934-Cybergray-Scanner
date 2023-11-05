from contextlib import redirect_stderr
import os
import sys
import webbrowser
from urllib.request import urlopen


print('\n ------------------- [Cybergray Clickjacking Tester] --------------------')
print('\n[+] Description: This tool can verify if web page is vulnerable to clickjacking !!!')
print('\n ----------------- ------------------------------- -----------------')

url = input("Target Url (with https://): ")


def check(url):
    ''' check given URL is vulnerable or not '''

    try:
        if "http" not in url:
            url = "http://" + url

        data = urlopen(url, timeout=3)
        headers = data.info()

        if not "X-Frame-Options" in headers:
            return False
        if not "Content-Security-Policy" in headers:
            return False

    except:
        return True


html = '''
<html>
	<head>
		<title>clickjack</title>
		<style>
		body {
 		 background-color: black;
        align-items: center;
		}

		h1 {
		font-size: 50px;
		font-weight: 600;
		color: #fdfdfe;
		text-shadow: 0px 0px 5px #b393d3, 0px 0px 10px #b393d3, 0px 0px 10px #b393d3,
			0px 0px 20px #b393d3;
        text-align: center;
		}
        h2 {
        font-size: 40px;
		font-weight: 600;
        color: #b393d3;
        }
        h3 {
            color: antiquewhite;
            font-size: 22pt;
        }
		</style>
	</head>

	<body>
		<h1>CLICKJACKING TEST RESULTS</h1>
        <h2 style="text-align: center;">Cybergray Clickjacking Tester</h2>
        <h3 style="text-align: center;">Kulika Padmika</h3>
        <hr>
		<h3>Target: <a href="%s">%s</a></h3>
		<h3>If you see the target website rendered below, it is <font color="red">VULNERABLE !!!</font>.</h3>
		<h3>If you can not see the target website rendered below, it is <font color="green">NOT VULNERABLE</font>.</h3>
        <hr> <br>
        <center>
		<iframe width="1400" height="600" src="%s"></iframe>
        </center>
		<iframe style="position: absolute; left: 200px; top: 600px; opacity: 0.8; background: AliceBlue; font-weight: bold;" src="cj-attacker.html"></iframe>
	</body>
</html>
''' % (url, url, url)

html2 = '''
<html>
	<div style="opacity: 1.0; left: 10px; top: 50px; background: PapayaWhip; font-weight: bold;">
		<center><a href="solutions.html" target="_blank">THIS IS AN EXAMPLE CLICKJACKING IFRAME AND LINK (-CLICK HERE FOR SOLUTIONS-)</a>
		<br>(Normally invisible)</center>
	</div>
</html>
'''

cjt = os.path.abspath('cj-target.html')
cja = os.path.abspath('cj-attacker.html')
localurl = 'file://' + cjt

with open(cjt, 'w') as t, open(cja, 'w') as a:
    t.write(html)
    a.write(html2)


webbrowser.open(localurl)
print(
    '\n --------------------- [Cybergray Clickjacking Tester] -----------------------')
print('\n[+] Test Complete!')
print("\n[+] Target URL : ", url, "\n")
site = url
status = check(site)

if status:
    print("[+] "+site.split('\n')[0] + " is \t" + " [ VULNERABLE !!! ] ")


elif not status:
    print("[-] "+site.split('\n')[0] + " is \t"+"[ NOT VULNERABLE :-) ]")
else:
    print('\n Program Error !!! Try again. \n')


print('\n[+] Thanks for using Cybergray Clickjacking Tester ;-) ')
print('\n ----------------- Created by Kulika Padmika ------------------')
print('\n')

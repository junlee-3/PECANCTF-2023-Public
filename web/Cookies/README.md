Views the html by right click > view source, there is a comment revealing test account credentials
Enter credentials test/test to log in and be directed to /home
View robots.txt - reveals a page called administrator.
Visit /administrator - this will state that only the administrator can access this page.
View cookie (varies by browser, following is for firefox): Right click > inspect > storage > cookies
Enter the cookie value into crackstation (or use any other method to crack the hash). This reveals that the cookie value is a sha256 hash of the string test, aka, their currently logged in username.
Replace cookie value with lowercase sha256 hash of the word 'administrator' - generate using linux command "echo -n 'administrator' | sha256sum" or web application such as <https://passwordsgenerator.net/sha256-hash-generator/>
Refresh /administrator to reveal cookie.

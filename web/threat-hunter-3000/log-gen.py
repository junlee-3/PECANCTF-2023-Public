import json
import sys
import random
from random import randint

# Globals
userList = [
    "adam", "jordan", "dave", "tristan", 
    "chris", "matt", "nihal", "lyndon", 
    "andrew", "megan", "joseph", "henry", 
    "ed", "shannon", "celeste"
]

groupList = [
    "Domain Users", "DHCP Guests", "Guests", "Users",
    "IOT", "Contract Users"
]

ipList = [
    "92.37.219.81", "86.66.137.225",
    "156.215.194.3", "80.118.110.81",
    "181.154.109.221", "45.121.107.173",
    "32.35.53.112", "157.71.53.68",
    "7.255.219.210", "4.239.236.140",
    "229.122.47.63", "100.5.24.85",
    "220.165.196.134", "140.177.207.78",
    "106.198.249.199", "149.6.248.138",
    "76.100.214.119", "12.167.236.83",
    "123.180.33.93", "58.222.38.180",
]

interIpList = [
    "10.0.0.114","10.0.0.80",
    "10.0.0.57","10.0.0.96",
    "10.0.0.168","10.0.0.158",
    "10.0.0.71","10.0.0.137",
    "10.0.0.197","10.0.0.196",
    "10.0.0.77","10.0.0.114",
    "10.0.0.121","10.0.0.157",
    "10.0.0.110","10.0.0.73",
    "10.0.0.67","10.0.0.53",
    "10.0.0.200","10.0.0.106"
]

websiteList = [
    "google.com", "about.me", "ask.com",
    "oracle.com", "java.com", "ory.sh", "microsoft.com",
    "facebook.com", "techcrunch.com", "nationalgeographic.com",
    "github.io", "instagram.com", "gnu.org", "distrowatch.com",
    "youtube.com"
]

websitePathList = [
    "/index.html", "/about.html", "/contact.html",
    "/admin.html", "/home.html", "/search.html",
    "/index.php", "/robots.txt", "/about-us.php",
    "/events", "/dashboard", "settings.php"
]

# Squid Proxy Traffic
class Squid:
    def __init__(self):
        self.ip = random.choice(interIpList)
        self.port = 443
        self.url = f"{random.choice(websiteList)}{random.choice(websitePathList)}"
        self.result = random.choice(["200", "404", "303"])
        self.user = random.choice(userList)

    def jsonify(self):
        return {
            "ip": self.ip,
            "port": self.port,
            "url": self.url,
            "result": self.result,
            "user": self.user
        }

# Squid Proxy Traffic
class Apache:
    def __init__(self):
        self.ip = random.choice(ipList)
        self.method = random.choice(["POST", "GET"])
        self.version = "HTTP/1.1"
        self.url = f"{random.choice(websitePathList)}"
        self.status = random.choice(["200", "404", "303"])

    def jsonify(self):
        return {
            "ip": self.ip,
            "method": self.method,
            "version": self.version,
            "url": self.url,
            "status": self.status
        }

# SSH
class SSH:
    def __init__(self):
        infoList = [
            "Invalid user admin", "Disconnected from invalid user", 
            "Connection closed", "Accepted publickey", "New session",
            "pam_unix(cron:session): session opened"
        ]

        self.ip = random.choice(ipList)
        self.port = 22
        self.hostname = "carnation"
        self.information = random.choice(infoList)
        self.user = random.choice(userList)
    
    def jsonify(self):
        return {
            "ip": self.ip,
            "port": self.port,
            "hostname": self.hostname,
            "user": self.user,
            "information": self.information
        }

# Windows Events
## 800 ##
class Powershell:
    def __init__(self, user):
        commandList = [
            "Set-ExecutionPolicy Unrestricted", "Get-Process MySQL | Stop-Process",
            "Invoke-WebRequest https://intranet/", "Test-Connection 1.1.1.1"
            "Get-Date -format F", "whoami",
            "Get-EventLog -LogName System -After '01/05/2022' -Before '01/06/2022'",
            "Get-Process | Export-Csv .\\Timesheets.csv"
        ]

        self.event = 800
        self.command = random.choice(commandList)
        self.user = user
        self.application = "powershell.exe"
    
    def jsonify(self):
        return {
            "event": self.event,
            "command": self.command,
            "user": self.user,
            "application": self.application
        }

## 4624 ##
class Login:
    def __init__(self, group, user):
        loginCategories = [2, 3, 7]
        loginMessages = ["Failed Login", "Successful Login"]

        self.event = 4624
        self.message = "Login/Logoff"
        self.group = group
        self.user = user
        # Login Type
        self.category = random.choice(loginCategories)
        # Successful login or not
        self.keyword = random.choice(loginMessages)

    def jsonify(self):
        return {
            "event": self.event,
            "message": "Login/Logoff",
            "user group": self.group,
            "account name": self.user,
            "logon type": self.category,
            "keywords": self.keyword
        }

## 4728 ##
class SecurityEnabled:
    def __init__(self, group, user):
        self.event = 4728
        self.group = group
        self.user = user

    def jsonify(self):
        return {
            "event": self.event,
            "user group": self.group,
            "account name": self.user,
        }

# Methods
def timeGen():
    day = randint(1, 30)
    day = str(day)
    if len(day) == 1:
        day = "0" + day

    hour = randint(0,23)
    if hour > 12:
        hour = hour - 12
        ampm = "PM"
    elif hour == 12:
        ampm = "PM"
    else:
        ampm = "AM"
    hour = str(hour)
    if len(hour) == 1:
        hour = "0" + hour

    minute = randint(0,59)
    minute = str(minute)
    if len(minute) == 1:
        minute = "0" + minute

    return(day + "/Sep/2022 " + hour+":"+minute+" "+ampm)

def write():
    pass

# Log Generators
def ftp(count, logName):
    pass


def apache(count, logName):
    logs = []

    for i in range(count):
        target = {"type": logName, "time": timeGen()}
        
        log = Apache()

        target["log"] = log.jsonify()
        logs.append(target)

    print(json.dumps(logs, indent=4))


def squid(count, logName):
    logs = []

    for i in range(count):
        target = {"type": logName, "time": timeGen()}
        
        log = Squid()

        target["log"] = log.jsonify()
        logs.append(target)

    print(json.dumps(logs, indent=4))


def ssh(count, logName):
    logs = []

    for i in range(count):
        target = {"type": logName, "time": timeGen()}
        
        log = SSH()

        target["log"] = log.jsonify()
        logs.append(target)

    print(json.dumps(logs, indent=4))


def windowsEvent(count, logType, logName):
    logs = []

    for i in range(count):
        target = {"type": logName, "time": timeGen()}
        
        ##############################
        if "login" == logType:
            log = Login(random.choice(groupList), random.choice(userList))

        elif "powershell" == logType:
            log = Powershell(random.choice(userList))

        elif "enum" == logType:
            log = SecurityEnabled("Administrators", random.choice(userList))
        ##############################

        target["log"] = log.jsonify()
        logs.append(target)

    print(json.dumps(logs, indent=4))


# MAIN
def main(args):
    if len(args) > 2:
        if args[1] == "ftp":
            ftp()

        elif args[1] == "ssh":
            ssh(int(args[2]), "SSH")

        elif args[1] == "windows":
            windowsEvent(int(args[2]), args[3], "Windows Event")

        elif args[1] == "squid":
            squid(int(args[2]), "Squid Proxy")

        elif args[1] == "apache":
            apache(int(args[2]), "Apache")

        else:
            print("Incorrect argument usage")
    else:
        print("No argument was specified")
        print("Example: python log-gen.py [ftp/ssh/windows/squid] [Number of Logs] OPTIONAL [Log Type]")

if __name__ == "__main__":
    main(sys.argv)


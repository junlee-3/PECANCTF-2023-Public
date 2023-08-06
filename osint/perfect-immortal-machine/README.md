# OSINT Challenge Writeup - Perfect Immortal Machine

Note: you will NOT need to actually visit these IPs or navigate to them.

Some will think of using Shodan (or a similar site) right away when they see IPs. Others may be lead toward Shodan with the hint in the challenge name.
If you Google 'perfect immortal machine' you will see this is a reference to the villain in the videogame System Shock. The name of the villain is Shodan.

The site you will use: https://www.shodan.io/dashboard

On this site, search each IP and view details to find the common trait.

![image](https://github.com/ECUComputingAndSecurity/PeCanCTF-2023/assets/87506849/91a8e7d3-740c-4cc2-8926-031a79ac8dd7)

These IPs are all tagged as a 'honeypot' somewhere on the pages listing their details. 

![image](https://github.com/ECUComputingAndSecurity/PeCanCTF-2023/assets/87506849/f08c6d7b-8caf-479a-9038-e3803c943e1b)

It may be a good opportunity to explain what a honeypot is to students who are unaware. A honeypot is a device that mimics a real one with vulnerabilities. This attracts attackers. Honeypots can be used for many reasons, including:
- Distract attackers away from your real systems
- Watch attackers and study their tactics
- Capture IPs of attackers to understand which IPs are being used maliciously
- Provide an early detection system so you know when you are under attack - often the honeypot will be attacked first as it is the easiest to break into

It may be possible to use sites apart from Shodan for this challenge, but I included the reference in the title as a heavy hint toward Shodan as I know the IPs are tagged as honeypots there.

The flag is pecan{honeypot}

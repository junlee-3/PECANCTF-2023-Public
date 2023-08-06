# OSINT chal writeup - Forward thinking

- Observe carefully: geographical features, buildings etc
- The only legible text is on a building straight ahead. If inspected closely, it reads "FWD"
- What/who is FWD? Google:
  ![image](https://github.com/ECUComputingAndSecurity/PeCanCTF-2023/assets/46239981/88fa70f9-c467-4f45-9094-70f9c42e661d)
- Great. The logo matches the building. Now we just need to locate that specific building
- Time for some more Googling. The placement of the logo is important; it narrows down some results. Singapore looks promising:
  ![image](https://github.com/ECUComputingAndSecurity/PeCanCTF-2023/assets/46239981/3fe14c15-7b94-4b3a-ad8a-5bf05da6e234)
- When we look for a FWD building in Singapore on Google maps (3D / globe view), this is the result:
  ![image](https://github.com/ECUComputingAndSecurity/PeCanCTF-2023/assets/46239981/4a6d9a7d-286e-4684-bd0f-78fd5ee58678)
- Strange. That doesn't look like our building. Let's backtrack a little:
  ![image](https://github.com/ECUComputingAndSecurity/PeCanCTF-2023/assets/46239981/730cb942-6fec-4c7d-b515-8b902ead3026)
- There are a couple results which match the challenge image better. They also reveal an address, [such as this article](https://www.mingtiandi.com/real-estate/finance/richard-lis-fwd-group-buying-50-stake-in-sg-office-building-for-424m/).
- Unfortunately, the Google maps globe view doesn't display the new logo yet. However, we know from the address and images that this is the correct building.
- We confirm by lining up the FWD building with other buildings present in the challenge image:
  ![image](https://github.com/ECUComputingAndSecurity/PeCanCTF-2023/assets/46239981/ca756879-0a79-4b2c-bbd2-68c1c9169544)
- The location is 'Ord Bridge, Singapore'. Thus, the flag is pecan{ord_bridge_singapore}

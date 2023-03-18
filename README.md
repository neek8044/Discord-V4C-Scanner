# Discord-V4C-Scanner
Based on V4C's repo on replit which is now deleted. Decoded script taken from [NoTextToSpeech](https://www.youtube.com/watch?v=nz1Bf3YaSWU) on YT

Just enchanced it a bit (or a lot?).

#### Update 18 March 2023

- main.py
  - Updated main.py to support v9 API
  - Added webhook customization. (Custom message, title, description)
  - Renamed savefile from nitro.codes to v4c_nitro_codes.txt since it is rarer for someone to have a file named after that (i should better just check the directory for file conflicts to not overwrite anything, i am going to update it soon)
- main_multiapi.py
  - Checks code links for API versions v6 to v9 to not miss any code which is unsupported by the latest API.
  - Drawbacks:
    - Strains your internet more since it has to do more requests for each code check.
    - Slower than the original

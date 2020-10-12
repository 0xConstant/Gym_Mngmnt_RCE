# Gym Management 1.0 RCE 

There is an unauthenticated file upload vulnerability in Gym Management 1.0 that allows anyone to upload files without a logged-in session, It can be used to upload malicious files that leads to RCE. 

The original exploit can be found [here](https://www.exploit-db.com/exploits/48506).

This exploit is just more readable than the original one.

### Reproduce
- Setup Gym Management 1.0 
- Install python3
- run poc.py




# Gym Management 1.0 RCE 

There is an unauthenticated file upload vulnerability in Gym Management 1.0 that allows anyone to upload files without a logged-in session, It can be used to upload malicious files that leads to RCE. 

The original exploit can be found [here](https://www.exploit-db.com/exploits/48506).

The original exploit was not very developer friendly so I decided to write my own version, my version does the same thing but here you don't need png magic bytes and a lot of other variables.

### Reproduce
- Setup Gym Management 1.0 
- Install python3
- run poc.py:
```
python3 poc.py
```




# NTLM Bruter
![NTLM](https://github.com/smaranchand/ntlm_bruter/blob/main/ntlm-bruter.png)

## NOTE: This fork uses a single list that contains `user:passwd` on each line instead of using separated users and password list.

NTLM Bruter is a simple tool that bruteforces the usernames/passwords against the application with HTTP NTLM Authentication.
The tool tries all possible combinations from ```usernames.txt``` and ```passwords.txt``` files to enumerate the correct set of credentials.


Usage: ```python3 ntlm.py [Target_URL] [AD_Domain_Name]```

Note: It is highly recommended to use your own wordlists.

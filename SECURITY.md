# Security Policy

## Reporting a Vulnerability

Submit a pull request, and either:
- a) fix the vuln, with comments explaining the issue and the proposed solution(mandatory) or,
- b) comment above the vuln, explaining the issue and the proposed solution(mandatory)

## Tested Vulnerabilities

| Name 					 | Tested           | Vulnerable                  |Notes	  |
| -----------------------|------------------|-----------------------------|-----------|
| SQL Injection 		 |:white_check_mark:|:negative_squared_cross_mark:|SQL commands are parametered|
<<<<<<< HEAD
| XSS 					 |:white_check_mark:|:negative_squared_cross_mark:|Browser(Mozilla) appears to automatically escape Dynamic content by using HTML entity encoding(' -> %23). In addition, a content security policy has been added in the Meta tag(but this breaks javascript)|
| Command Execution 	 |:x:|:negative_squared_cross_mark:|Sys is imported|
| Clickjacking 			 |:x:|:white_check_mark:|Trying to find a solution to having JS enabled but disabling iframes|
| XSRF 					 |:x:|||
| Directory Traversal 	 |:x:|||
| Reflected XSS 		 |:x:|||
| Dom-Based Xss 		 |:x:|||
| File Upload Vuln. 	 |:x:|||
| Broken Access Control  |:x:|||
| Open Redirects 		 |:x:|||
| Unencrypted Comm. 	 |:x:|||
| User Enumeration 		 |:x:|||
| Information Leakage    |:x:|||
| Password Mismanagement |:x:|||
| Privilege Escalation   |:x:|||
| Session Fixation 		 |:x:|||
| Weak Session IDS 		 |:x:|||
| XML Bombs 			 |:x:|||
| XML External Entities  |:x:|||
| DOS Attacks 			 |:x:|||
| Email Spoofing 		 |:x:|||
| Malvertising           |:x:|||
| Lax Security Settings  |:x:|||
| Toxic Dependencies     |:x:|||
| Logging and Monitoring |:x:|||
| Buffer Overflows 		 |:x:|||
=======
| XSS 					 |:white_check_mark:|:negative_squared_cross_mark:|Browser(Mozilla) appears to automatically escape Dynamic content by using HTML entity encoding|
| Command Execution 	 |:x:||||
| Clickjacking 			 |:x:||||
| XSRF 					 |:x:||||
| Directory Traversal 	 |:x:||||
| Reflected XSS 		 |:x:||||
| Dom-Based Xss 		 |:x:||||
| File Upload Vuln. 	 |:x:||||
| Broken Access Control  |:x:||||
| Open Redirects 		 |:x:||||
| Unencrypted Comm. 	 |:x:||||
| User Enumeration 		 |:x:||||
| Information Leakage    |:x:||||
| Password Mismanagement |:x:||||
| Privilege Escalation   |:x:||||
| Session Fixation 		 |:x:||||
| Weak Session IDS 		 |:x:||||
| XML Bombs 			 |:x:||||
| XML External Entities  |:x:||||
| DOS Attacks 			 |:x:||||
| Email Spoofing 		 |:x:||||
| Malvertising           |:x:||||
| Lax Security Settings  |:x:||||
| Toxic Dependencies     |:x:||||
| Logging and Monitoring |:x:||||
| Buffer Overflows 		 |:x:||||
>>>>>>> 9db346882baba559c0bef31765a4395d28b0dd92

# Writeup 3 - Operational Security and Social Engineering

Name: Philip Kwon
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Philip Kwon

## Assignment Writeup

### Part 1 (40 pts)

I would pretend to be an IT employee from the bank and call Elizabeth Moffet. I would use the information I gathered via OSINT to convince Elizabeth that I am in fact an IT employee from the bank. I would tell her that some hackers had comprised certain accounts, and that I was calling people whose accounts exhibited suspicious activity to help them change their passwords and PIN numbers immediately.

To convince Elizabeth of my pretext, I would first state that I need to confirm her identity. I would do this with statements and questions such as:

	"Hello, is this Elizabeth Moffet?"
	"Just for confirmation, your username is v0idcache correct?"
	"Your login password was 'linkinpark' corrent?"

Afterwards, I would go on to explain to Elizabeth that the system and a number of accounts had been compromised. As a result, I was changing the password and PIN of accounts exhibiting suspicious activity immediately by contacting the affected people over the phone. I would ask then ask her what new password and PIN number she would like to set up. After she gives me her new password and PIN, I would then tell her that we are going to set up some security questions in case of future breaches. For the security questions I would ask her:

	"What is your mother's maiden name?"
	"What is your city of birth?"
	"What was the name of your first pet?"

After setting up the security questions, I would tell her that we were still looking into the causes of the data breach. I would mention that certain web browsers would have security vulnerabilities, and then ask her what web browser she used. No matter what answer gives, I would then say that a security flaw had recently been discovered with respect to that web browser, and that she should use web browser [alternative web browser] at least for the next few weeks.

### Part 2 (60 pts)

1. Vulnerability - The robots.txt file and the /secret_directory

	The robots.txt file is publicly accessible. Therefore, I would make sure that secret information like confidential information and secret directories are not in the robots.txt file.

2. Vulnerability - Weak password

	The password used by Elizabeth Moffet was a weak, commonly used password. To prevent this, the system could require passwords to have a minimum number of characters, numbers, characters, symbols, lowercase letters, and uppercase letters. The system could then rate the password and only accept strong passwords. Furthermore, the system could require periodic password changes (i.e. users must change their password every 3 months)

3. Vulnerability - Exposed port

	I was able to gain access to v0idcache's account via the exposed port 1337. Therefore, open/exposed ports should be closed if they are unused or do not provide any required services.

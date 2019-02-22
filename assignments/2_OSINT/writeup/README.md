# Writeup 2 - OSINT

Name: Philip Kwon
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Philip Kwon

## Assignment Writeup

### Part 1 (45 pts)

1. 	Name: Elizabeth Moffet

	I used the username search tools from osintframework.com to search for "v0idcache." There I found v0idcache's Twitter, which had her name.

2. 	Workplace: 13/37th National Bank
	URL: 1337bank.money

	The information above was found on v0idache's Twitter page.

3.	Personal Information:
	Location: The Netherlands
	Job: Banking CEO
	Contacts:
		Dev0idcache (Twitter)
		fl1inch (pastebin)
		UMD CyberSecurity Club (Twitter)
	Workplace email: v0idcache@protonmail.com

	I found the information above by using the website osintframework.com and using the resources under "Username" > "Username Search Engines" to find v0idcache's Twitter account. There I found most of the information above. I found fl1inch in a copy/pasted conversation on pastebin after Googling "v0idcache." I found the workplace email on the website indicated on the Twitter account.

4.	IP Addresses:

142.93.136.81 - Server location: Canada
	I found the IP address by using dnstrails.com and dnsdumpster.com websites to lookup "1337bank.money." The location was provided by dnsdumpster.com.

5.	Flags
	
	Flag 1 - CMSC389R-{h1ding_fil3s_in_r0bots_L0L}

	I accessed the robots.txt file at 1337bank.money/robots.txt. There I found the secret_directory which had this flag.

	Flag 2 - CMSC378R-{h1d3_s3cret_g1ts}

	I ran the Kali nmap application on the IP address of the website, and the nmap discovered a git repository with the above flag.

6.	Open Ports

	Port 22 - ssh service
	Port 80 - http service
	Port 554 - tcpwrapped service - Real Time Streaming Protocol (RTSP) service
	Port 7070 - tcpwrapped service Real Time Streaming Protocol (RTSP) service
	Port 1337 - WASTE service

	I found the ports by running the Kali nmap application on the website's IP address. The application told me the services for ports 22 and 80. For ports 554 and 7070, the application merely told me that the ports provided "tcpwrapped" services. I looked in Wikipedia for the default services for ports 554 and 7070.

7.	OS: Ubuntu
	
	I ran the Kali nmap applciation on the website's IP address with the option to scan for the OS. The application was able to detect that the OS was Ubuntu. Also, connecting to the server via port 22 tells you what the OS is.
			
### Part 2 (75 pts)

username = v0idcache
password = linkinpark

CMSC389R-{brut3_f0rce_m4ster}

CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}

For the brute force program, I simply made a for loop. For each iteration of the for loop, I connected to the IP and port and then input v0idcache as the username and the next password in the wordlist. If the password did not fail, then I had the program print the password and then terminate.

Once I gained access to the account, the first place I looked was in the "home" folder which had a file named "flag.txt". I checked that file and found the first flag above. Previously, when I googled "v0idcache", I found a pastebin conversation where v0idcache specifically mentions the file "AB4300.txt". I found the file in "/home/files" and found the second flag above.

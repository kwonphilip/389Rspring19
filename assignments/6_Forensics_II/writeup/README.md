# Writeup 6 - Forensics

Name: Philip Kwon
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Philip Kwon

## Assignment Writeup

### Part 1 (45 Pts)

1. Warmup: what IP address has been attacked?

	The IP address attacked was 142.93.136.81.

2. What kind of assessment tool(s) were the attackers using against the victim machine? List the name(s) of the tool(s) as well.

	The attackers used a port mapper to find vulnerable ports. The name of the tool is nmap.

3. What are the hackers' IP addresses, and where are they connecting from?

	The hackers' IP addresses are: 159.203.113.181. The hackers are connecting fom New Jersey in the United States.

4. What port are they using to steal files on the server?

	The port they are using is Port 21.

5. Which file did they steal? What kind of file is it? Provide all metadata on the file. Specifically,

    a) What kind of file is it?

	A JPEG file named "find_me.jpeg" wa s stolen.

    b) Where was this photo taken? Provide a city, state and the name of the building in your answer.

	This photo was taken at: The Hand, Rambla General Artigas, 20100 Puna Del Este, Uruguay. The city is Punta Del Este. The county is La Pastora. The picture is of The Hand (or Los Dedos) on the beach.

    c) When was this photo taken? Provide a timestamp in your answer.

	The photo was taken Dec. 23, 2018 at 05:16:24 PM (more specifically 2018:12:23 17:16:24.002).

    d) What kind of camera took this photo?

	The photo was taken by a iPhone 8 camera.

    e) How high up was this photo taken? Provide an answer in meters.

	The photo was taken 4.5 meters below sea level.

6. Which file did the attackers leave on the server?

	The attackers left the file greetz.fpff on the server.

7. What is a countermeasure to prevent this kind of intrusion from happening again? Note: disabling the vulnerable service is *not* an option.

	One countermeasure would be a properly configured firewall. The firewall could filter closed ports by dropping any probes. Normally, when an Nmap SYN scan encounters a closed port, the target machine sends back a RST packet, and the Nmap is then able to determine the port's status in the timeframe of a single round trip. However, if the firewall filters the closed port by dropping any probes, then Nmap has to wait for the worst-case timeout before giving up. Nmap then has to make multiple retransmissions because Nmap doesn't know if the packet was dropped or not. If Nmap is scanning a large number of ports, then the firewall filters will significantly increase the amount of time that Nmap needs to scan all the ports. The time increase can be anywhere from hours to days depending on the number of ports being scanned. This could frustrate any attackers and prevent them from trying to Nmap scan for open ports.

### Part 2 (55 Pts)

The timestamp for when the file was generated is 1553660105, which March 27, 2019 4:15:05 AM.

The author is fl1nch.

Section 1
	type = SECTION_ASCII
	data = 'Hey you, keep looking :)'

Section 2
	type = SECTION_COORD
	data (52.336035, 4.880673)

Section 3
	type = SECTION_PNG
	data = CMSC389R-{w3lc0me_b@ck_fr0m_spr1ng_br3ak}

Section 4
	type = SECTION_ASCII
	data = CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R}

Section 5
	type = SECTION_ASCII
	data = Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=

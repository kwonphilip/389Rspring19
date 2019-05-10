# Crypto II Writeup

Name: Philip Kwon
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Philip Kwon

## Assignment Writeup

### Part 1 (40 Pts)

If you go to the website and click on one of the links for the exploits, the URL bar shows a query. I used SQL injection in the query to get the flag.

Before the SQL injection:

	1337bank.money:5000/item?id=0

After the SQL injection:

	1337bank.money:5000/item?id=admin' || 1=1 -- -

The SQL query looks up a table called 'items', and then goes to the 'id' column and returns all the rows associated with 'id'. The SQL injection passes in a tautology with the query. The injection also passes in block comments after the tautology so that everything after the tautology is ignored.

Flag - CMSC389R-{y0u_ar3_th3_SQ1_ninj@}

### Part 2 (60 Pts)

Level 1

Answer - <script>alert()</script>	Type the script in the search box

I looked up how to write an alert script. I tried writing the above script alert in the URL box, but that did nothing. Then I tried writing the script alert in the search box, which was the correct answer.

Level 2

Answer - \<img src="image.gif" onerror="javascript:alert()"></img>	Type into the box and share post.

I tried using the same script alert as before, but that did not produce the result I wanted. The hints said to use img and onerror, so I looked up img and onerror. From this I tried variations such as '<img src="image.gif" onerror=alert()></img>' and '<img src="image.gif" onerror=function(){alert();return true;}></img>'. Then I also looked up onerror popupalerts in img and refined my answer to '<img src="image.gif" onerror="javascript:alert()"></img>' which was the answer.

Level 3

Answer - 'onerror="javascript:alert()"'		Type into the URL after "frame#x", where x can be 1, 2, or 3.

The hints stated that data in the window.location object could be influenced by an attacker. I assumed this was related to "frame#" portion in the URL since that was the only part that changed when I clicked on the different images. I tried typing alert() and javascript:alert() into the URL. Eventually I realized that I needed to add quotes, and after a few tries, I found that 'onerror="javascript:alert()"' worked.

Level 4

Answer - ');alert('	Type into the timer box and then click the 'create timer' button.

The hints indicated I try inputing a single quote. When I did this, I noticed that the timer never went off. From this I assumed that we could use quote to inject code. I tried variations of 'alert()' and onerror. Then I realized I the code injection would go where "timer" was under startTimer. Therefore, I needed a single quote and a close parenthesis. Next I tried ');alert()', but this still did nothing. It took a while before I realized I needed an open parenthesis to since I was starting with a closed parenthesis.

Level 5

Answer - Click on "Sign up". Then in the URL box, type in 'https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert()'. Then click on "Go", and then "Next>>".

When I clicked on the "sign up" button, I noticed in the URL there was a "signup?next=confirm". That combined with the hint made me look at how the "Next" button worked. I tried 'next=alert()', 'next="javascript:alert()"', and a bunch of variations based on my previous answers, but nothing was working. After a while, I tried using variations of my previous answers, except I clicked on the "Go" button next to the URL before clicking "Next". From this I found that 'next=javascript:alert()' worked if I clicked "Go" and then "Next".

Level 6

Answer - https://xss-game.appspot.com/level6/frame#HTTPS://google.com/jsapi?callback=alert	Type into the URL box and click "Go"

One hint said pointed me to the # in the URL bar. I tried using variations of my previous answers to replace everything after the # in the URL, but that did not work. Another hint said to use 'google.com/jsapi?callback=foo'. I remembered that "foo" tends to be a filler name for random functions so I tried replacing foo with alert(). So, I put "https://google.com/jsapi?callback=alert()" after the #. At first this did not work because it did not allow for loading URLs containing "http". After a while, I noticed that it did not sanitize "HTTPS", so I replaced "https" with "HTTPS. This still did not work. Then I noticed in the hint that foo did not have "()". So I tried deleting the "()" after "alert" and this worked.

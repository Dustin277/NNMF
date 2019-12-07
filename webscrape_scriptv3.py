import urllib.request
import re
from bs4 import BeautifulSoup

urls = [
"https://en.wikipedia.org/wiki/Computer_security",
"https://en.wikipedia.org/wiki/Spectre_(security_vulnerability)",
"https://en.wikipedia.org/wiki/Meltdown_(security_vulnerability)",
"https://en.wikipedia.org/wiki/Encryption",
"https://en.wikipedia.org/wiki/Password",                   
"https://en.wikipedia.org/wiki/Internet_security",
"https://en.wikipedia.org/wiki/Malware",
"https://en.wikipedia.org/wiki/Botnet",
"https://en.wikipedia.org/wiki/Computer_virus",
"https://en.wikipedia.org/wiki/Computer_worm",
"https://en.wikipedia.org/wiki/Ransomware",
"https://en.wikipedia.org/wiki/Spyware",
"https://en.wikipedia.org/wiki/Keystroke_logging",
"https://en.wikipedia.org/wiki/Trojan_horse_(computing)",
"https://en.wikipedia.org/wiki/Phishing",
"https://www.imperva.com/learn/application-security/web-scraping-attack/",
"https://en.wikipedia.org/wiki/Denial-of-service_attack",
"https://en.wikipedia.org/wiki/Email_spoofing",                
"https://en.wikipedia.org/wiki/Antivirus_software",
"https://en.wikipedia.org/wiki/Layered_Service_Provider",
"https://en.wikipedia.org/wiki/Doxing",
"https://en.wikipedia.org/wiki/Cyberattack",
"https://en.wikipedia.org/wiki/Hacker",
"https://en.wikipedia.org/wiki/Security_hacker",
"https://en.wikipedia.org/wiki/Watering_hole_attack",
"https://en.wikipedia.org/wiki/Honeypot_(computing)",
"https://en.wikipedia.org/wiki/Computer_virus",
"https://en.wikipedia.org/wiki/Adware",
"https://en.wikipedia.org/wiki/Session_hijacking",
"https://www.pcrisk.com/removal-guides/12725-go-deepteep-com-redirect",
"https://en.wikipedia.org/wiki/Tor_(anonymity_network)",
"https://en.wikipedia.org/wiki/HTTPS",
"https://en.wikipedia.org/wiki/Transport_Layer_Security",
"https://en.wikipedia.org/wiki/SQL_injection",
"https://en.wikipedia.org/wiki/Cross-site_scripting",
"https://en.wikipedia.org/wiki/Cheating_in_online_games",
"https://en.wikipedia.org/wiki/Buffer_overflow",
]

terms = [   
"exploit",
"data",
"trick",  
"attack",
"steal",
"block",
"software",   
"vulnerability",
"protect",
"hack",    
"privacy",
"security",
"illegal",
"encryption",
"harm",
"remote", 
"malicious",
"computer",
"threat",
"bypass",   
"infected",   
"damage",
"internet",
"code"
]

def word_count(url,term):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    
    for script in soup(["script", "style"
                        #,"span","i","href","sup","cite","table"
                        ]):
        script.extract()    # take it out
        
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    #print (text)
    
    count = 0
    
    text_list = re.sub("[^\w]", " ",  text).split()

    flag = False
    for word in text_list:
        if word == term:
            count+=1
            flag = True
        term.capitalize()
        if word == term and flag == False:
            count+=1
    return count

V = []

iteration = 0
for url in urls:
    temp = []
    for term in terms:
        temp.append(word_count(url,term))
        iteration += 1
        print('The word', term, 'appears', temp[-1], 'times in', url)
    print("next")
    V.append(temp)

#print(len(V))
#for i in V:
#    print(i)
V = str(V)

V = V.replace(",","")
V = V.replace("]","; \n")
V = V.replace("[","")

print("V =[",V[:-6],"];")

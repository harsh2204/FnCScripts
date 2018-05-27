# Author: Harsh Gupta
# A simple python app that reads a pool of urls ,delimited by new line or '\n', from a text file to estimate the total file size. This tool is very handy in mapping opendirectory links. Goto r/opendirectories for more info.
# Requires colorama library. Use $pip3 install colorama. If unavailable, follow the instructions in comments

from urllib.request import Request, urlopen
import time
from colorama import init, Fore, Style #Comment if no colorama


MBFACTOR = float(1 << 20)
GBFACTOR = float(1 << 30)
start_time = time.clock()
init() #Comment if no colorama

# TODO: Parallelize requests to speed up the process of getting size. Current avg time to grab a page from a slow server is approximately .5 seconds. (VERY BAD!!)

def getSize(file_url):
    try:
        req = Request(file_url, headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(req)
        size = site.getheader('Content-Length')
        return (int(size) / GBFACTOR)
    except KeyboardInterrupt:
        raise SystemExit
    except:
        # print(f"{Fore.RED}BAD LINK!{Style.RESET_ALL}")
        return 0

def poolSize(textfile, removeDeadLinks):
    total_size = 0.0
    file = open(textfile,'r')
    links = file.readlines()
    file.close()
    for i in range(len(links)-1,-1,-1):
        url = links[i]
        size = getSize(links[i])
        if(size==0):
            print(f"{Fore.RED}({i+1}){Style.RESET_ALL} // Current Link: {url}") #Comment if no colorama
#			print(f"({i+1}) (REMOVED) // Current Link: {url}") #Uncomment if no colorama
            if removeDeadLinks: del links[i]
        else:
            print(f"{Fore.GREEN}({i+1}){Style.RESET_ALL} // Current Link: {url}") #Comment if no colorama
#			print(f"({i+1})// Current Link: {url}") #Uncomment if not colorama
            total_size +=size
    if removeDeadLinks:
        clean = open(f"{textfile.split('.txt')[0]}Cleaned.txt",'w')
        clean.writelines(links)
        clean.close()
    print('{:<40}: {:.2f} GB'.format('TOTAL SIZE', int(total_size)))
    print(time.clock() - start_time, "seconds to complete the task.")


# estSize("masterLinks.txt", True)

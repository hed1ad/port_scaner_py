import socket
from datetime import datetime
import sys 

start = datetime.now()

ports = {
    20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet",
    25: "SMTP", 43: "WHOIS", 53: "DNS", 80: "http",
    115: "SFTP", 123: "NTP", 143: "IMAP", 161: "SNMP",
    179: "BGP", 443: "HTTPS", 445: "MICROSOFT-DS",
    514: "SYSLOG", 515: "PRINTER", 993: "IMAPS",
    995: "POP3S", 1080: "SOCKS", 1194: "OpenVPN",
    1433: "SQL Server", 1723: "PPTP", 3128: "HTTP",
    3268: "LDAP", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 5900: "VNC", 8080: "Tomcat", 10000: "Webmin"
}

try:
    host_name = sys.argv[1]
    ip = socket.gethostbyname(host_name)
    
    print(f"Scanning {host_name} ({ip})...\n")
    
    for port in ports:
        cont = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cont.settimeout(1)
        try:
            cont.connect((ip, port))
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = ip
            print(f"{hostname}:{port} is open/{ports[port]}")
        except (socket.timeout, socket.error):
            pass
        finally:
            cont.close()

except IndexError:
    print("Usage: python scaner.py <hostname>")
except socket.gaierror:
    print("Error: Could not resolve hostname")
except KeyboardInterrupt:
    print("\nScan aborted by user")

end = datetime.now()
print(f"\nScan started at: {start}")
print(f"Scan finished at: {end}")
print(f"Duration: {end - start}")


import socket

def get_ip(host):
    '''Getting IP address using host or website
    '''

    ip_ad = socket.gethostbyname(host)
    return f"IP address of {host} is {ip_ad}"

ip = get_ip("emotionaldiary.com")
print(ip)
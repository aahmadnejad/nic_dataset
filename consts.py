import socket
from scapy.all import get_if_addr


def CONNECTION(finder:int):
    find = 'wl' if finder == 1 else 'et'
    for idx, con in socket.if_nameindex():
        if find in con:
            return con

def LOCALIP(finder:int):
    return get_if_addr(CONNECTION(finder))

PORTOCOLS = ['TCP', 'UDP', 'ICMP']
INFORMATIONS = ['src', 'dst', 'sport', 'dport']

CSV_COLUMNS = ['SourceIP', 'DestinationIP', 'SourcePort', 'DestinationPort', 'Protocol',
               'Duration', 'Sent_per_Flow', 'received_per_Flow', 'Total_Bytes_used_for_Headers']

from consts import *

from scapy.all import sniff
import pandas as pd
import numpy as np
import os
import sys


def dataExtraction(finder: int = 1, time: int = 150):
    Data = pd.DataFrame(columns=CSV_COLUMNS)

    for index, info in enumerate(sniff(iface=CONNECTION(finder), timeout=time)):
        packet_dict = {}
        isValid = False
        packet_dict['Duration'] = info.time

        for line in info.show2(dump=True).split('\n'):
            if '###' in line:
                layer = line.strip('#[] ')
                if layer in PORTOCOLS:
                    packet_dict['Protocol'] = layer
                    isValid = True
            elif '=' in line:
                key, val = line.split('=', 1)
                key = key.strip()
                if key in INFORMATIONS:
                    try:
                        packet_dict[key] = val.strip()
                    except:
                        packet_dict[key] = np.nan

        if isValid:
            packet_dict['SourcePort'] = packet_dict.pop('sport')
            packet_dict['SourceIP'] = packet_dict.pop('src')
            packet_dict['DestinationIP'] = packet_dict.pop('dst')
            packet_dict['DestinationPort'] = packet_dict.pop('dport')
            packet_dict['Sent_per_Flow'] = len(info) if packet_dict['SourceIP'] == LOCALIP(finder) else 0
            packet_dict['received_per_Flow'] = 0 if packet_dict['SourceIP'] == LOCALIP(finder) else len(info)
            packet_dict['Total_Bytes_used_for_Headers'] = len(info.payload)
            Data = pd.concat([Data, pd.DataFrame(packet_dict, index=[0])], ignore_index=True)

    script_dir = os.path.abspath(os.path.dirname(sys.argv[0]) or '.')
    csv_path = os.path.join(script_dir, 'dataset.csv')
    Data.to_csv(csv_path)

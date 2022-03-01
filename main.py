import argparse

from dataExtraction import dataExtraction

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='file options')
    parser.add_argument('--time', type=int, action='store', help='the duration of tracking the NIC (default:300)')
    parser.add_argument('--net', type=int, action='store', help='choose Ethernet(0) or WLAN(1) (default:1)')

    args = parser.parse_args()
    if args.net:
        if args.net not in [0, 1]:
            raise Exception("check the --help for --N")
        if args.time:
            dataExtraction(time=args.time, finder=args.net)
        else:
            dataExtraction(finder=args.net)
    elif args.time:
        dataExtraction(time=args.time)
    else:
        dataExtraction()


import argparse

import sys

from sender import send_emails


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    args = parser.parse_args()

    if args.command == 'send_emails':
        send_emails()
        return 0
    else:
        parser.print_help(sys.stderr)
        return 1


if __name__ == '__main__':
    exit(main())

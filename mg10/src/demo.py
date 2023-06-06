#!/usr/bin/env python3

import argparse

from onrobot import MG
import time

def run_demo():
    """interactive controller demo."""
    mg = MG(toolchanger_ip, toolchanger_port)
    while True:
        mg.get_status()
        print(f"Target strength: {mg.get_current_strength()} %")
        print("Command list:")
        print("  s: set strength, g: grip, r: release, q: quit")
        c = input("command > ")
        if c == "s":
            c = input("Target strength (0 ~ 100) > ")
            target_strength = int(c)
            if 0 <= target_strength <= 100:
                mg.set_target_strength(target_strength)
            else:
                print("Target strength must be 0 ~ 100")
        elif c == "g":
            mg.set_command(1)
        elif c == "r":
            mg.set_command(0)
        elif c == "q":
            break

    mg.set_command(0)
    mg.close_connection()
    exit(0)

def get_options():
    """Returns user-specific options."""
    parser = argparse.ArgumentParser(description='Set options.')
    parser.add_argument(
        '--ip', dest='ip', type=str, default="192.168.1.1",
        help='set ip address')
    parser.add_argument(
        '--port', dest='port', type=str, default="502",
        help='set port number')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_options()
    toolchanger_ip = args.ip
    toolchanger_port = args.port
    run_demo()

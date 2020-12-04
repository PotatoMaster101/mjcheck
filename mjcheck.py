#!/usr/bin/env python3
####################################################################################################
# Mojang server status checker.
# Repo: https://github.com/PotatoMaster101/mjcheck
####################################################################################################

import urllib.request as req
import json
import sys

API = "https://status.mojang.com/check"     # mojang API URL
FORMATTER = "{:<30} {:<6}"                  # print formatter
STATUS = {                                  # server status code
    "green": "online",
    "yellow": "online, but contains issue",
    "red": "offline"
}

def get_status():
    """Retrieves Mojang server status.

    Returns:
        The Mojang server status deserialized.
    """
    with req.urlopen(API) as r:
        return json.loads(r.read())

if __name__ == "__main__":
    status = get_status()
    for server in status:
        name, stat = next(iter(server.items()))     # should only have 1 entry in dict
        if stat not in STATUS:
            print(f"ERROR: Unknown status {stat} for {name}", file=sys.stderr)
            continue
        print(FORMATTER.format(name, STATUS[stat]))

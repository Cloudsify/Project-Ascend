"""
Project Ascend's Discord bot, Written and mainted by @Cloudsify

github.com/Cloudsify
"""

debugEnabled = True

def info(message):
    print(f"[Ascend] <INFO> {message}")

def error(message):
    print(f"[Ascend] <ERROR> {message}")

def warning(message):
    print(f"[Ascend] <WARNING> {message}")

def debug(message):
    if debugEnabled:
        print(f"[Ascend] <DEBUG> {message}")
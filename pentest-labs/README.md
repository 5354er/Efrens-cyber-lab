# Efrens Cyber Lab - Raspberry Pi Web Server Project

## Description

This project demonstrates:

- A Raspberry Pi running Apache2 serving a custom `index.html` page.
- An Nmap scan performed from a Kali machine to identify open ports and OS details.

## Files

- `index.html`: Custom HTML page hosted on the Pi.
- `nmap_scan.txt`: Nmap output showing open ports on 192.168.0.14.

## Nmap Command Used

```bash
nmap -sS -O 192.168.0.14 -oN nmap_scan.txt

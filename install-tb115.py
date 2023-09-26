#!/usr/bin/env python3

import osfinder
import os

version = osfinder.FindOsver()
arch = osfinder.FindArch()

urls = [
    f"https://kojipkgs.fedoraproject.org//packages/thunderbird/115.0.1/1.{version}/{arch}/thunderbird-115.1.1-1.{version}.{arch}.rpm > /dev/null 2>&1",
    f"https://kojipkgs.fedoraproject.org//packages/thunderbird/115.0.1/1.{version}/{arch}/thunderbird-librnp-rnp-115.1.1-1.{version}.{arch}.rpm > /dev/null 2>&1",
    f"https://kojipkgs.fedoraproject.org//packages/thunderbird/115.0.1/1.{version}/{arch}/thunderbird-debuginfo-115.1.1-1.{version}.{arch}.rpm > /dev/null 2>&1",
    f"https://kojipkgs.fedoraproject.org//packages/thunderbird/115.0.1/1.{version}/{arch}/thunderbird-debugsource-115.1.1-1.{version}.{arch}.rpm > /dev/null 2>&1",
    f"https://kojipkgs.fedoraproject.org//packages/thunderbird/115.0.1/1.{version}/{arch}/thunderbird-librnp-rnp-debuginfo-115.1.1-1.{version}.{arch}.rpm > /dev/null 2>&1"
]

os.system(f"mkdir /tmp/thunderbird-115-fedora")

num = 1
for i in urls:
    print(f"Downloading file {num}/5")
    os.system(
        f"curl --url {i} --output /tmp/thunderbird-115-fedora/thunderbird{num}.rpm")
    num += 1

print("Installing (please enter root password)")
os.system("sudo dnf localinstall /tmp/thunderbird-115-fedora/* -y")

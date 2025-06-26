# dns_sniffer

<p align="center">
    <img width="700"
        src="images/001.png"
        alt="Main Banner"
        style="float: left; margin-right: 10px;">
</p>

**DNS Sniffer** is a tool that captures **DNS** traffic on a Network Inetrface. You can use it by providing the **network interface name**.

<p align="center">
    <img width="700"
        src="images/002.png"
        alt="Tool excecution Example"
        style="float: left; margin-right: 10px;">
</p>

## Table of contents

- [First stepts](#what-do-i-need-to-run-it)
- [Neccesarry steps before running](#how-does-it-work)
- [How to run it](#how-do-i-use-it)

## What do I need to run it?

1. First, clone the repository:

    ```git
    git clone https://github.com/sammy-ulfh/dns_sniffer.git
    ```

2. Then, navigate to the **dns_sniffer/script** directory.

3. Next, install required libraries using pip:

    ```pip3
    pip3 install -r requirements.txt
    ```

## How does it work?

This **DNS Sniffer** tool that captures all DNS traffic on your Network Inetrface, focused on capture all visied domains.

It was built to capture traffic while performing spoofing, allowing you to see all the domains your target is accessing. You can complement the **[arp_spoofing](https://github.com/sammy-ulfh/arp_spoofer)** tool with this one to capure all dns traffic from your target.

<p align="center">
    <img width="700"
        src="images/003.png"
        alt="Tool excecution Example"
        style="float: left; margin-right: 10px;">
</p>

## How do I use it?

**NOTE:** Root privileges are required.

- **Inetrface:**
    Provide a Nework Interface Name using the **-i / --interface** argument.<br/>
    Example: -i wlan1

Great! you are now able to intercept all the domains accessed by your target.

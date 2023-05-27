# Networking Scanner Project

## Project Idea

The goal of this project is to develop a basic networking scanner tool. This tool will allow users to scan and identify devices connected to a network and gather essential information about these devices.

## Features

- **IP Range Scanning:** Provide users the ability to specify an IP address range to scan for connected devices.
- **Ping Sweep:** Implement a ping sweep feature to quickly identify live hosts on the network.
- **Basic Port Scanning:** Scan target devices for common open ports, such as HTTP (80), HTTPS (443), FTP (21), and SSH (22).
- **Basic Service Detection:** Identify basic services running on the target devices based on the open ports found.
- **Scan Results Export:** Export the scan results to a simple text file for further analysis or reporting.

Edit: Whilst working on project Scan Results Export was removed due to switching over to a gui solution, rendering it redundant.
Same thing for the Ping Sweep

## Usage Instruction:

## Prerequisites
- Up to date Python verison: You can download Python from the official website (https://www.python.org) if it's not already installed.
- Required Python libraries: `ipaddress`, `subprocess`, `re`, `socket`, `tkinter`. These libraries are part of the standard Python library and should already be available in most Python installations.

## Installation
1. Download or clone the project repository to your local machine.You can use the following command to do so.
```
git clone git@github.com:GabrielSoldati/NWS.git

```


## Usage
2. Open a command prompt or terminal and navigate to the project directory.
3. Run the main.py file to launch the Network Scanner GUI. This can be done with the following command:

```
python main.py
```
Yuu may also run main.py in other ways.

4. The GUI interface will be displayed, allowing you to enter the IP range and port range for scanning.
5. Enter the IP and Port ranges you wish to scan and then press "Scan Network"
The results will be displayed on the GUI above the "Scan Network" button.


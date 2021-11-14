# Vauban.scan
Vauban.scan is a part of vauban project. Learn more in my github profile.

# Features
- Scan for hosts in desired network
- Gather IP/Mac address and closed/opened/filtered ports
- Show results in a html page


# Installation & dependencies

## Dependencies
- Scapy
- Eel
- Argparse
- JSON

## Installation

- Clone github repo : 
```
git clone https://github.com/v1k1-ng/Vauban.scan.git
```

- Install all dependencies
```
pip install -r requirements.txt
```

-Run the script

#### Script tested in python 3.9.2


# Running the script 

To scan for 192.168.0.0/24 and ports 80 and 443 (for html server maybe?) with interface wlan0
```
python3 main.py -i 192.168.0.0/24 -p 80-443 -int wlan0
```

If -p is not defined, main.py will scan for 1 to 512 ports by default

### Make sure that interface name is correct, otherwise it won't work

### The script is explained function by function in the script

### If there is any bug, or you have problems executing /installing the script, let me know, i'll be happy to help!

## License
[MIT](https://choosealicense.com/licenses/mit/)








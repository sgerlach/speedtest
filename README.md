# speedtest
------
Keeping ISPs honest by collecting data!

# Requirements
* speedtest-cli
* an installation of elasticsearch
* kibana
* python 2.7

# Setup
1. Configure index.py to point at your elastciksearch instance
2. Set up a crontab to run index.py via the python 2.7 interpreter, for example
```
#*/16 * * * * {user} /bin/python {location of}/speedlog/index.py > /dev/null 2>$1
```
3. Load up kibana and harras the crap out of your ISP if they are not delivering what you are paying for.

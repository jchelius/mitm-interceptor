Instructions for running
Install mitmproxy (instructions to come)
Install certificates (instructions to come)
Run the following commands in the terminal to setup and run the proxy:
1. `./setup-transparent.sh`
2. `./start-proxy.sh interceptor.py`

Once done using the proxy, run the following command to reset the network to normal:
1. `./flush-iptables.sh`


Supported Apps

Application | Trusts proxy certificate | Can intercept requests 
--- | --- | --- 
Slack (client app) | NO | NO 
Discord (client app) | YES | NO
Firefox | YES | YES
Chromium | YES | YES
Outlook (in browser) | ? | NO
Gmail (in browser) | YES | YES
Slack (in browser) | YES | YES
Discord (in browser) | ? | NO


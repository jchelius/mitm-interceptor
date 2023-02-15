Instructions for running
Install mitmproxy (instructions to come)
Install certificates (instructions to come)
Run the following commands in the terminal to setup and run the proxy:
'./setup-transparent.sh'
'./start-proxy.sh interceptor.py'

Once done using the proxy, run the following command to reset the network to normal:
'./flush-iptables.sh'


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


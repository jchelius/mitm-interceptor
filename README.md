Instructions for running
<br> Install mitmproxy (instructions to come)
<br> Install certificates (instructions to come)
<br> Add mitmproxyuser user account
<br> `sudo useradd mitmproxy`
<br> Run the following commands in the terminal to setup and run the proxy:
1. `./setup-transparent.sh`
2. `./start-proxy.sh interceptor.py`

Once done using the proxy, run the following command to reset the network to normal:
1. `./flush-iptables.sh`


Supported Apps

Application | Trusts proxy certificate | Can intercept requests | Notes
--- | --- | --- | ---
Slack (client app) | NO | NO |
Discord (client app) | YES | NO |
Firefox | YES | YES |
Chromium | YES | YES |
Outlook (in browser) | - | NO | Disabling HTTP3 gets it to work
Gmail (in browser) | - | YES |
Slack (in browser) | - | YES |
Discord (in browser) | - | NO | Disabling HTTP3 gets it to work


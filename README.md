Instructions for setup

<br> [Install mitmproxy]( https://mitmproxy.org/)

<br> Configure IP fowarding:

1. `sysctl -w net.ipv4.ip_forward=1`
2. `sysctl -w net.ipv6.conf.all.forwarding=1`

<br> Disable ICMP requests:

1. `sysctl -w net.ipv4.conf.all.send_redirects=0`

<br> Create mitmproxyuser account to redirect traffic originating from the machine itself:

1. `sudo useradd --create-home mitmproxyuser`
2. `sudo -u mitmproxyuser -H bash -c 'cd ~ && pip install --user mitmproxy'`

<br> [Install certificates for desired browser/system](https://docs.mitmproxy.org/stable/concepts-certificates/)

<br> Run the following commands in the terminal to setup and run the proxy:

1. `./setup-transparent.sh`
2. `./start-proxy.sh interceptor.py`

Once done using the proxy, run the following command to reset the network to normal:

1. `./reset-iptables.sh`


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


sudo iptables -t nat -A OUTPUT -p tcp -m cgroup --cgroup 0x00110011 -m owner ! --uid-owner mitmproxyuser --dport 80 -j REDIRECT --to-port 8080
sudo iptables -t nat -A OUTPUT -p tcp -m cgroup --cgroup 0x00110011 -m owner ! --uid-owner mitmproxyuser --dport 443 -j REDIRECT --to-port 8080
sudo ip6tables -t nat -A OUTPUT -p tcp -m cgroup --cgroup 0x00110011 -m owner ! --uid-owner mitmproxyuser --dport 80 -j REDIRECT --to-port 8080
sudo ip6tables -t nat -A OUTPUT -p tcp -m cgroup --cgroup 0x00110011 -m owner ! --uid-owner mitmproxyuser --dport 443 -j REDIRECT --to-port 8080

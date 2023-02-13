if [ -z "$1" ]
then
	sudo -u mitmproxyuser -H bash -c '$HOME/.local/bin/mitmproxy --mode transparent --showhost --set block_global=false'
else
	sudo -u mitmproxyuser -H bash -c "\$HOME/.local/bin/mitmdump --mode transparent --showhost --set block_global=false -s $1"
fi

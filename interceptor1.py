from mitmproxy import ctx, http
def request(flow):
    if 'zBibhIrdQjeSI9AW26hT' in flow.request.text:
        flow.request.text = flow.request.text.replace('zBibhIrdQjeSI9AW26hT', 'FAKE_CIPHERTEXT')
        print("Modified http request: " + flow.request.text)
        
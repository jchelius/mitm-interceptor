from mitmproxy import ctx, http

def request(flow):
    #print(f"intercepted flow")
    if isinstance(flow, http.HTTPFlow):
        # print(f"HTTP request: {flow.request.text}")
        if "hello" in flow.request.text:
            flow.request.text = flow.request.text.replace("hello", "11111")
            print(f"Modified http request: {flow.request.text}")

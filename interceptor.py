import logging
import re

from mitmproxy import ctx
from mitmproxy import exceptions
import time

class ModifyBodyAndLog:
    def request(self, flow):
        print("received request")
        if flow.response or flow.error or not flow.live:
            return
        if not flow.request:
            return
        start_time = time.time()
        pattern = 'seids/{test_message\}seide'
        replacement = 'seids\{test_message_metadata\}seide'
        flow.request.content = re.sub(pattern.encode('utf-8'), replacement.encode('utf-8'), flow.request.content)
        logging.info('finished processing request')
        logging.info(f'time to process request: {time.time() - start_time}s')
addons = [ModifyBodyAndLog()]

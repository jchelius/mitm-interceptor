import logging
import re

from mitmproxy import ctx
from mitmproxy import exceptions

class ModifyBody:
    def request(self, flow):
        if flow.response or flow.error or not flow.live:
            return
        if not flow.request:
            return
        start_time = time.time()
        flow.request.content = re.sub('seids\{test_message\}seide', 'seids\{test_message_metadata\}seide', flow.request.content)
        logging.info('finished processing request')
        logging.info(f'time to process request: \{time.time() - start_time\}s')
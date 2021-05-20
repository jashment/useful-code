"""
Best to use iPython
First set variables for file_in and file_out
Then run using iPython
"""

import json
with open(file_in) as fin:
    text = fin.read()
data = json.loads(text)
with open(file_out, 'w') as fout:
    fout.write(json.dumps(data))
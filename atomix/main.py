"""
Description to add
"""

import ntplib
from time import ctime

get_time = ntplib.NTPClient()

def local_time():
    response_local = get_time.request('za.pool.ntp.org', version=3)
    print("Local time:         "+ctime(response_local.tx_time))

local_time()

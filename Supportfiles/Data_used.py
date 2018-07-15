import time
import psutil
import threading

def main():
    t0 =time.time()
    counter =psutil.net_io_counters(pernic=True)['Wi-Fi']
    total = [(counter.bytes_sent)/1024.0,(counter.bytes_recv)/1024.0,(counter.bytes_sent+counter.bytes_recv)/1024.0]
    return total

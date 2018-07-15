import threading
import time
import psutil
import signal
import sys


def calc_ul_dl(dt=1, interface='Wi-Fi'):

    t0 = time.time()
    counter = psutil.net_io_counters(pernic=True)[interface]
    tot = (counter.bytes_sent, counter.bytes_recv)
    while True:
        last_tot = tot
        time.sleep(dt)
        counter = psutil.net_io_counters(pernic=True)[interface]     
        tot = (counter.bytes_sent, counter.bytes_recv)
        ul, dl = [(now - last) / (dt) / 1024.0
                  for now, last in zip(tot, last_tot)]
        transfer_rate[0]=round(ul,2)
        transfer_rate[1]=round(dl,2)
    print("internetspeed")

def speed():
    
        return transfer_rate

def start():
    global value
    global transfer_rate
    transfer_rate = []
    transfer_rate.append(0)
    transfer_rate.append(0)
    global t
    t = threading.Thread(target=calc_ul_dl, args=())
    t.start()
    


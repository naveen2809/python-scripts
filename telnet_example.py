import getpass
import sys
import telnetlib
import datetime

HOST = "192.168.1.2"
output_file = "alpha_board_router_stats.txt"
user = 'root'
password = "test12345"

tn = telnetlib.Telnet(HOST)
tn.read_until(b"root@OpenWrt:/# ")

tn.write(b"uptime\n")
tn.write(b"free\n")
tn.write(b"mpstat\n")
tn.write(b"iwconfig\n")
tn.write(b"wlanconfig ath0 list sta\n")
tn.write(b"wlanconfig ath2 list sta\n")
tn.write(b"wlanconfig ath1 list sta\n")
tn.write(b"wlanconfig ath11 list sta\n")
tn.write(b"exit\n")

output = tn.read_all().decode('ascii')
output_list = output.split('\n')
time_stamp = str(datetime.datetime.now())
results_string=""
for line in output_list:
    new_line = str(line.strip())+"|"+time_stamp+"\n"
    results_string += new_line

file = open(output_file, "a")
file.write(results_string)
file.close()





import sys
import time
import psutil

pid = int(sys.argv[1])
p = psutil.Process(pid)

interval = 3

with open("process_monitor_" + p.name() + '_' + str(pid) + ".csv", "a+") as f:
        f.write("time,cpu%,mem%\n")
        while True:
                current_time = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
                cpu_percent = p.cpu_percent()
                mem_percent = p.memory_percent()
                line = current_time + ',' + str(cpu_percent) + ',' + str(mem_percent)
                print (line)
                f.write(line + "\n")
                time.sleep(interval)

import psutil

ps = [psutil.Process(i) for i in psutil.pids()] 
for p in ps:
    print(p.name())
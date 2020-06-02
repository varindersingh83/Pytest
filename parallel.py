from subprocess import Popen


processes = []

for counter in range(5):
    chrome_cmd = 'export BROWSER=chrome && python test_1.py'
    processes.append(Popen(chrome_cmd, shell=True))

for counter in range(5):
    processes[counter].wait()

from subprocess import check_call


for counter in range(10):
    chrome_cmd = 'export BROWSER=chrome && python test_1.py'
    check_call(chrome_cmd, shell=True)

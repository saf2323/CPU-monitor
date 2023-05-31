import psutil, time, os


while True:
    cpu = psutil.cpu_percent()
    print('cpu usage:',cpu, '%')
    time.sleep(3)
    if cpu>50:
        print('over usage of processor identified!!!', cpu,'%')
        print('Please close the app running in the background!')
    elif cpu<30:
        print('Normal')
    
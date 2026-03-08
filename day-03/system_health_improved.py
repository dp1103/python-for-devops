import psutil

def system_health(thres):
    usage, names= utility()
    for i in range(len(thres)):
        curr=usage[i]
        limit=thres[i]
        name=names[i]
        print(f"Current {name} usage: {curr}")
        print(f"{name} threshold value: {limit}")
        if curr>limit:
            print(f"{name} usage is high ")
        else:
            print(f"{name} is safe ")
        print('----------------------------------------')

def utility():
    try:
        curr_cpu=psutil.cpu_percent(interval=1)
        curr_disk=psutil.disk_usage('/').percent
        curr_memory=psutil.virtual_memory().percent
        curr_battery=psutil.sensors_battery().percent
        
        usage=[curr_cpu,curr_disk,curr_memory, curr_battery]
        names=['CPU', 'Disk', 'Memory', 'Battery'] 
        return usage, names
    
    except Exception as error:
        print("****Error occured, 'Not getting System metrices'****")
        exit()

def get_threshold():
    while True:
        try:
            cpu_thres=int(input("Enter CPU threshold value: "))
            disk_thres=int(input("Enter Disk Threshold value: "))
            memory_thres=int(input("Enter Memory threshold value: "))
            battery_thres=int((input("Enter Battery health value: ")))

            thres=[cpu_thres,disk_thres,memory_thres,battery_thres]
            return thres
        except ValueError:
            print("***Invalid Input, 'Please enter proper input'***")

def main():
    thres=get_threshold()
    system_health(thres)

if __name__=="__main__":
    main()
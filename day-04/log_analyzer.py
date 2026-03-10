import json

def read_log():
    try:
        with open('app.log', 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("File not found, please enter proper file.")
        exit()

def write_json(count):
    with open("log_summary.json", 'w') as json_file:
        json.dump(count, json_file)
    
def log_analyzer(log):
    log_count={
        'INFO':0,
        'WARNING':0,
        'ERROR':0
    }

    for i in log:
        if "INFO"in i:
            log_count['INFO']+=1
        elif "WARNING" in i:
            log_count['WARNING']+=1
        elif "ERROR" in i:
            log_count['ERROR']+=1
        else:
            pass
    print(log_count)
    return log_count

def main():
    log=read_log()
    count=log_analyzer(log)
    write_json(count)
    
if __name__=="__main__":
    main()
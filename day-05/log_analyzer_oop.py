import json
class LogAnalyzer:
    def __init__(self, input_file, output_file):
        self.input_file=input_file
        self.output_file=output_file

    def read_log(self):
        try:
            with open(self.input_file, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print("File not found, please enter proper file.")
            exit()

    def write_json(self, count):
        with open(self.output_file, 'w') as json_file:
            json.dump(count, json_file, indent=4)
        
    def log_analyzer(self):
        log_count={
            'INFO':0,
            'WARNING':0,
            'ERROR':0
        }
        log = self.read_log()
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
    input_file="app.log"
    output_file="log_summary.json"
    analyzer=LogAnalyzer(input_file, output_file)
    result=analyzer.log_analyzer()
    analyzer.write_json(result)
    
if __name__=="__main__":
    main()
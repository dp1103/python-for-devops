import json
import argparse
class LogAnalyzer:
    def __init__(self, input_file, output_file=None, level=None):
        self.input_file=input_file
        self.output_file=output_file
        self.level=level

    def read_log(self):
        try:
            with open(self.input_file, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"Error: {self.input_file} File not found, please enter proper file.")
            exit()
        except OSError as e:
            print(f"Error accessing file: {self.input_file}")
            exit()

    def write_json(self, count):
        if self.output_file:
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

        if self.level:
            level=self.level.upper()
            if level in log_count:
                return {level: log_count[level]}
            else:
                print("Invalid log level . please enter INFO, WARNING, ERROR")
                exit()    
        return log_count

def main():
    parser = argparse.ArgumentParser(description='What the program does')
    parser.add_argument('--file', required=True, help="path of log file")
    parser.add_argument('--out', help="Output file path")
    parser.add_argument("--level", help="filtering the level of log like ERROR, WARNING, INFO")
    args=parser.parse_args()

    analyzer=LogAnalyzer(args.file, args.out, args.level)
    result=analyzer.log_analyzer()
    print(result)
    analyzer.write_json(result)
    
if __name__=="__main__":
    main()
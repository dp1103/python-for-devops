# Log Analyzer of Day 4


## What is the problem?

Applications generate large log files containing messages like INFO, WARNING, and ERROR. Analyzing these logs manually is difficult when the files are large. Therefore, a Python script is needed to automate log analysis by reading the log file and generating a summary report that helps developers understand system issues.

## What input does it need?

The script takes a log file as input, such as **app.log**. This file contains log messages like INFO, WARNING, and ERROR. The script reads the log file and analyzes these messages to generate a summary.

## What output should it give?

The script should generate a summary of the log messages found in the log file.
- It counts the number of INFO, WARNING, and ERROR messages in the log file.
- The summary will be displayed in the terminal.
- The summary will also be written to an output file such as **log_summary.json**.

## What steps are involved?

Steps:
1. The user provides a log file as input.
2. The system checks whether the file exists and is valid. If the file is correct, it proceeds to the next step.
3. The script reads the log file.
4. The script checks each line of the log file.
5. The script counts the number of INFO, WARNING, and ERROR messages.
6. The script prints the summary of log counts in the terminal.
7. The script saves the summary in an output file.
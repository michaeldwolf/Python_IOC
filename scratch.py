import re

log_file_path = r"(path)"

regex = '(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'

match_list = []

with open(log_file_path, "r") as file:
    for line in file:
        line = line.replace('"', '')
        line = line.replace(',', '')
        #print(line)
        for match in re.finditer(regex, line, re.S):
            match_test = match.group()
            match_list.append(match_test)
            print(match_test)
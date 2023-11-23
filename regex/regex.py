import re

log_pattern = re.compile(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (\w+): (.+)$')

# Test the regex with some examples
log_lines = [
    '[2023-11-23 15:30:45] INFO: Example log message.',
    '[2023-11-23 16:45:12] ERROR: An error occured somewhere.',
    '[2023-11-23 18:20:30] DEBUG: Some debug information.',
    '[2023-11-23 20:05:17] WARNING: Some warning about the situation.',
]

def group_format(pattern: str, content: list[str]) -> str:
    for line in content:
        match = pattern.match(line)
        if match:
            timestamp, level, message = match.groups()
            print(f'Timestamp: {timestamp}, Level: {level}, Message: {message}')
        else:
            print(f'Invalid log format: {line}')

# Wil be modified
def get_time(content: str|list[str]):
    pattern = "\[.+\]"
    if type(content) == str:
        return re.match(pattern, content)[1:][:-1]
    elif type(content) == list:
        r_content = []
        for line in content:
            extracted_time = re.match(pattern, line)[1:][:-1]
            r_content.append(extracted_time)
    else:
        print("Check the data type")

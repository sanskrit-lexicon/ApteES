import re, sys

def process_parts(input_string):
    pattern = r'(B.*?E)'
    matches = re.finditer(pattern, input_string, re.DOTALL)
    for match in matches:
        print(f"Match: {match.group(0)}")

if __name__ == "__main__":
    nlines = 17
    lines = [f' B {i:02d} E = {i+1}' for i in range(nlines)]
    groupline = '\n'.join(lines)
    process_parts(groupline)

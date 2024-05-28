import re

def process_parts(input_string):
    pattern = r'(B.*?E)'
    matches = re.finditer(pattern, input_string, re.DOTALL)
    prev_end = 0  # Keep track of the end position of the previous match
    for match in matches:
        start, end = match.span()
        intervening_text = input_string[prev_end:start]
        print(f"Intervening Text: {intervening_text.strip()}")
        print(f"Match: {match.group(0)}")
        prev_end = end
    # Print the remaining text after the last match
    remaining_text = input_string[prev_end:]
    print(f"Remaining Text: {remaining_text.strip()}")

if __name__ == "__main__":
    nlines = 17
    lines = [f' B {i:02d} E = {i+1}' for i in range(nlines)]
    groupline = '\n'.join(lines)
    process_parts(groupline)

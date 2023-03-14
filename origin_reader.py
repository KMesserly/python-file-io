import re

def find_words(file_path, pattern):
    matches = []
    with open(file_path) as f:
        for i, line in enumerate(f, 1):
            for match in re.finditer(pattern, line):
                matches.append((i, match.group()))
    return matches

def write_matches(matches, output_path):
    with open(output_path, 'w') as f:
        for match in matches:
            f.write(f'{match[0]}\t{match[1]}\n')

if __name__ == '__main__':
    # Define the pattern to match
    pattern = r'\b\w*herit\w*\b'

    # Find all matches in the file.
    matches = find_words('origin.txt', pattern)

    # Write the matches to the output file.
    write_matches(matches, 'origin_output.txt')


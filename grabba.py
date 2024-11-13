import re, sys

output_file = open('ids.txt', 'w')

with open(f'{sys.argv[2]}', 'r') as file: # pass path to arma 3 modlist as argument
    for line in file:
        line = line.strip()
        match = re.search(r'id=(\d+)', line) # evil regex
        if match:
            steam_id = match.group(1)
            print(f'writing {steam_id} for id {sys.argv[1]} into output file')
            output_file.write(f'workshop_download_item {sys.argv[1]} {steam_id}\n')

file.close()
output_file.close()
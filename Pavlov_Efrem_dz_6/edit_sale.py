import sys

DATA_FILE = './bakery.csv'

pos = sys.argv[1]
new_data = sys.argv[2]

if pos.isdigit() and new_data.replace('.', '').replace(',', '').isdigit():
    with open(DATA_FILE, 'r+', encoding='UTF-8') as f:
        skip_chars = 0
        for _ in range(int(pos) - 1):
            try:
                skip_chars += len(next(f))
            except StopIteration:
                print('out of index')
                sys.exit(1)
        f.seek(skip_chars)
        f.writelines(f'{new_data}')
else:
    sys.exit(1)

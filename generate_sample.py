FILE = 'ufos.csv'
DIVIDER = 12

with open(FILE, 'r', encoding='utf-8') as file:
  with open(f'sample_{FILE}', 'w', encoding='utf-8') as out:
    for i, line in enumerate(file):
      if i % DIVIDER == 0: out.write(line)

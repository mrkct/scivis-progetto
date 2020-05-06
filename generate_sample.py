'''
Questo file genera, a partire da 'ufos.csv' un altro file chiamato
`sample_ufos.csv` che contiene un sottoinsieme delle righe. 
Alcune delle operazioni nei notebook sono abbastanza pesanti e se si 
vuole soltanto sperimentare è comodo utilizzare un sottoinsieme piccolo 
del dataset, che è più veloce
'''


FILE = 'ufos.csv'
DIVIDER = 12

with open(FILE, 'r', encoding='utf-8') as file:
  with open(f'sample_{FILE}', 'w', encoding='utf-8') as out:
    for i, line in enumerate(file):
      if i % DIVIDER == 0: out.write(line)

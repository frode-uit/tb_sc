# File: sc_02_13_fstring_examples.py
# Standard justering for tekst er venstrejustering
# Standard justering for tall er høyrejustering
dag1 = "Mandag"
dag2 = "Tirsdag"
dag3 = "Onsdag"
temp1 = 20.5
temp2 = 18.2
temp3 = 22.8

print(f'Temperaturer de første 3 dager denne uke')
print(f'{"Dag":15}{"Temperatur":10}')
print(f'{dag1:15}{temp1:10}')
print(f'{dag2:15}{temp2:10}')
print(f'{dag3:15}{temp3:10}')

print(f'\nTemperaturer de første 3 dager denne uke')
print(f'{"Dag":15}{"Temperatur":10}')
print(f'{dag1:15}{temp1:<10}')
print(f'{dag2:15}{temp2:<10}')
print(f'{dag3:15}{temp3:<10}')

print(f'\nTemperaturer de første 3 dager denne uke')
print(f'{"Dag":^15}{"Temperatur":^10}')
print(f'{dag1:^15}{temp1:^10}')
print(f'{dag2:^15}{temp2:^10}')
print(f'{dag3:^15}{temp3:^10}')

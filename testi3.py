# Toistorakenteet

# FOR-silmukka

lista = ['Mika', 'Mikko', 'Harttu', 'Markku']
for opettaja in lista:
    print('Hyvää huomenta', opettaja, '\n')
    if opettaja == 'Harttu' :
        break
print('Tervetuloa töihin')


# Kertoma

kertoma = 1
for luku in range(1, 5):
    kertoma = kertoma * luku
print('kertoma on', kertoma)
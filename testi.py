# Esimerkkejä muuttujista

etunimi = 'Petri' # Merkkijono (string)
sukunimi = "Pohjanjoki"
kengan_koko = 46 # kaksiosainen nimi: Snake Case, suositeltu tapa
kenganKoko = 42.5 # kaksiosainen nimi: Dromedar Case, ei suositella
KenganKoko = 52 # kaksiosainen nimi: Camel Case, ei suositella
opettaja = True


# Esimerkkejä rakenteista ja komennoista

# Ruudulle tulostaminen

print('Opettajana on tänään', etunimi, sukunimi)
print(sukunimi, 'on isokenkäinen, kengän koko on', kengan_koko, '\n')

koko_nimi = input('Kirjoita nimesi ')
print('Morjensta,', koko_nimi + ',', 'tervetuloa Tampereelle')

"""
Vaihtoehto kaksi (tekstien yhdistäminen, katenointi/concatenation)
tervehdys = 'Morjensta, ' + koko_nimi + ', tervetuloa Tampereelle'
print(tervehdys,)
"""


# Luetaan numeerista tietoa näppämistöstä

markat = input('Kuinka monta markkaa sait viikkorahaa? ')
eurot = float(markat) / 6
print('Se olisi nykyään ', eurot, 'euroa')

# Funktiot Pythonissa, esim. funktio, joka muuttaa markat euroiksi

def euroa(markkaa):

    """Funktio palauttaa markkoina annetun arvon euroina

    Args:
        markkaa (float): rahamäärä markkoina

    Returns:
        float: rahan määrän euroina
    """

    return markkaa / 6

viikkoraha = euroa(100)

print(viikkoraha, 'on nykyisin euroa')


# Rakenteellisia tietotyyppejä

# Lista (list)

osallistujat = ['Hakala', 'Viljanen', 'Karilainen', 'Aku Ankka']
print('Listan toinen jäsen on', osallistujat[1])
osallistujat.append('Vainio')
osallistujat[3] = 'Öllönqvist'
print(osallistujat)
print('Listassa on', len(osallistujat), 'henkilöä')

tiimin_vetaja = 'Mikko Karilainen'
print('Nimen pituus on', len(tiimin_vetaja))
print(tiimin_vetaja.upper())


# Monikko (tuple)

kouluttajat = 'Hakala', 'Viljanen', 'Vainio'
# kouluttajat[3] = 'Öllönqvist' ei toimi, koska Tuplen listaa ei voi muuttaa
print(kouluttajat)


# Joukko (set)

tutkinnon_osat = {'Perustehtävät', 'Ohjelmistokehittäjä', 'IT-tukihenkilö'}

#Tutkitaan, löytyykö joukosta jäsen (alkio) Hyvinvointiteknologia-asentaja
print('Raseko järjestää', 'Hyvinvointiteknologia-asentaja' in tutkinnon_osat) 


# Sekvenssi (Sequence)

# Avain-arvoparit (Dictionary aka Key value pair)

mini_sanakirja = {'virtahepo' : 'flodhäst', 'karhu' : 'björn', 'kettu' : 'räv'}
print('Karhu on ruotsiksi', mini_sanakirja['karhu'])



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
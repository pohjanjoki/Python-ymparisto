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
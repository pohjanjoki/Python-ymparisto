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
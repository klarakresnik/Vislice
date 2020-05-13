import model

def izpis_igre(igra):
    tekst = (
        '=========================================================\n\n'
        '{pravilni_del_gesla}\n\n' 
        'Število preostalih poskusov: {stevilo_preostalih_poskusov}\n\n'
        'Nepravilni ugibi: {nepravilni_ugibi}\n\n'
        '{obesen}'
        '========================================================\n\n'
    ).format(
        stevilo_preostalih_poskusov = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        pravilni_del_gesla = igra.pravilni_del_gesla(),
        nepravilni_ugibi = igra.nepravilni_ugibi(),
        obesen = igra.obesen(),
    )
    return tekst

def izpis_zmage(igra):
    tekst = (
        '########### BRAVO!!! ZMAGA!!! Geslo je {pravilni_del_gesla} ###########\n\n' 
        '{obesen}'

    ).format(
        pravilni_del_gesla = igra.geslo,
        obesen = igra.obesen()
    )
    return tekst

def izpis_poraza(igra):
    tekst = (
        '########### Buuu!! PORAZ! Geslo je bilo {pravilni_del_gesla} ###########\n\n' 
        '{obesen}'
    ).format(
        pravilni_del_gesla = igra.geslo,
        obesen = igra.obesen()
    )
    return tekst

def izpis_napake():
    return '########### Ugiba se ENA črka naenkrat. ########### '

def izpis_poseben_znak():
    return '########### Vpisuj samo slovenske črke. ###########'

def ponovna_igra():
    return input('Če želiš ponovno igrati pritisni 1, drugače 2: ')

def zahtevaj_vnos():
    return input('Tukaj napiši črko: ')

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        rezultat_ugiba = igra.ugibaj(poskus)
        if rezultat_ugiba == model.VEC_KOT_CRKA:
            print(izpis_napake()) 
        elif rezultat_ugiba == model.POSEBEN_ZNAK:
            print(izpis_poseben_znak())
        elif rezultat_ugiba == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif rezultat_ugiba == model.PORAZ:
            print(izpis_poraza(igra))
            break
    ponovno = ponovna_igra()
    if ponovno == '1':
        pozeni_vmesnik()
    return

pozeni_vmesnik()
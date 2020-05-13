import random

STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
VEC_KOT_CRKA = '§'
POSEBEN_ZNAK = '@'
ZMAGA = 'w'
PORAZ = 'l'

class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke
    
    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        return all(crka in self.crke for crka in self.geslo)
    
    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka
            else:
                niz += ' _ '
        return niz
    
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, ugib):
        if len(ugib) != 1:
            return VEC_KOT_CRKA
        crka = ugib.upper()
        if crka not in 'ABCČDEFGHILKJMNOPRSŠTUVZŽ':
            return POSEBEN_ZNAK
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if crka in self.geslo:
                if self.zmaga():
                    return ZMAGA
                else:
                    return PRAVILNA_CRKA
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNA_CRKA
    def obesen(igra):
        if igra.stevilo_napak() == 1:
            return '\n\n\n\n\n\n__________\n'
        elif igra.stevilo_napak() == 2:
            return ' |\n |\n |\n |\n |\n |\n_|_________\n'
        elif igra.stevilo_napak() == 3:
            return ' |_____\n |\n |\n |\n |\n |\n_|_________\n'
        elif igra.stevilo_napak() == 4:
            return ' |_____\n |     |\n |\n |\n |\n |\n_|_________\n'
        elif igra.stevilo_napak() == 5:
            return ' |_____\n |     |\n |     O\n |\n |\n |\n_|_________\n'
        elif igra.stevilo_napak() == 6:
            return ' |_____\n |     |\n |     O\n |     |\n |\n |\n_|_________\n'
        elif igra.stevilo_napak() == 7:
            return ' |_____\n |     |\n |     O\n |    /|\n |\n |\n_|_________\n'
        elif igra.stevilo_napak() == 8:
            return ' |_____\n |     |\n |     O\n |    /|\\\n |\n |\n_|_________\n'
        elif igra.stevilo_napak() == 9:
            return ' |_____\n |     |\n |     O\n |    /|\\\n |    /\n |\n_|_________\n'
        elif igra.stevilo_napak() == 10:
            return ' |_____\n |     |\n |     O\n |    /|\\\n |    / \\\n |\n_|_________\n'

with open('besede.txt', 'r', encoding='utf-8') as dat:
    bazen_besed = [vrstica.strip().upper() for vrstica in dat]

def nova_igra():
    return Igra(random.choice(bazen_besed))
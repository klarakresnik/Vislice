import bottle
import model

SKRIVNOST = 'moja_skrivnost'
DATOTEKA_S_STANJEM = 'stanje.json'
DATOTEKA_Z_BESEDAMI = 'besede.txt'

vislice = model.Vislice(DATOTEKA_S_STANJEM)
vislice.nalozi_igre_iz_datoteke()


@bottle.get('/')
def index():
    return bottle.template('index.tpl')


@bottle.post('/nova_igra/')
def nova_igra():
    id_igre, _ = vislice.nova_igra()
    bottle.response.set_cookie('idigre', 'idigre{}'.format(id_igre), secret=SKRIVNOST, path='/')
    bottle.redirect('/igra/')


@bottle.get('/igra/')
def pokazi_igro():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    igra, poskus1 = vislice.igre[id_igre]
    return bottle.template('igra.tpl',  
                            igra=igra, 
                            poskus=poskus1)


@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split('e')[1])
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')


@bottle.post('/')
def geslo():
    return bottle.template('geslo.tpl')


@bottle.post('/duo/')
def nova_igra_duo():
    id_igre, igra = vislice.nova_igra()
    novo_geslo = bottle.request.forms.getunicode('novo_geslo')
    igra.geslo = novo_geslo.upper()
    bottle.redirect('/duo/{}/'.format(id_igre))


@bottle.get('/duo/<id_igre:int>/')
def pokazi_igro(id_igre):
    igra, poskus1 = vislice.igre[id_igre]
    return bottle.template('igra.tpl', 
                            id_igre=id_igre, 
                            igra=igra, 
                            poskus=poskus1)


@bottle.post('/duo/<id_igre:int>/')
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode('crka')
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/duo/{}/'.format(id_igre))


@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')


bottle.run(reloader=True, debug=True)
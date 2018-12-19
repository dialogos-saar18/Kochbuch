# -*- coding: cp1252 -*-
def e_umrechnen(einheit_alt, einheit_neu, menge):
    if einheit_alt == einheit_neu:
        m = menge
    elif einheit_alt == u'g' and einheit_neu == u'kg':
        m = menge/1000.0
    elif einheit_alt == u'g' and einheit_neu == u'mg':
        m = menge * 1000.0
    elif einheit_alt == u'kg' and einheit_neu == u'g':
        m = menge * 1000.0
    elif einheit_alt == u'kg' and einheit_neu == u'mg':
        m = menge * 1000.0 * 1000.0
    elif einheit_alt == u'mg' and einheit_neu == u'g':
        m = menge / 1000.0
    elif einheit_alt == u'mg' and einheit_neu == u'kg':
        m = menge / 1000.0 / 1000.0
    elif einheit_alt == u'Liter' and einheit_neu == u'ml':
        m = menge * 1000.0
    elif einheit_alt == u'Liter' and einheit_neu == u'cl':
        m = menge * 100.0
    elif einheit_alt == u'Liter' and einheit_neu == u'dl':
        m = menge * 10.0
    elif einheit_alt == u'ml' and einheit_neu == u'Liter':
        m = menge / 1000.0
    elif einheit_alt == u'ml' and einheit_neu == u'cl':
        m = menge / 10.0
    elif einheit_alt == u'ml' and einheit_neu == u'dl':
        m = menge / 100.0
    elif einheit_alt == u'cl' and einheit_neu == u'Liter':
        m = menge / 100.0
    elif einheit_alt == u'cl' and einheit_neu == u'dl':
        m = menge / 10.0
    elif einheit_alt == u'cl' and einheit_neu == u'ml':
        m = menge * 10.0
    elif einheit_alt == u'dl' and einheit_neu == u'Liter':
        m = menge / 10.0
    elif einheit_alt == u'dl' and einheit_neu == u'cl':
        m = menge * 10.0
    elif einheit_alt == u'dl' and einheit_neu == u'ml':
        m = menge * 100.0
    else:
        print("Nicht umrechenbar")
    return m    

def e_ausschreiben(einheit):
    if einheit == u'EL, gestr.':
        e = u'EL, gestrichen'
    #elif einheit == u'EL, geh�uft':
        #pass
    elif einheit == u'TL, gestr.':
        e = u'TL, gestrichen'
    elif einheit == u'gr. Dose/n':
        e = u'gro�e Dose/n'
    elif einheit == u'gr. Flasche(n)':
        e = u'gro�e Flasche(n)'
    elif einheit == u'gr. Gl�ser':
        e = u'gro�e Gl�ser'
    elif einheit == u'gr. Glas':
        e = u'gro�es Glas'
    elif einheit == u'gr. Kopf':
        e = u'gro�er Kopf'
    elif einheit == u'gr. Scheiben':
        e = u'gro�e Scheiben'
    elif einheit == u'm.-gro�e':
        e = u'mittelgro�e'
    elif einheit == u'm.-gro�er':
        e = u'mittelgro�er'
    elif einheit == u'm.-gro�es':
        e = u'mittelgro�es'
    elif einheit == u'Msp.':
        e = u'Messerspitze'
    elif einheit == u'n. B.':
        e = u'nach Belieben'
    elif einheit == u'Pck.':
        e = u'P�ckchen'
    elif einheit == u'Pkt.':
        e = u'P�ckchen'
    else:
        e = einheit
    return e
    

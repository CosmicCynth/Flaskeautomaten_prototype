from itertools import count

import automat
from automat import beregn_session_total


# Denne funktion samler al information til brugeren i en tekst
def generer_bruger_info():
    return generer_flaske_info()

# Denne funktion genererer information om sessionens afleverede flasker
def generer_flaske_info():
    return beregn_session_total()

# Denne funktion genererer teksten til udskrift på kvittering
def generer_kvittering_total():
    for type in automat.pantdata.keys():
        if type in automat.session:
            print(automat.pantdata[type]['info'] + ' ' + str(automat.session.count(type)) + ' x ' + str(automat.pantdata[type]['takst']) + 'kr.')
    out = ""
    for type in automat.pantdata.keys():
        out += type
        out += str(automat.session.count(type))
        out += automat.session.count(type) * str(automat.pantdata[type]['takst'])
    svar = 'total værdi udbetalt ' + str(automat.beregn_session_total()) + 'kr.'
    print(svar)


if __name__ == '__main__':
    aktiv = True
    automat.opstart()
    while aktiv:
        print(generer_bruger_info())
        handlingDisabled = False
        # Simuleret pantindkast/udbetal-tryk

        handling = input('Indkast pant eller udbetal. ')

        if handling == 'udbetal' or handling == "UDBETAL":
            print(str(generer_kvittering_total()))
            automat.udbetal()
            automat.doner()

        elif (handling.upper() in automat.pantdata.keys()):
            automat.modtag(handling)

        elif handling == 'shutdown':
            if input('Nedlukningskode? ') == automat.nedlukningskode:
                aktiv = False

        elif handling == 'reboot':
            if input('Nedlukningskode? ') == automat.nedlukningskode:
                automat.reboot()

        else:
            print('Handling ikke mulig.')
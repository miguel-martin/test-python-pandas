import re

class Validaciones:
    REGEXP = "[0-9]{8}[A-Z]"
    DIGITO_CONTROL = "TRWAGMYFPDXBNJZSQVHLCKE"
    INVALIDOS = {"00000000T", "00000001R", "99999999R"}

    def __init__(self):
        pass

    def isDNI(self, dni: str) -> bool:
        return dni not in self.INVALIDOS \
               and re.match(self.REGEXP, dni) is not None \
               and dni[8] == self.DIGITO_CONTROL[int(dni[0:8]) % 23] 


    def enmascararDNI(self, dni: str) -> str:
        return "***" + dni[3:6] + "**"



if __name__ == '__main__':
    # DNI que no son válidos por el Ministerio de interior
    print(Validaciones().isDNI("00000000T"))
    print(Validaciones().isDNI("00000001R"))
    print(Validaciones().isDNI("99999999R"))

    # Strings que no cumplen la expresion regular
    print(Validaciones().isDNI("0123"))
    print(Validaciones().isDNI("01234A67Z"))
    print(Validaciones().isDNI("012345678-"))
    print(Validaciones().isDNI("0123456789"))

    # DNI que si cumplen todas las validaciones
    print(Validaciones().isDNI("12345678Z"))
    print(Validaciones().isDNI("45673254S"))
    print(Validaciones().isDNI("72849506L"))

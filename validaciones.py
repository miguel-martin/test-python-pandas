import re

class Validaciones:
    REGEXP = "[0-9]{8}[A-Z]"
    DIGITO_CONTROL = "TRWAGMYFPDXBNJZSQVHLCKE"
    INVALIDOS = {"00000000T", "00000001R", "99999999R"}

    REGEXP_NIE = "[X-Z]{1}[0-9]{7}[A-Z]"

    REGEXP_PASSPORT = "[A-Z]{3}[0-9]{6}"

    def __init__(self):
        pass

    def isDNI(self, dni: str) -> bool:
        """Comprueba si es un DNI válido"""
        return dni not in self.INVALIDOS \
               and re.match(self.REGEXP, dni) is not None \
               and dni[8] == self.DIGITO_CONTROL[int(dni[0:8]) % 23] 


    def enmascararDNI(self, dni: str) -> str:
        """Devuelve las posiciones 4 a 7 de un DNI y enmascara el resto con asteriscos"""
        return "***" + dni[3:6] + "**"

    def isNIE(self, nie: str) -> bool:
        """Comprueba si es un NIE válido"""
        isValid = re.match(self.REGEXP_NIE, nie) is not None
        # reemplaza el primer caracter, X por 0, Y por 1, Z por 2
        if nie.startswith("X"):
            reemplazado = "0" + nie[1:]
        elif nie.startswith("Y"):
            reemplazado = "1" + nie[1:]
        elif nie.startswith("Z"):
            reemplazado = "2" + nie[1:]
        return isValid and self.isDNI(reemplazado)

    def enmascararNIE(self, nie: str) -> str:
        """Devuelve las posiciones 4,5,6,7 evitando el primer carácter alfabético"""
        return "****" + nie[4:7] + "*"

    def isPasaporte(self, pasaporte: str) -> bool:
        """Comprueba si es un pasaporte válido"""
        return re.match(self.REGEXP_PASSPORT, pasaporte) is not None

    def enmascararPasaporte(self, pasaporte: str) -> str:
        """Devuelve las posiciones 3,4,5,6 evitando los tres caracteres alfabéticos del pasaporte"""
        return "*****" + pasaporte[5:]



if __name__ == '__main__':

    # pruebas unitarias de Validaciones

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

    # enmascarado de DNI segun Instruccion SG 2/2019
    print(Validaciones().enmascararDNI("12345678Z"))
    
    # PASAPORTE que cumple validaciones
    print(Validaciones().isPasaporte("ABC123456"))
    
    # enmascarado de pasaporte segun instruccion SG 2/2019
    print(Validaciones().enmascararPasaporte("ABC123456"))

    # NIE que cumple validaciones
    print(Validaciones().isNIE("Z5195941Q"))

    # enmascarado de NIE segun instruccion SG 2/2019
    print(Validaciones().enmascararNIE("Z5195941Q"))

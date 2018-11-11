class Medio(object):

    def __init__(self, blancos):
        self.blancos = blancos


    def reflejar(self, una_senal, tiempo_inicial, tiempo_final):
        """
        Los blancos en el medio reflejan la senal
        """
        senial = [x*0.5 for x in una_senal]
        #tiempo_inicial == self.tiempo_inicial
        if len(senial) <= len(una_senal):
            return senial
		

        #TODO reflejar en un medio debe reflejar en todos los blancos de un medio
        #y devolver la senal reflejada
        pass

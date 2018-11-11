class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial_blanco, tiempo_final_blanco):
        self.amplitud = amplitud
        self.tiempo_inicial_blanco = tiempo_inicial_blanco
        self.tiempo_final_blanco = tiempo_final_blanco
        #TODO: completar con la inicializacion de los parametros del objeto
	
    def reflejar(self, senal, tiempo_inicial, tiempo_final):
        senial = [x*0.5 for x in senal]
        #tiempo_inicial == self.tiempo_inicial
        if len(senial) <= len(senal):
            return senial
		
        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        

from deportista import Deportista
from persona import Persona


class Futbolista(Persona, Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo,añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(nombre, edad, altura, sexo)
        Deportista.__init__(self, añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def setTarjetasRojas(self, tarjetaRoja):
        self._tarjetasRojas = tarjetaRoja

    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

    def __str__(self):
        return "Mi nombre es {} soy profesional en el deporte {} Tengo {} años de edad y llevo {} años en el deporte".format(self.getNombre(), self.getDeporte(), self.getEdad(), self.getAñosPracticando())

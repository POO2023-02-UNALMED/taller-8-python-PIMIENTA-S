class Deportista:
    def __int__(self, añosPracticando, deporte="Futbol"):
        self._deporte = deporte
        self._anosPracticando = añosPracticando

    def getDeporte(self):
        return self._deporte

    def setDeporte(self, deporte):
        self._deporte = deporte

    def getAñosPracticando(self):
        return self._añosPracticando

    def setAñosPracticando(self, añosPracticando):
        self._añosPracticando = añosPracticando

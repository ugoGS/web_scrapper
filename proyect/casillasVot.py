class CasillaDeVotacion:
    
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no esta en la lista')


casilla = CasillaDeVotacion(123,['Mexico','Morelos'])
print(casilla._identificador)
print(casilla._pais)
print(casilla.region)
print(casilla._region)
print('\n')

casilla.region = 'Mexico'

print(casilla._identificador)
print(casilla._pais)
print(casilla.region)
print(casilla._region)
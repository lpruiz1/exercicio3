class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def informacao(self):
        print(f"Marca do veículo: {self.marca}\nModelo do veículo: {self.modelo}\n")


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        Veiculo.__init__(self, marca, modelo)
        self.numero_portas = numero_portas
        pass
    
    def informacao_completa(self):
        print(f"Marca do veículo: {self.marca}\nModelo do veículo: {self.modelo}\nQuantidade de portas: {self.numero_portas}\n")
        
        
if __name__ == "__main__":
    carro1 = Carro("BYD", "Seal", 4)
    carro1.informacao_completa()
    carro2 = Carro("BYD", "Dolphin", 4)
    carro2.informacao_completa()
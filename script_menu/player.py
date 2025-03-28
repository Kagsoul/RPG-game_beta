from menu import classe_escolhida as jogador

print ("para de certeza que este codigo chegou aqui: ")

class jogador:
    def __init__(self, nome, classe):
        self.nome = nome
        self.classe = classe
        self.hp = classe["hp"]
        self.dano = classe["dano"]
        self.defesa = classe["defesa"]
        self.passiva = classe["passiva"]

    def __str__(self):
        return f"{self.nome}, the {self.classe['nome']}"

#planos, add inimigos ou fazer uma bag para o jogador usa item, com variaves de item dentro de outro script, criar profixo e sofixo de inimigo radom
# como se fosse bot, e não como npcs, da eles habilidade tbm radom, add coisas do tipo espada... bag de salario, sell or buy para acrescenta melhor o rpg

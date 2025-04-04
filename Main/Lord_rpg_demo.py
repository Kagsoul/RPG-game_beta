input(" voce precisa mante seu reino e a enconomia dele em equilibrio, terão eventos, e cada evento pode acontecer\n") 
input("será que voce vai consegui admistrar o seu reino de forma correta ou sera apenas mais um reino caido\n")
input("cuidado!!\n")
input('!\n')
input("obrigado por jogar\n")

class Reino:
    def __init__(self, nome):
        self.nome = nome
        self.popularidade = 50
        self.riqueza = 50
        self.forca_militar = 50

    def __str__(self):
        return (f"Reino: {self.nome}\n"
                f"Popularidade: {self.popularidade}\n"
                f"Riqueza: {self.riqueza}\n"
                f"Força Militar: {self.forca_militar}")

    def ajustar_atributos(self, popularidade, riqueza, forca_militar):
        self.popularidade += popularidade
        self.riqueza += riqueza
        self.forca_militar += forca_militar

def apresentar_escolhas():
    return [
        {"descricao": "Plantar mais para garantir recursos futuros.",
         "consequencias": {"popularidade": +5, "riqueza": -10, "forca_militar": 0}},
        {"descricao": "Vender recursos para enriquecer o reino.",
         "consequencias": {"popularidade": -5, "riqueza": +20, "forca_militar": 0}},
        {"descricao": "Investir na força militar.",
         "consequencias": {"popularidade": -5, "riqueza": -10, "forca_militar": +20}},
        {"descricao": "Organizar um festival para melhorar a moral do povo.",
         "consequencias": {"popularidade": +15, "riqueza": -15, "forca_militar": 0}},
        {"descricao": "Melhorar infraestrutura para o futuro.",
         "consequencias": {"popularidade": +10, "riqueza": -20, "forca_militar": 0}}
    ]

def main():
    nome_reino = input("Digite o nome do seu reino: ")
    reino = Reino(nome_reino)

    print("\nBem-vindo ao seu reino!")
    print(reino)

    dia = 1
    while True:  
        print(f"\nDia {dia}: Escolha uma ação para o seu reino!")
        escolhas = apresentar_escolhas()
        for idx, escolha in enumerate(escolhas):
            print(f"{idx + 1}. {escolha['descricao']}")

        escolha_idx = int(input("\nDigite o número da sua escolha (ou 0 para encerrar o jogo): ")) - 1

        if escolha_idx == -1: 
            print("\nFim do jogo! Estado final do reino:")
            print(reino)
            input("se voce apertou numero algum coisa errada, perdeu, troxa")
            break
               

        escolha = escolhas[escolha_idx]

        print("\nVocê escolheu: ", escolha["descricao"])
        print("Consequências: ", escolha["consequencias"])

        reino.ajustar_atributos(escolha["consequencias"]["popularidade"],
                                escolha["consequencias"]["riqueza"],
                                escolha["consequencias"]["forca_militar"])

        print("\nEstado atual do reino:")
        print(reino)

        dia += 1

if __name__ == "__main__":
    main()

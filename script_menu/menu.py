input("Pressione ENTER para começar o jogo.")
print("Bem-vindo ao RPgzil!")

nome = input("Digite o nome do seu personagem: ")
s = input("Aperte S para continuar ou N se você digitou seu nome errado: ").upper()

if s == "S":
    print("Seu nome está correto.")
    print("Você deseja continuar.")
elif s == "N":
    print("Reinicie o jogo e insira seu nome novamente.")
else:
    print("Opção inválida.")

opicao = int(input("[1] - Aperte 1 para continuar. Se você não quer continuar com este nome, aperte qualquer tecla: "))

if opicao == 1:
    # Atributos das classes
    classes = {
        1: {
            "nome": "Mago",
            "hp": 1500,
            "dano": 50,
            "defesa": 25,
            "passiva": "Curar igual à defesa"
        },
        2: {
            "nome": "Guerreiro",
            "hp": 2500,
            "dano": 45,
            "defesa": 35,
            "passiva": "Ganha 15 de defesa ao deixar de atacar"
        },
        3: {
            "nome": "Arqueiro",
            "hp": 1200,
            "dano": 60,
            "defesa": 20,
            "passiva": "Ganha esquiva de forma aleatória"
        }
    }

    print("Escolha sua classe:")
    print("[1] - Mago: Habilidade e magia")
    print("[2] - Guerreiro: Força e agilidade")
    print("[3] - Arqueiro: Distância e precisão")

    classe_escolhida = int(input("Digite o número da classe que você deseja escolher: "))

    if classe_escolhida in classes:
        classe = classes[classe_escolhida]
        print(f"\nVocê escolheu: {classe['nome']}")
        print(f"HP: {classe['hp']}")
        print(f"Dano: {classe['dano']}")
        print(f"Defesa: {classe['defesa']}")
        print(f"Passiva: {classe['passiva']}")
    else:
        print("Opção inválida. Tente novamente.")
else:
    print("Você decidiu não continuar. Reinicie o jogo.")

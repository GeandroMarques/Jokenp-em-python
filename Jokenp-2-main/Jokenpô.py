import random

print(f'Bem-vindo ao jogo jokenpô. Escolha o modo de jogo')
print(f' Pedra= 1; Papel = 2; Tesoura = 3;')
while True:
    print(f'0 - Regras')
    print(f'1 - PvP, (Jogador x Jogador)')
    print(f'2 - PvE, (Jogador x Computador)')
    print(f'3 - EvE, (Computador x Computador')
    escolha = int(input("Digite a sua escolha: "))
    if escolha == 0:
        print(f'Pedra ganha de tesora')
        print(f'Tesoura ganha de papel')
        print(f'Papel ganha de pedra')
    elif escolha == 1 or escolha == 2 or escolha == 3:
        break
    else:
        print(f'Comando inválido')

placarUM = 0
placarDOIS = 0
while escolha == 1:
    jogador1 = int(input("Jogador 1: Digite 1 para pedra, 2 para papel e 3 para tesoura: "))
    jogador2 = int(input("Jogador 2: Digite 1 para pedra, 2 para papel e 3 para tesoura: "))
    if jogador1 == 1 and jogador2 == 1:
        placarUM += 0
    elif jogador1 == 1 and jogador2 == 2:
        placarDOIS += 1
    elif jogador1 == 1 and jogador2 == 3:
        placarUM += 1
    elif jogador1 == 2 and jogador2 == 1:
        placarUM += 1
    elif jogador1 == 2 and jogador2 == 2:
        placarUM += 0
    elif jogador1 == 2 and jogador2 == 3:
        placarDOIS += 1
    elif jogador1 == 3 and jogador2 == 1:
        placarDOIS += 1
    elif jogador1 == 3 and jogador2 == 2:
        placarUM += 1
    elif jogador1 == 3 and jogador2 == 3:
        placarUM += 0
    #Comando inválido
    else:
        print(f'Comando inválido')
        
    print(f' Placar: Jogador 1 ({placarUM} x {placarDOIS}) Jogador 2')
    escolha2 = input("Quer continuar? Sim ou não: ")
    if escolha2 == "Não" or escolha2 == "não":
        print(f'Placar: Jogador 1: ({placarUM} x {placarDOIS}) Jogador 2')
        print(f'Obrigado por jogar!!! Atenciosamente Alisson, Enzo, Geandro e Juliano')
        break


placarJogador = 0
placarComputador = 0
while escolha == 2:
    jogador = int(input(" Digite 1 para pedra, 2 para papel e 3 para tesoura: "))
    computador = random.randint(1,3)
    # Computador vence
    if computador == 1 and jogador == 3:
        placarComputador += 1
        print(f'Computador: Pedra x Jogador: Tesoura')
        print(f'Computador venceu!!')
    elif computador == 2 and jogador == 1:
        placarComputador += 1
        print(f'Computador: Papel x Jogador: Pedra')
        print(f'Computador venceu!!')
    elif computador == 3 and jogador == 2:
        placarComputador += 1
        print(f'Computador: Tesoura x Jogador: Papel')
        print(f'Computador venceu!!')
    # EMPATE
    elif jogador == 1 and computador == 1:
        print(f'Computador: Pedra x Jogador: Pedra')
        print(f'Empate!!')
    elif jogador == 2 and computador == 2:
        print(f'Computador: Papel x Jogador: Papel')
        print(f'Empate!!')
    elif jogador == 3 and computador == 3:
        print(f'Computador: Tesoura x Jogador: Tesoura')
        print(f'Empate!!')
    # Jogador vence
    elif jogador == 1 and computador == 3:
        placarJogador += 1
        print(f'Jogador: Pedra x Computador: Tesoura')
        print(f"Jogador venceu!!")
    elif jogador == 2 and computador == 1:
        placarJogador += 1
        print(f'Jogador: Papel x Computador: Pedra')
        print(f"Jogador venceu!!")
    elif jogador == 3 and computador == 2:
        placarJogador += 1
        print(f'Jogador: Tesoura x Computador: Papel')
        print(f"Jogador venceu!!")
    #Comando inválido
    else:
        print(f'Comando inválido')

    print(f'Placar: Jogador {placarJogador} x {placarComputador} Computador')
    escolha2 = input("Quer continuar? Sim ou não ")
    if escolha2 == "Não" or escolha2 == "não":
        print(f'Placar: Jogador {placarJogador} x {placarComputador} Computador')
        print(f'Obrigado por jogar!!! Atenciosamente Alisson, Enzo, Geandro e Juliano')
        break


placarComputador1 = 0
placarComputador2 = 0
#0 - pedra
#1 - papel
#2 - tesoura
while escolha == 3:
    computador1 =random.randint(0, 2)
    computador2 =random.randint(0, 2)
    #computador1 vence
    if computador1 == 0 and computador2 == 2:
        placarComputador1 += 1
        print(f'Computador1: Pedra x Computador2:Tesoura')
        print(f'Computador1 venceu!!')
    elif computador1 == 1 and computador2 == 0:
        placarComputador1 += 1
        print(f'Computador1: Papel x Computador2: Pedra')
        print(f'Computador1 venceu!!')
    elif computador1 == 2 and computador2 == 1:
        placarComputador1 += 1
        print(f'Computador1: Tesoura x Computador2: Papel')
        print(f'Computador1 venceu!!')
    #Empate
    elif computador1 == 0 and computador2 == 0:
        print(f'Computador1: Pedra x Coputador2: Pedra')
        print(f'Empate!!')
    elif computador1 == 1 and computador2 == 1:
        print(f'Computador1: Papel x Coputador2: Papel')
        print(f'Empate!!')
    elif computador1 == 2 and computador2 == 2:
        print(f'Computador1: Tesoura x Coputador2: Tesoura')
        print(f'Empate!!')
    #computador2 vence
    elif computador2 == 0 and computador1 == 2:
        placarComputador2 += 1
        print(f'Computador1: Tesoura x Coputador2: Pedra')
        print(f"Computador2 venceu!!")
    elif computador2 == 1 and computador1 == 0:
        placarComputador2 += 1
        print(f'Computador1: Pedra x Coputador2: Papel')
        print(f"Computador2 venceu!!")
    elif computador2 == 2 and computador1 == 1:
        placarComputador2 += 1
        print(f'Computador1: Papel x Coputador2: Tesoura')
        print(f"Computador2 venceu!!")


    print(f' Placar: Computador1 {placarComputador1} x {placarComputador2} Computador2')
    escolha2 = input("Quer continuar? Sim ou não ")
    if escolha2 == "Não" or escolha2 == "não":
        print(f'Placar: Computador1 {placarComputador1} x {placarComputador2} Computador2')
        print(f'Obrigado por jogar!!! Atenciosamente Alisson, Enzo, Geandro e Juliano')
        break

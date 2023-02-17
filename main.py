
import time
import menu
opcao =  1
while opcao != 0:
    opcao = int(input(("Digite a opçao desejada\n1- Labirinto 1\n2- Labirinto 2\n3- Labirinto 3\n4- Labirinto 4\n5- Labirinto 5\n6- Labirinto 6\n7- Toy\n0- Sair\n")))

    if opcao == 1:
        inicio = time.time()
        print("Labirinto 1:\n")
        menu.imprime_lab("labirintos/maze3.txt")
        menu.labirinto("labirintos/maze3.txt")
        print("Tempo de execução para resolver o problema a partir da leitura do arquivo - maze3.txt -: ", time.time() - inicio)


    elif opcao == 2:
        inicio = time.time()
        print("Labirinto 2:\n")
        menu.imprime_lab("labirintos/maze10.txt")
        menu.labirinto("labirintos/maze10.txt")
        print("Tempo de execução para resolver o problema a partir da leitura do arquivo 'maze10.txt': ", time.time() - inicio)
    

    elif opcao == 3:
        inicio = time.time()
        print("Labirinto 3:\n")
        menu.imprime_lab("labirintos/maze20.txt")
        menu.labirinto("labirintos/maze20.txt")
        print("Tempo de execução para resolver o problema a partir da leitura do arquivo 'maze20.txt': ", time.time() - inicio)

    elif opcao == 4:
        inicio = time.time()
        print("Labirinto 4:\n")
        menu.imprime_lab("labirintos/maze30.txt")
        menu.labirinto("labirintos/maze30.txt")
        print("Tempo de execução para resolver o problema a partir da leitura do arquivo 'maze30.txt': ", time.time() - inicio)
    

    elif opcao ==5:
        inicio = time.time()
        print("Labirinto 5:\n")
        menu.imprime_lab("labirintos/maze40.txt")
        menu.labirinto("labirintos/maze40.txt")
        print("Tempo de execução para resolver o problema a partir da leitura do arquivo 'maze40.txt': ", time.time() - inicio)

    elif opcao ==6:
        inicio = time.time()
        print("Labirinto 6:\n")
        menu.imprime_lab("labirintos/maze50.txt")
        menu.labirinto("labirintos/maze50.txt")
        print("Tempo de execução para resolver o problema a partir da leitura do arquivo 'maze50.txt': " , time.time() - inicio)

    elif opcao == 7:
        inicio = time.time()
        print("Toy:\n")
        menu.imprime_lab("labirintos/toy.txt")
        menu.labirinto("labirintos/toy.txt")
        print("Tempo de execução para resolver o problema a partir da leitura do arquivo 'toy.txt': " , time.time() - inicio)
    

    else:
        exit()
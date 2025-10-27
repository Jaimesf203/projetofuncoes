# BANCO_DE_DADOS


#Criar uma lista vazia.
banco_de_dados = []

#Criar função e adicionar tarefa
def adicionar_tarefa():
    nova_tarefa = {
        'nome': input("Digite o nome da tarefa: "),
        'descrição': input("Digite a descrição: "),
        'prioridade': int(input("Digite a prioridade (1-5): ")),
        'categoria': input("Digite a categoria: "),
        'concluido': False
    }
    banco_de_dados.append(nova_tarefa)
    print("Nova tarefa criada com sucesso!")

def listar_tarefas():
    for tarefa in banco_de_dados: # se quiser pecorrer usa "for"
        print(f'Nome: {tarefa["nome"]}')
        print(f'Descrição: {tarefa["descrição"]}')
        print(f'Prioridade: {tarefa["prioridade"]}')
        print(f'Categoria: {tarefa["categoria"]}')
        print(f'Concluido: {"Sim" if tarefa["concluido"]else "Não"}')
        print('---------------------------- ')

def listar_por_prioridades():
    prioridade = int(input("Digite a prioridade para se listado:"))
    for tarefa in banco_de_dados:
        if tarefa["prioridade"] == prioridade:
            print(f'Nome: {tarefa["nome"]}')
            print(f'Descrição: {tarefa["descrição"]}')
            print(f'Prioridade: {tarefa["prioridade"]}')
            print(f'Categoria: {tarefa["categoria"]}')
            print(f'Concluido: {"Sim" if tarefa["concluido"]else "Não"}')
            print('---------------------------- ')

def listar_por_categoria():
    categoria = int(input("Digite a categoria para se listado:"))
    for tarefa in banco_de_dados:
        if tarefa["categoria"] == categoria:
            print(f'Nome: {tarefa["nome"]}')
            print(f'Descrição: {tarefa["descrição"]}')
            print(f'Prioridade: {tarefa["prioridade"]}')
            print(f'Categoria: {tarefa["categoria"]}')
            print(f'Concluido: {"Sim" if tarefa["concluido"]else "Não"}')
            print('---------------------------- ')

def concluir_tarefa():
    nome_busca = input("Digite o nome da tarefa a ser conluida:")
    for tarefa in banco_de_dados:
        if tarefa["nome"] == nome_busca:
          tarefa["concluida"] = True
          print("Tarefa concluida com sucesso!")
          break

    else:
        print('Nenhuma tarefa encontrada!')


def remover_tarefa():
    nome_busca = input("Digite o nome da tarefa a ser removida:")
    for tarefa in banco_de_dados:
        if tarefa in banco_de_dados:
            banco_de_dados.remove(tarefa)
            print('Tarefa foi removida com sucesso!')
            break
        else:
            print("Nenhuma tarefa encontrada!")




while True:
    print("1 - Adicionar nova tarefa")
    print("2 - Listar todas as tarefas")
    print("3 - Sair")
    print("4 - Listar por categoria")
    print("5 - Marcar tarefa como concluida")
    print("6 - Deletar tarefa")
    print("7 - Sair")
    op = int(input("-> "))
    if op == 1:
        adicionar_tarefa()
    elif op == 2:
        listar_tarefas()
    elif op == 3:
        listar_por_prioridades()
    elif op == 4:
        break
    elif op == 5:
        break
    elif op == 6:
        break
    elif op == 7:
        break

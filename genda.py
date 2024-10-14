def add_task():
  name_task = str(input('Nome da Tarefa: '))
  date_task = str(input('Data de Vencimento da tarefa: '))

  with open('Tasks.txt', 'a') as arquivo:
    arquivo.write(f"{name_task} , {date_task}\n")
  print(f'\n  Tarefa "{name_task}" adicionada com sucesso!\n')


def delet_task():
    display_task()

    name_delet_task = str(input('Me de o Nome da Tarefa que Deseja EXCLUIR: '))

    with open('Tasks.txt', 'r') as arquivo:
      tarefas = arquivo.readlines()
      
      if len(tarefas) == 1:
        import os
        os.remove('Tasks.txt')
      else:
        tarefas_atualizadas = []
        tarefa_excluida = False
        for tarefa in tarefas:
          nome, data = tarefa.strip().split(',')
          if nome.strip() == name_delet_task:
            tarefa_excluida = True
            print(f'\n  Tarefa "{name_delet_task}" excluída com sucesso!\n')
          else:
            tarefas_atualizadas.append(tarefa)
        if not tarefa_excluida:
          print(f'\n  Tarefa "{name_delet_task}" não encontrada no sistema.\n')
    
        with open('Tasks.txt', 'w') as arquivo:
          arquivo.writelines(tarefas_atualizadas)
          

def display_task():
  try:
    with open('Tasks.txt', 'r') as arquivo:
      tarefas = arquivo.readlines()
  except FileNotFoundError:
    print('\n  Não a TareFas\n')
  else:
    print("=-" * 20)
    with open('Tasks.txt', 'r') as arquivo:
      tarefas = arquivo.readlines()
      if tarefas:
        print("Tarefas:")
        for tarefa in tarefas:
          nome, data = tarefa.strip().split(',')
          print(f"  - {nome} (Vencimento: {data})")   
    print("-=" * 20)


while True:

  print('1 - Adicionar Uma Tarefa')
  print('2 - Excluir Tarefa')
  print('3 - Exibir Tabela')
  print('4 - Sair')
  
  try:
    choice = int(input('Escolha o Numero: '))
  except ValueError:
    print('\n  Apenas Numero\n')
  else:
    if choice == 1:
      add_task()
    elif choice == 2:
      delet_task()
    elif choice == 3:
      display_task()
    elif choice == 4:
      print('  Irei te Lembrar')
      break
    else:
      print('  Nao a Esta Escolha Tente Novamente')
    
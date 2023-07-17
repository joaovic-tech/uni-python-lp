employee_list = []
global_id = 0

def register_employee(id):
    name = input("Digite o nome do colaborador: ")
    department = input("Digite o setor do colaborador: ")
    payment = float(input("Digite o pagamento do colaborador: "))

    employee = {
        "id": id,
        "name": name,
        "department": department,
        "payment": payment
    }

    employee_list.append(employee)
    print("Colaborador cadastrado com sucesso!")

def search_employee():
    print('-' * 49 + 'MENU CONSUlTAS' + '-' * 49)
    print("1. Consultar Todos")
    print("2. Consultar por Id")
    print("3. Consultar por Setor")
    print("4. Retornar ao menu")
    option = input("Qual opção deseja? (1, 2, 3 ou 4): ")

    if option == "1":
        print("Todos os colaboradores:")
        for employee in employee_list:
            print(employee)

    elif option == "2":
        id_search = int(input("Digite o ID do colaborador a ser consultado: "))
        for employee in employee_list:
            if employee["id"] == id_search:
                print("Colaborador encontrado:")
                print(employee)
                break
        else:
            print("Colaborador não encontrado.")


    elif option == "3":
        department_search = input("Digite o setor dos colaboradores a serem consultados: ")
        print(f"Colaboradores do setor '{department_search}':")
        for employee in employee_list:
            if employee["department"] == department_search:
                print(employee)


    elif option == "4":
        return

    else:
        print("Opção inválida.")

    search_employee()  # Chama a função novamente para voltar ao menu

def remove_employee():
    id_remove = int(input("Digite o ID do colaborador a ser removido: "))

    for employee in employee_list:
        if employee["id"] == id_remove:
            employee_list.remove(employee)
            print("Colaborador removido com sucesso!")
            break
    else:
        print("Colaborador não encontrado.")

def main():
    global global_id
    print('-' * 114)
    print('-' * 20 + '( Seja bem-vindo(a) ao sistema de cadastro do João Victor Carvalho Alves )' + '-' * 20)
    while True:
        print('-' * 49 + '(MENU PRINCIPAL)' + '-' * 49)
        print("1. Cadastrar Colaborador")
        print("2. Consultar Colaborador")
        print("3. Remover Colaborador")
        print("4. Encerrar Programa")

        option = input("Digite a opção desejada: ")

        if option == "1":
            global_id += 1
            register_employee(global_id)

        elif option == "2":
            search_employee()

        elif option == "3":
            remove_employee()

        elif option == "4":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida.")

# Teste do programa
main()

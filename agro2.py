import datetime


desperdicio_alimentos = []

def registrar_desperdicio(fase_produtiva, descricao, impacto):
    try:
        data_registro = datetime.datetime.now()
        registro = {
            "fase_produtiva": fase_produtiva,
            "descricao": descricao,
            "impacto": impacto,
            "data_registro": data_registro
        }
        desperdicio_alimentos.append(registro)
        print("Dados registrados com sucesso!")
    except Exception as e:
        print(f"Erro ao registrar os dados: {e}")

def exibir_dados():
    try:
        if desperdicio_alimentos:
            print("\nRegistros de Desperdício de Alimentos:")
            for idx, registro in enumerate(desperdicio_alimentos, 1):
                print(f"ID: {idx}, Fase: {registro['fase_produtiva']}, Descrição: {registro['descricao']}, Impacto: {registro['impacto']}, Data: {registro['data_registro']}")
        else:
            print("Nenhum dado registrado ainda.")
    except Exception as e:
        print(f"Erro ao consultar os dados: {e}")

def remover_dado():
    try:
        if desperdicio_alimentos:
            exibir_dados()
            id_remover = int(input("Informe o ID do registro que deseja remover: "))
            if 1 <= id_remover <= len(desperdicio_alimentos):
                desperdicio_alimentos.pop(id_remover - 1)
                print("Registro removido com sucesso!")
            else:
                print("ID inválido. Tente novamente.")
        else:
            print("Nenhum dado registrado para remover.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.")
    except Exception as e:
        print(f"Erro ao remover o dado: {e}")

def main():
    while True:
        print("\nMenu de Desperdício de Alimentos:")
        print("1. Registrar novo desperdício")
        print("2. Ver registros de desperdício")
        print("3. Remover um registro de desperdício")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            fase = input("Informe a fase produtiva (ex: Plantio, Transporte, Comercialização): ")
            descricao = input("Descreva o tipo de desperdício: ")
            impacto = float(input("Informe o impacto (em números, ex: 10.5): "))
            registrar_desperdicio(fase, descricao, impacto)
        elif escolha == '2':
            exibir_dados()
        elif escolha == '3':
            remover_dado()
        elif escolha == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()

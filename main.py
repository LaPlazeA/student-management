import os

from alunos_mod import cadastrar, editar, remover
from listagem_mod import listar_geral, listar_por_sexo, listar_por_curso


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


while True:

    limpar_tela()

    modo = int(input(
        "TI Cursos\n\n"
        "1 - Cadastrar Aluno\n"
        "2 - Editar Aluno\n"
        "3 - Remover Aluno\n"
        "4 - Listagem Geral\n"
        "5 - Listagem por sexo\n"
        "6 - Listagem por curso\n"
        "0 - Sair\n\n"
        "Opção: "
    ))

    limpar_tela()

    if modo == 1:
        cadastrar()

    elif modo == 2:
        editar()

    elif modo == 3:
        remover()

    elif modo == 4:
        listar_geral()

    elif modo == 5:
        listar_por_sexo()

    elif modo == 6:
        listar_por_curso()

    elif modo == 0:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")

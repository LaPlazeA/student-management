import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(BASE_DIR, "cadastro.json")

def cadastrar():

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            alunos = json.load(arquivo)
            if not isinstance(alunos, list):
                alunos = []
    except:
        alunos = []

    matricula = int(input("matricula do aluno: "))

    # verifica matrícula duplicada
    for a in alunos:
        if a["matricula"] == matricula:
            print("ERRO: matrícula já cadastrada!")
            return

    aluno = {
        "matricula": matricula,
        "nome": input("nome do aluno: "),
        "sexo": input("sexo do aluno(F/M): "),
        "idade": int(input("idade do aluno: ")),
        "turno": int(input("Turno (1-manha/2-noite): ")),
        "cursos": [],
    }

    while True:
        curso = int(input("(1-PHP / 2-Java / 3-Python): "))
        aluno["cursos"].append(curso)

        continuar = int(input("Deseja cadastrar outro curso? (1-Sim / 2-Não): "))
        if continuar != 1:
            break

    alunos.append(aluno)

    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)

    print("Aluno salvo com sucesso!")



def editar():

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            alunos = json.load(arquivo)
    except:
        print("Nenhum aluno cadastrado.")
        return

    matricula = int(input("Digite a matrícula do aluno: "))

    for aluno in alunos:

        if aluno["matricula"] == matricula:

            print("\nALUNO ENCONTRADO\n")

            print("Nome:", aluno["nome"])
            aluno["nome"] = input("Novo nome: ")

            print("Sexo:", aluno["sexo"])
            aluno["sexo"] = input("Novo sexo(F/M): ")

            print("Idade:", aluno["idade"])
            aluno["idade"] = int(input("Nova idade: "))

            print("Turno:", aluno["turno"])
            aluno["turno"] = int(input("Novo turno (1-manha/2-noite): "))

            print("Cursos:", aluno["cursos"])

            alterar = input("Deseja alterar os cursos? (1-Sim / 2-Não): ")

            if alterar == "1":

                aluno["cursos"] = []

                while True:

                    curso = int(input("(1-PHP / 2-Java / 3-Python): "))
                    aluno["cursos"].append(curso)

                    continuar = input("Adicionar outro curso? (1-Sim / 2-Não): ")

                    if continuar != "1":
                        break

            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                json.dump(alunos, arquivo, ensure_ascii=False, indent=4)

            print("\nAluno atualizado com sucesso!")
            return

    print("Matrícula não encontrada.")



def remover():

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            alunos = json.load(arquivo)

    except:
        print("Nenhum aluno cadastrado.")
        return

    matricula = int(input("Digite a matrícula do aluno que deseja remover: "))

    encontrado = False

    for aluno in alunos:

        if aluno["matricula"] == matricula:

            encontrado = True

            print("\nAluno encontrado:")
            print(f"Nome: {aluno['nome']}")
            print(f"Matrícula: {aluno['matricula']}")

            confirmar = int(input(
                "\nConfirma exclusão?\n"
                "1-Sim\n"
                "2-Não\n"
            ))

            if confirmar == 1:

                alunos.remove(aluno)

                with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                    json.dump(alunos, arquivo, ensure_ascii=False, indent=4)

                print("Aluno removido com sucesso!")

            else:
                print("Exclusão cancelada.")

            break

    if not encontrado:
        print("Matrícula não encontrada.")
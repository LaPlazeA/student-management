import json
import os
from mensalidade_mod import calcular_mensalidade

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO = os.path.join(BASE_DIR, "cadastro.json")

def listar_geral():

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            alunos = json.load(arquivo)

    except:
        print("Nenhum aluno cadastrado.")
        return

    # nomes dos cursos
    nomes_cursos = {
        1: "PHP",
        2: "Java",
        3: "Python"
    }

    print("\n")
    print("=" * 80)
    print("                    TELA DA LISTAGEM GERAL")
    print("=" * 80)

    print(
        f"{'Matricula':<12}"
        f"{'Nome':<20}"
        f"{'Sexo':<8}"
        f"{'Idade':<8}"
        f"{'Cursos':<20}"
        f"{'Mensalidade':<12}"
    )

    print("-" * 80)

    for aluno in alunos:

        cursos = []

        for curso in aluno["cursos"]:
            cursos.append(nomes_cursos.get(curso, "Desconhecido"))

        cursos_texto = " / ".join(cursos)

        mensalidade = calcular_mensalidade(
            aluno["cursos"],
            aluno["turno"],
            aluno["idade"]
        )

        print(
            f"{aluno['matricula']:<12}"
            f"{aluno['nome']:<20}"
            f"{aluno['sexo']:<8}"
            f"{aluno['idade']:<8}"
            f"{cursos_texto:<20}"
            f"R$ {mensalidade:.2f}"
        )

    print("=" * 80)

    input("\nTecle ENTER para voltar ao menu...")




def listar_por_sexo():

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            alunos = json.load(arquivo)

    except:
        print("Nenhum aluno cadastrado.")
        input("\nClique ENTER para voltar ao menu...")
        return

    sexo_busca = input("Digite o sexo (F/M): ").upper()

    nomes_cursos = {
        1: "PHP",
        2: "Java",
        3: "Python"
    }

    encontrados = False

    print("\n" + "=" * 80)
    print("                LISTAGEM POR SEXO")
    print("=" * 80)

    print(
        f"{'Matricula':<12}"
        f"{'Nome':<20}"
        f"{'Sexo':<8}"
        f"{'Idade':<8}"
        f"{'Cursos':<25}"
    )

    print("-" * 80)

    for aluno in alunos:

        if aluno["sexo"].upper() == sexo_busca:

            cursos = [nomes_cursos.get(c, "Desconhecido") for c in aluno["cursos"]]
            cursos_texto = " / ".join(cursos)

            print(
                f"{aluno['matricula']:<12}"
                f"{aluno['nome']:<20}"
                f"{aluno['sexo']:<8}"
                f"{aluno['idade']:<8}"
                f"{cursos_texto:<25}"
            )

            encontrados = True

    print("=" * 80)

    if not encontrados:
        print("Nenhum aluno encontrado com esse sexo.")

    input("\nClique ENTER para voltar ao menu...")




def listar_por_curso():

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            alunos = json.load(arquivo)

    except:
        print("Nenhum aluno cadastrado.")
        input("\nClique ENTER para voltar ao menu...")
        return

    nomes_cursos = {
        1: "PHP",
        2: "Java",
        3: "Python"
    }

    curso_busca = int(input(
        "\nDigite o curso:\n"
        "1-PHP\n"
        "2-Java\n"
        "3-Python\n"
    ))

    encontrados = False

    print("\n" + "=" * 80)
    print("                LISTAGEM POR CURSO")
    print("=" * 80)

    print(
        f"{'Matricula':<12}"
        f"{'Nome':<20}"
        f"{'Sexo':<8}"
        f"{'Idade':<8}"
        f"{'Cursos':<25}"
    )

    print("-" * 80)

    for aluno in alunos:

        if curso_busca in aluno["cursos"]:

            cursos = [nomes_cursos.get(c, "Desconhecido") for c in aluno["cursos"]]
            cursos_texto = " / ".join(cursos)

            print(
                f"{aluno['matricula']:<12}"
                f"{aluno['nome']:<20}"
                f"{aluno['sexo']:<8}"
                f"{aluno['idade']:<8}"
                f"{cursos_texto:<25}"
            )

            encontrados = True

    print("=" * 80)

    if not encontrados:
        print("Nenhum aluno encontrado nesse curso.")

    input("\nClique ENTER para voltar ao menu...")
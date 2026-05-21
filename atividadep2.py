import json
import os
from datetime import datetime

ARQUIVO = "treinos.txt"

#  salvar e carregar dados

def carregar_treinos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_treinos(treinos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(treinos, f, ensure_ascii=False, indent=4)

#  UTILITÁRIOS


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def cabecalho():
    print("=" * 50)
    print("        💪  FitTask – Gerenciador de Treinos")
    print("=" * 50)

def pausar():
    input("\nPressione ENTER para continuar...")

def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validar_hora(hora_str):
    try:
        datetime.strptime(hora_str, "%H:%M")
        return True
    except ValueError:
        return False

def proximo_id(treinos):
    if not treinos:
        return 1
    return max(t["id"] for t in treinos) + 1

#  ADICIONAR TREINO

def adicionar_treino(treinos):
    limpar_tela()
    cabecalho()
    print("\n  ➕  ADICIONAR TREINO\n")

    nome = input("  Nome do treino (ex: Peito e Tríceps): ").strip()
    if not nome:
        print("\n  ⚠️  Nome não pode ser vazio.")
        pausar()
        return

    while True:
        data = input("  Data (DD/MM/AAAA): ").strip()
        if validar_data(data):
            break
        print("  ⚠️  Data inválida. Use o formato DD/MM/AAAA.")

    while True:
        hora = input("  Horário (HH:MM): ").strip()
        if validar_hora(hora):
            break
        print("  ⚠️  Horário inválido. Use o formato HH:MM.")

    grupo = input("  Grupo muscular (ex: Peitoral, Costas, Pernas): ").strip()
    exercicios = input("  Exercícios (ex: Supino, Crucifixo, Tríceps): ").strip()

    treino = {
        "id": proximo_id(treinos),
        "nome": nome,
        "data": data,
        "hora": hora,
        "grupo_muscular": grupo,
        "exercicios": exercicios,
        "concluido": False
    }

    treinos.append(treino)
    salvar_treinos(treinos)

    print(f"\n  ✅  Treino '{nome}' adicionado com sucesso! (ID: {treino['id']})")
    pausar()

#  LISTAR TREINOS

def listar_treinos(treinos):
    limpar_tela()
    cabecalho()
    print("\n  📋  LISTA DE TREINOS\n")

    if not treinos:
        print("  Nenhum treino cadastrado ainda.")
        pausar()
        return

    ordenados = sorted(treinos, key=lambda t: (
        datetime.strptime(t["data"], "%d/%m/%Y"),
        t["hora"]
    ))

    for t in ordenados:
        status = "✅ Concluído" if t["concluido"] else "⏳ Pendente"
        print(f"  {'─'*46}")
        print(f"  ID: {t['id']}  |  {status}")
        print(f"  📌 {t['nome']}")
        print(f"  📅 {t['data']}  🕐 {t['hora']}")
        print(f"  💪 Grupo: {t['grupo_muscular']}")
        print(f"  🏋️  Exercícios: {t['exercicios']}")
    print(f"  {'─'*46}")
    print(f"\n  Total: {len(treinos)} treino(s)")
    pausar()

#  EDITAR TREINO

def editar_treino(treinos):
    limpar_tela()
    cabecalho()
    print("\n  ✏️   EDITAR TREINO\n")

    if not treinos:
        print("  Nenhum treino cadastrado.")
        pausar()
        return

    try:
        id_busca = int(input("  Digite o ID do treino que deseja editar: "))
    except ValueError:
        print("  ⚠️  ID inválido.")
        pausar()
        return

    treino = next((t for t in treinos if t["id"] == id_busca), None)
    if not treino:
        print(f"  ⚠️  Treino com ID {id_busca} não encontrado.")
        pausar()
        return

    print(f"\n  Editando: {treino['nome']} ({treino['data']} às {treino['hora']})")
    print("  Deixe em branco para manter o valor atual.\n")

    novo_nome = input(f"  Nome [{treino['nome']}]: ").strip()
    if novo_nome:
        treino["nome"] = novo_nome

    while True:
        nova_data = input(f"  Data [{treino['data']}]: ").strip()
        if nova_data == "":
            break
        if validar_data(nova_data):
            treino["data"] = nova_data
            break
        print("  ⚠️  Data inválida. Use DD/MM/AAAA.")

    while True:
        nova_hora = input(f"  Hora [{treino['hora']}]: ").strip()
        if nova_hora == "":
            break
        if validar_hora(nova_hora):
            treino["hora"] = nova_hora
            break
        print("  ⚠️  Hora inválida. Use HH:MM.")

    novo_grupo = input(f"  Grupo muscular [{treino['grupo_muscular']}]: ").strip()
    if novo_grupo:
        treino["grupo_muscular"] = novo_grupo

    novos_ex = input(f"  Exercícios [{treino['exercicios']}]: ").strip()
    if novos_ex:
        treino["exercicios"] = novos_ex

    salvar_treinos(treinos)
    print(f"\n  ✅  Treino atualizado com sucesso!")
    pausar()

#  REMOVER TREINO

def remover_treino(treinos):
    limpar_tela()
    cabecalho()
    print("\n  🗑️   REMOVER TREINO\n")

    if not treinos:
        print("  Nenhum treino cadastrado.")
        pausar()
        return

    try:
        id_busca = int(input("  Digite o ID do treino que deseja remover: "))
    except ValueError:
        print("  ⚠️  ID inválido.")
        pausar()
        return

    treino = next((t for t in treinos if t["id"] == id_busca), None)
    if not treino:
        print(f"  ⚠️  Treino com ID {id_busca} não encontrado.")
        pausar()
        return

    confirmacao = input(f"  Tem certeza que deseja remover '{treino['nome']}'? (s/n): ").strip().lower()
    if confirmacao == "s":
        treinos.remove(treino)
        salvar_treinos(treinos)
        print(f"\n  ✅  Treino removido com sucesso!")
    else:
        print("  ❌  Remoção cancelada.")
    pausar()

#  MARCAR COMO CONCLUÍDO

def marcar_concluido(treinos):
    limpar_tela()
    cabecalho()
    print("\n  ✅  MARCAR TREINO COMO CONCLUÍDO\n")

    if not treinos:
        print("  Nenhum treino cadastrado.")
        pausar()
        return

    pendentes = [t for t in treinos if not t["concluido"]]
    if not pendentes:
        print("  Todos os treinos já estão concluídos! 🎉")
        pausar()
        return

    print("  Treinos pendentes:\n")
    for t in pendentes:
        print(f"  ID {t['id']:>3}  |  {t['data']}  {t['hora']}  |  {t['nome']}")

    try:
        id_busca = int(input("\n  Digite o ID do treino concluído: "))
    except ValueError:
        print("  ⚠️  ID inválido.")
        pausar()
        return

    treino = next((t for t in treinos if t["id"] == id_busca), None)
    if not treino:
        print(f"  ⚠️  Treino com ID {id_busca} não encontrado.")
    elif treino["concluido"]:
        print("  ⚠️  Este treino já está marcado como concluído.")
    else:
        treino["concluido"] = True
        salvar_treinos(treinos)
        print(f"\n  🎉  '{treino['nome']}' marcado como concluído!")
    pausar()

#  BUSCAR POR DATA

def buscar_por_data(treinos):
    limpar_tela()
    cabecalho()
    print("\n  🔍  BUSCAR TREINOS POR DATA\n")

    while True:
        data = input("  Digite a data (DD/MM/AAAA): ").strip()
        if validar_data(data):
            break
        print("  ⚠️  Data inválida. Use DD/MM/AAAA.")

    resultado = [t for t in treinos if t["data"] == data]

    if not resultado:
        print(f"\n  Nenhum treino encontrado para {data}.")
    else:
        print(f"\n  {len(resultado)} treino(s) encontrado(s) para {data}:\n")
        for t in resultado:
            status = "✅ Concluído" if t["concluido"] else "⏳ Pendente"
            print(f"  {'─'*46}")
            print(f"  ID: {t['id']}  |  {status}")
            print(f"  📌 {t['nome']}  🕐 {t['hora']}")
            print(f"  💪 Grupo: {t['grupo_muscular']}")
            print(f"  🏋️  Exercícios: {t['exercicios']}")
        print(f"  {'─'*46}")
    pausar()

#  MENU PRINCIPAL


def menu():
    treinos = carregar_treinos()

    while True:
        limpar_tela()
        cabecalho()

        concluidos = sum(1 for t in treinos if t["concluido"])
        pendentes  = len(treinos) - concluidos

        print(f"\n  📊  Total: {len(treinos)} treino(s)  |  "
              f"✅ {concluidos} concluído(s)  |  ⏳ {pendentes} pendente(s)\n")
        print("  [1]  Adicionar Treino")
        print("  [2]  Listar Treinos")
        print("  [3]  Editar Treino")
        print("  [4]  Remover Treino")
        print("  [5]  Marcar como Concluído")
        print("  [6]  Buscar por Data")
        print("  [0]  Sair")
        print("\n" + "=" * 50)

        opcao = input("  Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_treino(treinos)
        elif opcao == "2":
            listar_treinos(treinos)
        elif opcao == "3":
            editar_treino(treinos)
        elif opcao == "4":
            remover_treino(treinos)
        elif opcao == "5":
            marcar_concluido(treinos)
        elif opcao == "6":
            buscar_por_data(treinos)
        elif opcao == "0":
            limpar_tela()
            print("\n  Até logo! Continue treinando! 💪\n")
            print("=" * 50)
            print("  Desenvolvido por:")
            print("    • Gustavo Matias")
            print("    • Lucas Faelis Carlos")
            print("    • Miguel Lumitti")
            print("    • Rafael Carracci")
            print("=" * 50 + "\n")
            break
        else:
            print("\n  ⚠️  Opção inválida. Tente novamente.")
            pausar()

if __name__ == "__main__":
    menu()

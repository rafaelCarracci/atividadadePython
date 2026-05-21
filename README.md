# 💪 FitTask — Gerenciador de Treinos

> Aplicação de linha de comando para organizar, acompanhar e gerenciar sua rotina de treinos com simplicidade e eficiência.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Como Usar](#-como-usar)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Autores](#-autores)

---

## 🏋️ Sobre o Projeto

O **FitTask** é um gerenciador de treinos para terminal desenvolvido em Python. Ele permite cadastrar, editar, listar e acompanhar seus treinos de academia de forma prática, sem depender de aplicativos ou internet. Os dados são salvos localmente em formato JSON, garantindo persistência entre sessões.

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| ➕ Adicionar Treino | Cadastra nome, data, horário, grupo muscular e exercícios |
| 📋 Listar Treinos | Exibe todos os treinos ordenados por data e horário |
| ✏️ Editar Treino | Atualiza qualquer campo de um treino existente |
| 🗑️ Remover Treino | Remove um treino pelo ID com confirmação |
| ✅ Marcar como Concluído | Registra a conclusão de um treino pendente |
| 🔍 Buscar por Data | Filtra treinos por uma data específica |

---

## 🛠️ Tecnologias

- **Python 3.x** — linguagem principal
- **json** — persistência de dados local
- **datetime** — validação de datas e horários
- **os** — limpeza de tela e verificação de arquivos

Sem dependências externas. Funciona com Python puro.

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.6 ou superior instalado
- Terminal (Prompt de Comando, PowerShell, Bash etc.)

### Instalação e Execução

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/fittask.git

# Acesse a pasta do projeto
cd fittask

# Execute a aplicação
python main.py
```

### Navegação no Menu

Após iniciar, o menu principal será exibido:

```
==================================================
        💪  FitTask – Gerenciador de Treinos
==================================================

  📊  Total: 3 treino(s)  |  ✅ 1 concluído(s)  |  ⏳ 2 pendente(s)

  [1]  Adicionar Treino
  [2]  Listar Treinos
  [3]  Editar Treino
  [4]  Remover Treino
  [5]  Marcar como Concluído
  [6]  Buscar por Data
  [0]  Sair
```

Digite o número da opção desejada e pressione **ENTER**.

### Exemplo de Cadastro

```
  Nome do treino: Peito e Tríceps
  Data (DD/MM/AAAA): 20/05/2025
  Horário (HH:MM): 07:30
  Grupo muscular: Peitoral, Tríceps
  Exercícios: Supino reto, Crucifixo, Tríceps corda
```

---

## 📁 Estrutura do Projeto

```
fittask/
│
├── main.py          # Código principal da aplicação
├── treinos.txt      # Arquivo de dados (gerado automaticamente)
└── README.md        # Documentação do projeto
```

> O arquivo `treinos.txt` é criado automaticamente na primeira execução e armazena os dados em formato JSON.

---

## 👥 Autores

Desenvolvido como projeto acadêmico por:

| Nome | GitHub |
|---|---|
| Gustavo Matias | [@gustavo]([https://github.com/](https://github.com/gus-ms) |
| Lucas Faelis | [@lucas]([https://github.com/](https://github.com/Khaosxxx) |
| Miguel Lumitti | [@miguel](https://github.com/) |
| Rafael Carracci | [@rafael]([https://github.com/](https://github.com/rafaelCarracci) |

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

<p align="center">Feito com 💪 e Python</p>

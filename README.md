#  Sistema Bancário em Python

Projeto desenvolvido como parte do **Desafio Back-End com Python (Santander 2025)** da plataforma **DIO**.

## 📋 Descrição

Este é um sistema bancário básico, criado em Python, com funcionalidades essenciais como:

[Atividade 1]
- Depósito de valores
- Saque com limite diário
- Visualização de extrato

[Atividade 2]

- Criar conta
- Listar conta
- Criar usuário
O objetivo é simular uma aplicação de terminal simples e robusta, praticando os fundamentos da linguagem Python e lógica de programação.

[Atividade 3]

- Usar a biblioteca datatime
- Impor um limite diário de transações

---

## ⚙️ Funcionalidades

- **Depositar**
  - Aceita apenas valores positivos.
  - Atualiza o extrato automaticamente.

- **Sacar**
  - Limite de **3 saques por dia**.
  - Valor máximo por saque: **R$ 500,00**.
  - Verificação de saldo suficiente e valor válido.

- **Extrato**
  - Lista todas as operações (saques e depósitos).
  - Exibe o saldo final formatado.

- **Criar Conta**
    - Usuário é composto por: Nome, Data de Nascimento, CPF e Endereço
    - 1 CPF por usuário
- **Criar conta corrente**
    - Agência, número da conta e usuário
    - O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário

---

##  Tecnologias utilizadas

- [Python 3.10+](https://www.python.org/)
- Módulo `os` para limpar a tela (compatível com Windows e Linux/macOS)

---

## Aprendizados

Com este projeto foi possível praticar:

- Estruturas de controle (if, while, try/except)
- Manipulação de listas e tuplas
- Criação de funções com múltiplos parâmetros e retorno
- Organização de código e boas práticas
- Manipilação de dicionários




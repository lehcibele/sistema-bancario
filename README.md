# Sistema Bancário - Desafio Bootcamp Santander 2025 (Back-end com Python)

Este projeto é uma implementação simples de um sistema bancário, desenvolvido como parte do desafio do Bootcamp Santander 2025 na trilha de Back-end com Python.

## Descrição do Projeto

O sistema simula operações básicas de uma conta bancária para um único usuário, sem a necessidade de gerenciamento de múltiplas contas ou agências.

As operações disponíveis são:

- **Depósito:** permite depositar valores positivos na conta. Todos os depósitos são registrados e exibidos no extrato.
- **Saque:** permite realizar até 3 saques diários, com limite máximo de R$500,00 por saque. Caso o saldo seja insuficiente, o saque não é autorizado e uma mensagem é exibida. Os saques realizados são registrados e exibidos no extrato.
- **Extrato:** exibe o histórico completo de depósitos e saques, além do saldo atual da conta. Os valores são formatados no padrão monetário brasileiro (R$).

## Regras do Sistema

- Depósitos devem ser valores positivos.
- Máximo de 3 saques por dia.
- Limite máximo de saque por operação: R$500,00.
- Saques só são permitidos se houver saldo suficiente.

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/lehcibele/sistema-bancario.git
2. Navegue até a pasta do projeto:
    ```bash
    cd sistema-bancario-python
3. Execute o programa:
    ```bash
    python sistema_bancario.py
4. Siga as instruções no terminal para realizar depósitos, saques e consultar o extrato.

## Tecnologias Utilizadas
- Python

## Estrutura do Projeto
- sistema_bancario.py — arquivo principal com a lógica do sistema bancário.
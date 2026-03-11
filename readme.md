# Exercícios de Python: LLMs, SLMs e Tool Calling

Este repositório contém exercícios práticos em Python que demonstram o uso de *tool calling* (chamada de ferramentas/funções) com os modelos da Groq. Cada exercício foca em um caso de uso específico, desde aritmética simples até consulta de clima e agendamento.

## Objetivos de Aprendizado

- Expor funções em Python como ferramentas que podem ser chamadas (callable tools)
- Permitir que o modelo escolha a função correta a partir de uma entrada em linguagem natural
- Fazer o *parsing* dos argumentos das ferramentas retornados pelo modelo
- Manter a lógica de orquestração separada da lógica de domínio (`tools.py`)

## Estrutura do Projeto

| Exercício | Cenário                                           | Script de Entrada               |
| --------- | ------------------------------------------------- | ------------------------------- |
| Ex1       | Calculadora básica (soma e multiplicação)         | `Ex1/calculadoraSimples.py`     |
| Ex2       | Calculadora completa (soma, sub, mult, div)       | `Ex2/calculadoraCompleta.py`    |
| Ex3       | Conversão de temperatura                          | `Ex3/conversaoDeTemperatura.py` |
| Ex4       | Consulta de preço de produto                      | `Ex4/consultaDeProduto.py`      |
| Ex5       | Verificação de estoque                            | `Ex5/veridicacaoDeEstoque.py`   |
| Ex6       | Sistema de agenda                                 | `Ex6/sistemaDeAgenda.py`        |
| Ex7       | Consulta de clima                                 | `Ex7/consultaDeClima.py`        |

Cada pasta de exercício inclui:

- um script de entrada com a orquestração de *tool-calling* da Groq
- um arquivo `tools.py` contendo as funções executáveis do domínio

## Tecnologias Utilizadas

- Python 3
- [groq](https://pypi.org/project/groq/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Pré-requisitos

- Python 3.11 ou mais recente
- Uma chave de API válida da Groq

## Configuração

A partir da raiz do repositório:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install groq python-dotenv

Crie seu arquivo de ambiente e defina sua chave de API:
Copy-Item .env.example .env

Em seguida, edite o .env e defina:
GROQ_API_KEY=sua_chave_de_api_real_da_groq
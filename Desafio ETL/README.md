# Bootcamp Santander - Pipeline ETL com Python

Este projeto é um desafio de Engenharia de Dados proposto no Santander Dev Week 2023. Como a API original do desafio foi descontinuada, desenvolvi minha própria API local para simular o ambiente completo.

## Objetivo
Construir um pipeline ETL (Extract, Transform, Load) que:
1.  **Extrai** dados de usuários de uma API (simulada localmente).
2.  **Transforma** os dados (neste caso, a lógica simula a geração de mensagens de marketing personalizadas, mas está preparada para integração com IA Generativa/OpenAI).
3.  **Carrega** os dados transformados de volta na API.

## Tecnologias Utilizadas
* **Python 3**
* **FastAPI**: Para criar a API simulada e expor os endpoints de dados.
* **Pandas**: Manipulação e transformação de dados em DataFrames (ETL).
* **Requests**: Consumo da API Rest.
* **JSON**: Como banco de dados simples (Simulação de DB).

## Estrutura do Projeto
* `api.py`: Código da API criada com FastAPI.
* `db.json`: "Banco de dados" local onde as informações dos usuários ficam salvas.
* `etl.py`: Script de pipeline que executa o processo de Extração, Transformação e Carga.
* `README.md`: Este arquivo! Documentando algumas coisas e falando sobre o que foi feito, e tecnologias utilizadas.

## Imagens do terminal mostrando o código sendo executado com sucesso
### ETL executado com Sucesso
![ETL](/Desafio%20ETL/img/ETL%20Sucesso.png)
### API executado com Sucesso
![API](/Desafio%20ETL/img/API%20Sucesso.png)
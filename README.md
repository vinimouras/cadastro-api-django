# 🚀 Desafio Backend - Python & Django

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django REST Framework](https://img.shields.io/badge/Django%20REST-Framework-green?logo=django&logoColor=white)](https://www.django-rest-framework.org/)

## 🛠️ Tecnologias Utilizadas

- 🐍 Python
- 🌐 Django REST Framework

## 📌 Descrição do Projeto

Este projeto consiste em uma **API simples de cadastro de clientes**, desenvolvida com Django.

A aplicação contém as seguintes funcionalidades:

- 📇 Cadastro, edição e listagem de clientes.
- 🔍 Validação de **CPF**.
- 🏡 Verificação de **CEP** com integração a serviço externo.

## 🔗 Endpoints da API

| Método   | URL                             | Nome da URL       | Descrição                    |
|----------|----------------------------------|-------------------|------------------------------|
| `POST`   | `/clients/`                      | `client-create`   | Inserir novo cliente         |
| `GET`    | `/clients/<int:id>/`             | `client-detail`   | Detalhar cliente específico  |
| `PUT`    | `/clients/<int:id>/update/`      | `client-update`   | Atualizar dados do cliente   |
| `DELETE` | `/clients/<int:id>/delete/`      | `clients-delete`  | Remover cliente do sistema   |

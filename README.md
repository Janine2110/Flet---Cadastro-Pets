# 🐾 Sistema de Cadastro de Petshop

Este é um sistema simples de cadastro de animais de um petshop, desenvolvido em Python com a biblioteca [Flet](https://flet.dev/), utilizando uma API REST local via [JSON Server](https://github.com/typicode/json-server).

## ✨ Funcionalidades

- 📋 **Cadastro de Pets**: Registra nome, espécie, raça, peso.
- 📑 **Listagem de Pets**: Exibe todos os pets cadastrados em uma tabela dinâmica.
- 🔍 **Filtro de Pets**: Permite buscar pets por nome e espécie.
- 📊 **Gráfico por Espécie**: Exibe um gráfico de barras com a quantidade de pets por espécie.

---

## 🧱 Estrutura de Telas

### 📁 `telas/cad_pets.py`
Tela principal de **cadastro de pets**:
- Formulário para inserir os dados do pet.
- Tabela com todos os pets cadastrados.
- Botões de envio e limpeza dos campos.

### 📁 `telas/filtro_pets.py`
Tela para **filtro de pets** por nome e espécie:
- Campos de busca por nome e espécie.
- Resultados exibidos dinamicamente.

### 📁 `telas/graf_especies.py`
Tela de **gráfico**:
- Gráfico de barras com número de pets agrupados por espécie.
- Utiliza dados retornados da API.

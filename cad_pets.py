# telas/cad_pets.py
import flet as ft
import requests

API_PETS = "http://localhost:3000/pets"
API_CLIENTES = "http://localhost:3000/clientes"

def cad_pets(page: ft.Page):
    txt_nome = ft.TextField(label="Nome do Pet", expand=3)
    txt_especie = ft.TextField(label="Espécie", expand=2)
    txt_raca = ft.TextField(label="Raça", expand=3)
    txt_peso = ft.TextField(label="Peso (kg)", expand=1)

    dropdown_dono = ft.Dropdown(label="Dono do Pet", options=[])

    def carregar_donos():
        try:
            response = requests.get(API_CLIENTES)
            response.raise_for_status()
            clientes = response.json()
            dropdown_dono.options = [
                ft.dropdown.Option(str(c["id"]), f'{c["nome"]} ({c["telefone"]})') for c in clientes
            ]
        except Exception as e:
            page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao carregar donos: {e}"))
            page.snack_bar.open = True
            page.update()

    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Espécie")),
            ft.DataColumn(ft.Text("Raça")),
            ft.DataColumn(ft.Text("Peso")),
            ft.DataColumn(ft.Text("Dono ID"))
        ],
        rows=[],
    )

    def carregar_pets():
        try:
            pets = requests.get(API_PETS).json()
            tabela.rows.clear()
            for p in reversed(pets):
                tabela.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(p["id"])),
                    ft.DataCell(ft.Text(p["nome"])),
                    ft.DataCell(ft.Text(p["especie"])),
                    ft.DataCell(ft.Text(p["raca"])),
                    ft.DataCell(ft.Text(str(p["peso"]))),
                    ft.DataCell(ft.Text(str(p["donoId"]))),
                ]))
            page.update()
            
        except Exception as e:
            page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao carregar pets: {e}"))
            page.snack_bar.open = True
            page.update()

    def enviar_click(e):
        if "" in [txt_nome.value, txt_especie.value, txt_raca.value, txt_peso.value, dropdown_dono.value]:
            page.snack_bar = ft.SnackBar(ft.Text("Preencha todos os campos!"))
            page.snack_bar.open = True
            page.update()
            return

        try:
            novo = {
                "nome": txt_nome.value,
                "especie": txt_especie.value,
                "raca": txt_raca.value,
                "peso": float(txt_peso.value.replace(",", ".")),
                "donoId": int(dropdown_dono.value)
            }
            requests.post(API_PETS, json=novo)
            page.snack_bar = ft.SnackBar(ft.Text("Pet cadastrado com sucesso!"))
            page.snack_bar.open = True
            txt_nome.value = txt_especie.value = txt_raca.value = txt_peso.value = ""
            dropdown_dono.value = None
            carregar_pets()
        except Exception as e:
            page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao cadastrar: {e}"))
            page.snack_bar.open = True
        page.update()

    layout = ft.Column([
        ft.Text("Cadastro de Pets", size=22, weight="bold"),
        ft.Row([txt_nome, txt_especie], spacing=10),
        ft.Row([txt_raca, txt_peso, dropdown_dono], spacing=10),
        ft.Row([
            ft.ElevatedButton("Cadastrar", on_click=enviar_click),
            ft.ElevatedButton("Limpar", on_click=lambda e: limpar_campos())
        ]),
        ft.Divider(),
        ft.Text("Pets Cadastrados:", size=18, weight="bold"),
        ft.Container(
            content=ft.Column([tabela], scroll=ft.ScrollMode.AUTO),
            height=400,
            padding=5,
            border=ft.border.all(1, ft.Colors.GREY_300),
            border_radius=10,
            bgcolor=ft.Colors.GREY_100
        )
    ])

    def limpar_campos():
        txt_nome.value = txt_especie.value = txt_raca.value = txt_peso.value = ""
        dropdown_dono.value = None
        page.update()

    carregar_donos()
    carregar_pets()

    return layout

import flet as ft
import requests

API_PETS = "http://localhost:3000/pets"

def filtro_pets(page):
    txt_nome = ft.TextField(label="Filtrar por Nome", expand=3)
    txt_especie = ft.TextField(label="Filtrar por Espécie", expand=2)

    resultado = ft.Column(spacing=5)

    def buscar(e):
        try:
            pets = requests.get(API_PETS).json()
            resultado.controls.clear()
            for p in pets:
                if txt_nome.value.lower() in p["nome"].lower() and txt_especie.value.lower() in p["especie"].lower():
                    resultado.controls.append(ft.Text(f'{p["nome"]} ({p["especie"]}) - Raça: {p["raca"]}, Peso: {p["peso"]}kg'))
            page.update()
        except Exception as err:
            resultado.controls = [ft.Text(f"Erro: {err}", color="red")]
            page.update()

    return ft.Column([
        ft.Text("Filtro de Pets por Nome e Espécie", size=22, weight="bold"),
        ft.Row([txt_nome, txt_especie, ft.ElevatedButton("Buscar", on_click=buscar)]),
        ft.Divider(),
        resultado
    ])

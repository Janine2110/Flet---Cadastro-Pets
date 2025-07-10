import flet as ft
import requests

API_PETS = "http://localhost:3000/pets"

def obter_pets_api():
    try:
        resposta = requests.get(API_PETS)
        resposta.raise_for_status()
        return resposta.json()
    except Exception as e:
        print(f"Erro ao buscar pets: {e}")
        return []

def graf_especies(page: ft.Page):

    pets = obter_pets_api()

    dicionario = {}
    for pet in pets:
        especie = pet.get("especie", "Desconhecida")
        if especie in dicionario:
            dicionario[especie] += 1
        else:
            dicionario[especie] = 1

    if not dicionario:
        return ft.Text("Nenhum pet cadastrado.")

    cores = [ft.Colors.BLUE, ft.Colors.GREEN, ft.Colors.ORANGE, ft.Colors.PURPLE, ft.Colors.RED]
    maior = max(dicionario.values())
    barras = []

    for i, (especie, qtd) in enumerate(dicionario.items()):
        largura = (qtd / maior) * 600
        barra = ft.Container(
            width=largura,
            height=30,
            bgcolor=cores[i % len(cores)],
            border_radius=5,
        )
        barras.append(
            ft.Row(
                [
                    ft.Text(especie, width=100),
                    barra,
                    ft.Text(f"{qtd} pet(s)", width=100),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    return ft.Column(
        [ft.Text("Quantidade de Pets por Espécie", size=22, weight="bold")] + barras,
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
    )


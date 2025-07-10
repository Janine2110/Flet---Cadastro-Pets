import flet as ft
from telas.cad_pets import cad_pets
from telas.graf_especies import graf_especies
from telas.filtro_pets import filtro_pets

def main(page: ft.Page):
    page.title = "Pet Shop - Sistema de Gestão"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    snack = ft.SnackBar(content=ft.Text(""), open=False)
    page.snack_bar = snack
    page.overlay.append(snack) 

    conteudo_dinamico = ft.Column() 

    def navegar(e):
        rota = e.control.data
        if rota == "cad_pets":
            conteudo_dinamico.controls = [cad_pets(page)]
        elif rota == "graf_especies":
            conteudo_dinamico.controls = [graf_especies(page)]
        elif rota == "filtro_pets":
            conteudo_dinamico.controls = [filtro_pets(page)]
        page.update()

    menu = ft.Row([
        ft.ElevatedButton("Cadastro de Pets", data="cad_pets", on_click=navegar),
        ft.ElevatedButton("Gráfico por Espécie", data="graf_especies", on_click=navegar),
        ft.ElevatedButton("Filtro por Nome e Espécie", data="filtro_pets", on_click=navegar),
    ], alignment=ft.MainAxisAlignment.CENTER)

    conteudo_dinamico.controls = [cad_pets(page)]  

    page.add(
        ft.Column([
            ft.Text("Pet Shop - Sistema de Gestão", size=30, weight="bold", text_align="center"),
            menu,
            ft.Divider(),
            conteudo_dinamico
        ], scroll=ft.ScrollMode.AUTO)
    )

ft.app(target=main)

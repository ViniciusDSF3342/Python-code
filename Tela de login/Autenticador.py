from flet import *
import flet as ft

def main (page:ft.Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.window_maximized = True
    page.window_resizable = True

    def logar(e):
        page.remove(register)
        page.add(login)
        page.update()

    def registrar(e):
        page.remove(login)
        page.add(register)
        page.update()

    def abrir_msgbox(e):
        page.dialog = MsgBox
        MsgBox.open = True
        page.update()

    def fechar_msgbox(e):
        MsgBox.open = False
        page.update()      

    MsgBox = ft.AlertDialog(

        content=ft.Container(
            width=260,
            height=30,

            content=ft.Column([
                ft.Row([
                    ft.Icon(
                        ft.icons.CANCEL,
                        size=30,
                        color=ft.colors.RED
                    ),

                    ft.Text(
                        value='Email ou senha incorretos',
                        size=16,
                        weight='bold'
                    )
                ], spacing=5)
            ])
        ) ,
        actions=[
            ft.TextButton(
                text='OK',
                on_click=fechar_msgbox 
            )
        ], actions_alignment='end'

    )  

    login = ft.Column([
        ft.Container(
            bgcolor=ft.colors.GREEN_200,
            width=page.window_width - 10,
            height=page.window_height - 60,
            border_radius=10,

            content=ft.Column([
                ft.Container(
                    bgcolor=ft.colors.WHITE70,
                    width=400,
                    height=320,
                    border_radius=10,

                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(
                                top=10,
                                bottom=12
                            ),
                            content = ft.Column([
                                ft.Text(
                                    value='Sign-In',
                                    weight='bold',
                                    size=20
                                )
                            ])
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text='Digite o seu email',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.EMAIL,
                            ),

                             ft.TextField(
                                hint_text='Digite a sua senha',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                            ),

                            ft.ElevatedButton(
                                text='Continuar',
                                bgcolor=ft.colors.GREEN_200,
                                on_hover=ft.colors.GREEN_100,
                                width=300,
                                height=40,
                                style=ft.ButtonStyle(overlay_color=ft.colors.GREEN_200),
                                on_click=abrir_msgbox
                            ),
                            ft.Row([
                                ft.TextButton('Recuperar conta'),
                                ft.TextButton(
                                    text='Criar nova conta',
                                    on_click=registrar)
                            ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            
                        ], spacing=10),
                        ft.Row([
                            ft.IconButton(icon=ft.icons.EMAIL),
                            ft.IconButton(icon=ft.icons.FACEBOOK),
                            ft.IconButton(icon=ft.icons.TELEGRAM)
                        ], alignment='center')

                    ], horizontal_alignment='center')

                )

            ], horizontal_alignment='center', alignment='center')
        )
    ])

    register = ft.Column([
        ft.Container(
            bgcolor=ft.colors.GREEN_200,
            width=page.window_width - 10,
            height=page.window_height - 60,
            border_radius=10,

            content=ft.Column([
                ft.Container(
                    bgcolor=ft.colors.WHITE70,
                    width=400,
                    height=450,
                    border_radius=10,

                    content=ft.Column([
                        ft.Container(
                            padding=ft.padding.only(
                                top=10,
                                bottom=12
                            ),
                            content = ft.Column([
                                ft.Text(
                                    value='Registro',
                                    weight='bold',
                                    size=20
                                )
                            ])
                        ),

                        ft.Column([
                            ft.TextField(
                                hint_text='Primeiro nome',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.NAME,
                            ),

                              ft.TextField(
                                hint_text='Segundo nome',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PERSON,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.NAME,
                            ),

                            ft.TextField(
                                hint_text='Digite o seu email',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.EMAIL,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.EMAIL,
                            ),

                            ft.TextField(
                                hint_text='Digite o seu telefone',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.PHONE,
                                text_vertical_align=1,
                                keyboard_type=ft.KeyboardType.PHONE,
                            ),
                            
                             ft.TextField(
                                hint_text='Digite a sua senha',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                            ),

                            ft.TextField(
                                hint_text='Digite a sua senha novamente',
                                width=300,
                                height=40,
                                border_radius=40,
                                prefix_icon=ft.icons.LOCK,
                                text_vertical_align=1,
                                password=True,
                                can_reveal_password=True,
                                keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
                            ),

                            ft.ElevatedButton(
                                text='Registro',
                                bgcolor=ft.colors.GREEN_200,
                                on_hover=ft.colors.GREEN_100,
                                width=300,
                                height=40
                            ),
                            ft.Row([
                                ft.TextButton('Recuperar conta'),
                                ft.TextButton(
                                    text='Já tenho uma conta',
                                    on_click=logar)
                            ], width=300, alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
                            
                        ], spacing=8),

                    ], horizontal_alignment='center')

                )

            ], horizontal_alignment='center', alignment='center')
        )
    ])

    def redimensionar_controles(e):
        login.controls[0].width = page.window_width - 10
        login.controls[0].height = page.window_height - 60

        register.controls[0].width = page.window_width - 10
        register.controls[0].height = page.window_width - 60

        page.update()     
    page.on_resize = redimensionar_controles
    
    page.add(login)

if __name__ == '__main__':
    ft.app(target=main)

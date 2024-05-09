import flet as ft

def main(page: ft.Page):
    
    page.padding = 0
    page.spacing = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # def route_change(self, route):
    #     routes = {
    #         '/': HomePage()
    #     }
    #     page.view.content = routes[route]
    #     page.view.update()

    # page.on_route_change = route_change
    text_btn_style = {
        'style': ft.ButtonStyle(color=ft.colors.WHITE, overlay_color={"": "transparent"}),
    }
    


    def card():
        return ft.Card(
            content=ft.Container(
                width=240,
                height=340,
                col={'sm': 12, 'md': 12, 'lg': 12},
                content=ft.Column(
                    controls=[
                        ft.Container(
                            height=150,
                            width=240,
                            border_radius=ft.border_radius.only(top_left=60, bottom_right=60),
                            border=ft.border.all(0.2, ft.colors.RED_ACCENT_700),
                            content=ft.Image(
                                src=f"https://picsum.photos/150/150?{5}",
                                fit=ft.ImageFit.FILL,
                                expand=True,
                                repeat=ft.ImageRepeat.NO_REPEAT,
                                border_radius=ft.border_radius.only(top_left=60, bottom_right=60),
                            )
                        ),
                        ft.Container(
                            bgcolor=ft.colors.DEEP_PURPLE_ACCENT_100,
                            content=ft.Text('Food'),
                            padding=ft.padding.symmetric(horizontal=12, vertical=5),
                            border_radius=8,
                            margin=ft.margin.only(left=10)
                        ),
                        ft.Container(
                            padding=10,
                            content=ft.Column(
                                controls=[
                                    ft.Text('Artificial Intelligence and Chess', color='black'),
                                    ft.Text(
                                        """Artificial Intelligence and Chess: A Match Made in Heaven Artificial 
                                        Intelligence (AI) has made significant strides in the oast few decades and 
                                        has tes""",
                                        color='black', overflow=ft.TextOverflow.ELLIPSIS),
                                    ft.Text('By: Aster Kennedy', color='black'),
                                    ft.Container(
                                        padding=ft.padding.only(left=10),
                                        content=ft.Row(
                                            controls=[
                                                ft.Image(
                                                    src=f"/images/user.jpeg",
                                                    width=30,
                                                    height=30,
                                                    border_radius=ft.border_radius.all(15),

                                                ),
                                                ft.Text(
                                                    spans=[
                                                        ft.TextSpan('Mar 08, 2023-07-04',
                                                                    style=ft.TextStyle(
                                                                        color='black',
                                                                        weight=ft.FontWeight.BOLD
                                                                    )
                                                                    )
                                                    ],
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.START
                )
            ),
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=60),
            elevation=0.2,
            shadow_color=ft.colors.RED_ACCENT_700
        )
        
    def open_drawer(e):
        drawer = page.controls[0].content.controls[1]

        if not drawer.visible:
            drawer.visible = True
        else:
            drawer.visible = False
        page.update()

    def collapse():
        return ft.Container(
            content=ft.IconButton(
                visible=True,
                icon='menu',
                icon_color='white',
                # hover_color=ft.colors.DEEP_PURPLE_ACCENT_100,
                on_click=open_drawer
            ),
        )

    def drawer():
        return ft.Container(
            visible=False,
            width=page.width,
            bgcolor=ft.colors.DEEP_PURPLE_ACCENT_100,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.START,
                spacing=0,
                col={'sm': 12, 'md': 12, 'lg': 12},
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    ft.TextButton('About', **text_btn_style),
                    ft.TextButton('Services', **text_btn_style),
                    ft.TextButton('Contact', **text_btn_style),
                    ft.TextButton('Login', **text_btn_style),
                ]
            )
        )

        return ft.Card(
            content=ft.Container(
                width=240,
                height=340,
                col={'sm': 12, 'md': 12, 'lg': 12},
                content=ft.Column(
                    controls=[
                        ft.Container(
                            height=150,
                            width=240,
                            border_radius=ft.border_radius.only(top_left=60, bottom_right=60),
                            border=ft.border.all(0.2, ft.colors.RED_ACCENT_700),
                            content=ft.Image(
                                src=f"https://picsum.photos/150/150?{5}",
                                fit=ft.ImageFit.FILL,
                                expand=True,
                                repeat=ft.ImageRepeat.NO_REPEAT,
                                border_radius=ft.border_radius.only(top_left=60, bottom_right=60),
                            )
                        ),
                        ft.Container(
                            bgcolor=ft.colors.DEEP_PURPLE_ACCENT_100,
                            content=ft.Text('Food'),
                            padding=ft.padding.symmetric(horizontal=12, vertical=5),
                            border_radius=8,
                            margin=ft.margin.only(left=10)
                        ),
                        ft.Container(
                            padding=10,
                            content=ft.Column(
                                controls=[
                                    ft.Text('Artificial Intelligence and Chess', color='black'),
                                    ft.Text(
                                        """Artificial Intelligence and Chess: A Match Made in Heaven Artificial 
                                        Intelligence (AI) has made significant strides in the oast few decades and 
                                        has tes""",
                                        color='black', overflow=ft.TextOverflow.ELLIPSIS),
                                    ft.Text('By: Aster Kennedy', color='black'),
                                    ft.Container(
                                        padding=ft.padding.only(left=10),
                                        content=ft.Row(
                                            controls=[
                                                ft.Image(
                                                    src=f"/images/user.jpeg",
                                                    width=30,
                                                    height=30,
                                                    border_radius=ft.border_radius.all(15),

                                                ),
                                                ft.Text(
                                                    spans=[
                                                        ft.TextSpan('Mar 08, 2023-07-04',
                                                                    style=ft.TextStyle(
                                                                        color='black',
                                                                        weight=ft.FontWeight.BOLD
                                                                    )
                                                                    )
                                                    ],
                                                )
                                            ]
                                        )
                                    )
                                ]
                            )
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.START
                )
            ),
            color=ft.colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=60),
            elevation=0.2,
            shadow_color=ft.colors.RED_ACCENT_700
        )

    def menu():
        
        menu_style = {
            'height': 42,
            'bgcolor': ft.colors.DEEP_PURPLE_ACCENT_100,
            'padding': ft.padding.symmetric(horizontal=20),
        }

        collapse = ft.Container(
                opacity=0,
                visible=False,
                animate_opacity=300,
                content=ft.IconButton(
                    icon='menu',
                    icon_color='white',
                    # hover_color=ft.colors.DEEP_PURPLE_ACCENT_100,
                    on_click=open_drawer
                ),
            )

        menu_right = ft.Container(
            expand=1,
            visible=True,
            content=ft.Row(
                controls=[
                    ft.TextButton('About', **text_btn_style),
                    ft.TextButton('Services', **text_btn_style),
                    ft.TextButton('Contact', **text_btn_style),
                    ft.TextButton('Login', **text_btn_style),
                ],
                alignment=ft.MainAxisAlignment.END
            ),
        )

        return ft.Container(
            **menu_style,
            content=ft.Row(
                controls=[
                    ft.Container(
                        expand=1,
                        content=ft.Row(
                            controls=[
                                ft.Text('Blog', color='white'),
                                ft.Container(
                                    padding=3,
                                    content=ft.TextField(
                                        prefix_icon=ft.icons.SEARCH,
                                        hint_text='Enter the tag',
                                        bgcolor='white',
                                        border_radius=40,
                                        border_width=1,
                                        focused_border_color='white',
                                        text_size=12,
                                        text_style=ft.TextStyle(
                                            color='black',
                                        ),
                                        hint_style=ft.TextStyle(
                                            color='black',
                                        ),
                                        keyboard_type=ft.KeyboardType.TEXT,
                                    ),
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                    ),
                    menu_right,
                    collapse
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            )
        )

    def body():
        cards = ft.Row(wrap=True, spacing=20, scroll=ft.ScrollMode.ALWAYS, col={'sm': 12, 'md': 12, 'lg': 12})

        for i in range(16):
            cards.controls.append(card())

        return ft.Container(
            width=page.width * 0.8,
            expand=True,
            alignment=ft.alignment.center,
            content=ft.Column(
                controls=[
                    cards
                ], scroll=ft.ScrollMode.ALWAYS
            )
        )

    def footer():
        return ft.Container(
            bgcolor=ft.colors.DEEP_PURPLE_ACCENT_100,
            height=70,
            content=ft.Row(
                controls=[
                    ft.Container(
                        expand=1,
                        padding=ft.padding.symmetric(horizontal=30),
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    src=f"/images/youtube.svg",
                                    width=30,
                                    height=30,
                                ),
                                ft.Image(
                                    src=f"/images/facebook.png",
                                    width=30,
                                    height=30,

                                ),
                                ft.Image(
                                    src=f"/images/linkedin.png",
                                    width=30,
                                    height=30,

                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY
                        )
                    ),
                    ft.Container(
                        expand=2,
                        padding=ft.padding.symmetric(horizontal=30),
                        content=ft.Text('Developed by: @Yohan Diaz Acosta'),
                        alignment=ft.alignment.center_right
                    )
                ]
            )
        )

    def build():
        
        body_style = {
            'bgcolor': ft.colors.WHITE,
            'width': page.width,
            'height': page.height,
            'padding': ft.padding.symmetric(horizontal=20),
        }

        return ft.Container(
            **body_style,
            content=ft.Column(
                controls=[
                    menu(),
                    drawer(),
                    body(),
                    footer(),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER   
            ),
        )

    page.add(build())
    
    def page_resize(e):
        home = page.controls[0]
        collapse_btn = home.content.controls[0].content.controls[2]
        menu_right = home.content.controls[0].content.controls[1]
        
        home.width = page.width
        home.height = page.height
        body = home.content.controls[2]
        body.width = home.width
        body.height = home.height
        home.update()
        body.update()
        
        if page.width <= 720:
            collapse_btn.opacity = 1
            menu_right.visible = False
            collapse_btn.visible = True
            menu_right.update()
            collapse_btn.update()
        else:
            menu_right.visible = True
            collapse_btn.visible = False
            collapse_btn.opacity = 0
            menu_right.update()
            collapse_btn.update()
    
    page.on_resize = page_resize
    page.update()

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)

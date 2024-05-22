import flet as ft

class HomePage(ft.UserControl):
    _page = None
    # -----------------------------STYLE------------------------------------------------
    menu_right_style = {
        'col': 4,
        'padding': 3,
        'expand': True,
        'visible': True,
    }
    
    # -------------------------------FUNCTIONS-------------------------------------------
    def __init__(self, page: ft.Page):
        self._page = page
        super().__init__(expand=True)
        
        # -----------------------------STYLE------------------------------------------------
        menu_style = {
            'col': 12,
            'height': 42,
            'bgcolor': ft.colors.DEEP_PURPLE_ACCENT_100,
            'padding': ft.padding.symmetric(horizontal=20),
        }
        
        menu_left_style = {
            'col': 2,
            'expand': True,
            'padding': 10,
        }
        
        menu_center_style = {
            'col': 6,
            'padding': 3,
        }
        
        search_menu_btn_style = {
            'bgcolor': 'white',
            'border_radius': 40,
            'border_width': 1,
            'focused_border_color': 'white',
            'text_size': 12,
            'text_style': ft.TextStyle(
                color='black',
            ),
            'hint_style': ft.TextStyle(
                color='black',
            ),
            'keyboard_type': ft.KeyboardType.TEXT,
        }
        
        text_btn_style = {
            'style': ft.ButtonStyle(color=ft.colors.WHITE, overlay_color={"": "transparent"}),
        }  
        # -------------------------------WIDGET---------------------------------------------
        self.menu_left = ft.Container(
            **menu_left_style,
            content=ft.Text("Blog", color='white', weight= ft.FontWeight.BOLD)
        )
        
        self.menu_center = ft.Container(
            **menu_center_style,
            content=ft.TextField(
                **search_menu_btn_style,
                prefix_icon=ft.icons.SEARCH,
                hint_text='Enter the tag',
            ),
        )   
        
        self.collapse = ft.Container(
            opacity=0,
            visible=False,
            animate_opacity=300,
            col=1,
            content=ft.IconButton(
                icon='menu',
                icon_color='white',
                on_click=self.open_drawer,
                style=ft.ButtonStyle(overlay_color={"": "transparent"})
            ),
        )
    
        self.menu = ft.Container(
            **menu_style,
            content=ft.ResponsiveRow(
                [
                    self.menu_left,
                    self.menu_center,
                    self.menu_right(),
                    self.collapse,
                ]
            )
        )
        
        self.drawer = ft.Container(
            visible=False,
            bgcolor = ft.colors.DEEP_PURPLE_ACCENT_100,
            padding=10,
            margin=ft.margin.symmetric(vertical=1.5),
            content=ft.ResponsiveRow(
                controls=[
                    ft.TextButton('About', style = ft.ButtonStyle(color=ft.colors.WHITE, overlay_color={"": "transparent"}),),
                    ft.TextButton('Services', style = ft.ButtonStyle(color=ft.colors.WHITE, overlay_color={"": "transparent"}),),
                    ft.TextButton('Contact', style = ft.ButtonStyle(color=ft.colors.WHITE, overlay_color={"": "transparent"}),),
                ], 
            )
        )
        
        self.footer = ft.Container(
            bgcolor=ft.colors.DEEP_PURPLE_ACCENT_100,
            height=80,
        )
        
        self.home =ft.ResponsiveRow(
            controls=[
                ft.Container(
                    expand=True,
                    padding=ft.padding.symmetric(horizontal=20),
                    content=ft.Column(
                        spacing=0,
                        controls=[
                            self.menu,
                            self.drawer,
                            self.body(),
                            self.footer,
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        scroll='None'
                    )
                )
            ]
        )
    
    def open_drawer(self, e):
        drawer = self.controls[0].controls[0].content.controls[1]

        if not drawer.visible:
            drawer.visible = True
        else:
            drawer.visible = False
        drawer.update()  
      
    def menu_right(self):
        text_btn_menu_right_style = {
            'style': ft.ButtonStyle(color=ft.colors.WHITE, overlay_color={"": "transparent"}),
        }
            
        return ft.Container(
            **self.menu_right_style,
            content=ft.Row(
                col=4,
                controls=[
                    ft.TextButton('About', **text_btn_menu_right_style),
                    ft.TextButton('Services', **text_btn_menu_right_style),
                    ft.TextButton('Contact', **text_btn_menu_right_style),
                ],
                alignment=ft.MainAxisAlignment.END
            )
        )

    def card(self):
        width = self._page.width
        height = self._page.height
        
        return ft.Card(
            content=ft.Container(
                width=288,
                height=height * 0.8,
                col={'sm': 12, 'md': 12, 'lg': 12},
                content=ft.Column(
                    controls=[
                        ft.Container(
                            height=height * 0.3,
                            width=width,
                            col=12,
                            border_radius=ft.border_radius.only(top_left=60, bottom_right=60),
                            border=ft.border.all(0.2, ft.colors.RED_ACCENT_700),
                            content=ft.Image(
                                src=f"https://picsum.photos/150/150?{5}",
                                fit=ft.ImageFit.COVER,
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
                                    ft.Container(
                                        content=ft.Text(
                                        "Artificial Intelligence and Chess: A Match Made in Heaven Artificial Intelligence (AI) has made significant strides in the oast few decades and has tes Artificial Intelligence and Chess: A Match Made in Heaven Artificial Intelligence (AI) has made significant strides in the oast few decades and has tes Artificial Intelligence and Chess: A Match Made in Heaven Artificial Intelligence (AI) has made significant strides in the oast few decades and has tes Artificial Intelligence and Chess: A Match Made in Heaven Artificial Intelligence (AI) has made significant strides in the oast few decades and has tes Artificial Intelligence and Chess: A Match Made in Heaven Artificial Intelligence (AI) has made significant strides in the oast few decades and has tes Artificial Intelligence and Chess: A Match Made in Heaven Artificial Intelligence (AI) has made significant strides in the oast few decades and has tes Artificial Intelligence and Chess: A Match Made in Heaven Artificial Intelligence (AI) has made significant strides in the oast few decades and has tes Artificial Intelligence and Chess: A Match Made in Heaven Artificial Intelligence (AI) has made significant strides in the oast few decades and has tes",
                                        color='black', 
                                        overflow=ft.TextOverflow.ELLIPSIS,
                                        no_wrap=True,
                                        max_lines=8
                                        ),
                                    ),
                                    
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
        
    def body(self):
        cards = ft.Row(wrap=True, spacing=20)
        
        for i in range(21):
            cards.controls.append(self.card())
        
        return ft.Container(                                                                                                            
            expand=True,
            margin=ft.margin.symmetric(vertical=10),
            alignment=ft.alignment.center,
            content=ft.Column(
            controls=[
                cards
            ], 
            scroll=ft.ScrollMode.ALWAYS,
            )
        )
    
    def build(self):
        return self.home

# -------------------------------------------------MAIN------------------------------------
def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def page_resize(e):
        home = e.control.controls[0].controls[0].controls[0].content.controls
        cards = home[2].content.controls[0].controls
        menu_right = home[0].content
        
        print(page.width)
        
        if int(page.width) <= 700:
            menu_right.controls[2].visible = False
            menu_right.controls[1].col = 9
            menu_right.controls[3].opacity = 1
            menu_right.controls[3].visible = True
        
            for i in cards:
                i.content.width = page.width / 2.5
                i.content.update()
            
            if int(page.width) <= 500:
                for i in cards:
                    i.content.width = page.width
                    i.content.update()
        else:
            drawer = e.control.controls[0].controls[0].controls[0].content.controls[1]
            menu_right.controls[3].visible = False
            drawer.visible = False
            drawer.update()
            menu_right.controls[1].col = 6
            menu_right.controls[2].visible = True
            
            for i in cards:
                i.content.width = 288
                i.content.update()
        menu_right.update()

    page.on_resize = page_resize
    
    page.update()
    
    page.add(HomePage(page))
    
ft.app(main)
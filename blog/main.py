import flet as ft

class HomePage(ft.UserControl):
    # -----------------------------STYLE------------------------------------------------
    menu_right_style = {
        'col': 4,
        'padding': 3,
        'expand': True,
        'visible': True,
    }
    
    # -------------------------------FUNCTIONS-------------------------------------------
    def __init__(self):
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
        
        self.home =ft.ResponsiveRow(
            controls=[
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        spacing=0,
                        controls=[
                            self.menu,
                            self.drawer,
                        ]
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
        
    def build(self):
        return self.home

# -------------------------------------------------MAIN------------------------------------
def main(page: ft.Page):
    page.padding = 0
    page.spacing = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    def page_resize(e):
        menu_right = e.control.controls[0].controls[0].controls[0].content.controls[0].content
        
        if int(page.width) <= 700:
            menu_right.controls[2].visible = False
            menu_right.controls[1].col = 9
            menu_right.controls[3].opacity = 1
            menu_right.controls[3].visible = True
        else:
            drawer = e.control.controls[0].controls[0].controls[0].content.controls[1]
            menu_right.controls[3].visible = False
            drawer.visible = False
            drawer.update()
            menu_right.controls[1].col = 6
            menu_right.controls[2].visible = True
        menu_right.update()
    
    page.on_resize = page_resize
    
    page.update()
    
    page.add(HomePage())
    
ft.app(main)
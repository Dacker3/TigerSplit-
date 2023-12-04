import flet as ft
BG = '#00D632'
WHITE = '#FFFFFF'
class ThirdPage(ft.UserControl):
  def  __init__(self,page):
   super().__init__()
   self.page = page
   self.textfield_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Enter Payment tag"),
        actions=[
            ft.TextField(label="click here", width=200),
            ft.TextButton("Submit", on_click=self.close_textfield),
            ft.ElevatedButton("CANCEL", bgcolor="red", on_click=self.close_textfield),
        ],
        on_dismiss=lambda e: print("Modal dismissed"),
  ) 
   self.dlg_modal_settings = ft.AlertDialog(
        modal=True,
        title=ft.Text("              Choose payment method"),
        actions=[
            ft.ElevatedButton("Cashapp", bgcolor = BG, color=WHITE, icon_color = WHITE, icon="attach_money", on_click=self.open_textfield),
            ft.ElevatedButton("PayPal", bgcolor = '#00457C', color=WHITE, icon_color = WHITE, icon="paypal", on_click=self.open_textfield),
            ft.ElevatedButton("Venmo", bgcolor = '#008CFF', color=WHITE, icon_color = WHITE, icon="v", on_click=self.open_textfield),
            ft.ElevatedButton("CANCEL", bgcolor="red", color=WHITE, icon_color = WHITE, on_click=self.close_dlg_settings),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dismissed"),
    )
   self.dlg_modal_profile = ft.AlertDialog (
        modal = True,
        title = ft.Text("Edit Profile"),
        actions = [
            ft.ElevatedButton("Edit Name", bgcolor = WHITE, color=BG, icon_color =BG, icon="drive_file_rename_outlined", on_click=self.open_textfield),
            ft.ElevatedButton("Edit Picture", bgcolor = WHITE, color=BG, icon_color=BG, icon="picture_as_pdf_outlined", on_click= self.open_textfield),
            ft.ElevatedButton("CANCEL", bgcolor="red", color=WHITE, icon_color = WHITE, on_click=self.close_dlg_settings),

        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dismissed"),

    )
   

  def close_textfield(self,e):

        self.textfield_dialog.open = False
        self.dlg_modal_settings.open = False
        self.page.update()

  def open_textfield(self,e):
        self.page.dialog = self.textfield_dialog
        self.page.dialog.open = True
        self.page.update()

  def open_dlg_modal_settings(self,e):
        self.page.dialog = self.dlg_modal_settings
        self.dlg_modal_settings.open = True
        self.page.update()      
  def close_dlg_settings(self,e):
        self.page.dialog.open = False
        self.page.update()


  def build(self):
    
      return ft.Container(
        width = 400, 
        height = 850,
        bgcolor= BG, 
        border_radius = 20,
        padding = ft.padding.only(left = 10, top = 60, right = 200),
        content = ft.Column(
            controls = [
                ft.Container(height =20), 
                ft.Row(
                    controls = [
                        ft.Container(padding=ft.padding.all(5),
                          bgcolor=WHITE,
                          width=90,height=90,
                          border_radius=50,
                          content=ft.Container(bgcolor=WHITE,
                            height=70,width=70,
                            border_radius=40,
                            content=ft.CircleAvatar(opacity=0.9,
                            foreground_image_url="https://bloximages.newyork1.vip.townnews.com/nola.com/content/tncms/assets/v3/editorial/4/69/469f1c32-6f4b-5c5d-b24f-f567206d6a2d/60c3ec1d12eeb.image.jpg?resize=362%2C500"
                            )
                          )
                        )
                    ]
                ),
                ft.Row(
                    controls = [
                        ft.Icon(ft.icons.PERSON, color = WHITE), 
                        ft.Text('Dos Acker',size=30,weight='bold', color = WHITE), 


                    ]
                ),
                ft.Row( alignment= 'right', 
                    controls = [
                        ft.Text('______________________________________________________________', color = WHITE)
                    ]
                ),
                ft.Row(
                    controls = [
                        ft.Icon(ft.icons.ATTACH_MONEY, color = WHITE),
                        ft.Container(
                            content=ft.ElevatedButton(
                                text='Add new Payment',
                                color = BG,
                                on_click = self.open_dlg_modal_settings,
                                bgcolor=WHITE,
                                width=200
                            ),

                    ),
                    ]
                ),
                ft.Row(
                    controls = [
                        ft.Icon(ft.icons.EDIT_OUTLINED, color =WHITE),
                        ft.Container(
                            content=ft.ElevatedButton(
                                text='Edit profile',
                                color = BG,
                                on_click=self.open_dlg_modal_settings,
                                bgcolor=WHITE,
                                width=200
                            ),

                    ),
                
                    ]
                )
                

            ]
        )
        

    )
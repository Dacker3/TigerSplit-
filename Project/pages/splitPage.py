import flet as ft
BG = '#00D632'
WHITE = '#DDEEDF'
class splitPage(ft.UserControl):
  def  __init__(self,page):
   super().__init__()
   self.page = page
   self.group_adder = ft.AlertDialog(
            title=ft.Text("Your Bill", size=30,weight='bold', color = BG), 
            content= ft.Row(
                controls=[
                    ft.Text("Hi"),
                    
                ]
            )
        )
  def build(self):
    return ft.Container(
        width = 400, 
        height = 850,
        bgcolor= WHITE, 
        border_radius = 20,
        padding = ft.padding.only(left = 10, top = 60, right = 200),)
  
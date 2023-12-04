import flet as ft;
class Navigation(ft.UserControl):
     def change(self,e):
        self.changeFunc(e)
        return
     def __init__(self,func):
        super().__init__()
        self.changeFunc = func
   #   text = "a"
     def build(self):
        return ft.Container(
           padding= ft.padding.only(100,100,0,0) ,
           content =ft.NavigationBar(
          
        on_change= self.change,
        
        destinations=[
            ft.NavigationDestination(icon=ft.icons.PEOPLE, label="Friends"),
            ft.NavigationDestination(icon=ft.icons.CARD_GIFTCARD, label="Bill"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Explore",
            ),
        ]
      ))

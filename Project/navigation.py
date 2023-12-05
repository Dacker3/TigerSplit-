import flet as ft;
BG = '#00D632'
WHITE = '#FFFFFF'
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
         #   padding= ft.padding.only(100,100,0,0),
         #   margin = ft.margin.only(left = -25), 
           border_radius= ft.border_radius.all(20),
           content =ft.NavigationBar(
          
               on_change= self.change,
               bgcolor=BG, 
               destinations=[
                     ft.NavigationDestination(
                         icon=ft.icons.HOME_FILLED,
                         label="Home"
                         ),
                     ft.NavigationDestination(
                         icon=ft.icons.CARD_GIFTCARD, 
                         label="Split",
                     ),
                     ft.NavigationDestination(
                        icon=ft.icons.PEOPLE,
                        label="Groups",
                     ),
                     ft.NavigationDestination(
                        icon=ft.icons.SETTINGS,
                        label="Settings",
                     ),
               ]
            ))

import flet as ft;
from pages.thirdPage import ThirdPage;
from pages.secondPage import SecondPage;

from pages.firstPage import FirstPage;
from pages.splitPage import splitPage;
from navigation import Navigation;
BG = '#00D632'
WHITE = '#DDEEDF'






def main(page: ft.Page):
      
     page.window_bgcolor = WHITE 
     
   #   def toggle_splitPage(e):
   #       splitPage.visible =True
   #       firstPage.visible = False
   #       secondPage.visible = False
   #       thirdPage.visible = False
   #       page.update()
     
     hi = splitPage(page)
     firstPage = FirstPage(page)
     secondPage = SecondPage(page)
     thirdPage = ThirdPage(page)
     
     secondPage.visible = False
     thirdPage.visible = False
   
      
     def changetab(e):
        my_index = e.control.selected_index
        firstPage.visible = True if my_index == 0 else False
        secondPage.visible = True if my_index == 1 else False
        hi.visible = True if my_index == 2 else False
        thirdPage.visible = True if my_index == 3 else False

        page.update()
        
      
     n = Navigation(changetab)  
     hi.visible = False


     c = ft.Container( content=ft.Column(controls = [firstPage,secondPage,thirdPage, hi]))
     page.add(n)
     page.add(c)
     page.add(hi)
      
     page.update()
      
     
ft.app(target=main)

        
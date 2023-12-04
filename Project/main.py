import flet as ft;
from pages.thirdPage import ThirdPage;
from pages.secondPage import SecondPage;

from pages.firstPage import FirstPage;
from navigation import Navigation;
BG = '#00D632'
WHITE = '#FFFFFF'






def main(page: ft.Page):
      
     firstPage = FirstPage(page)
     secondPage = SecondPage()
     thirdPage = ThirdPage(page)
     
     secondPage.visible = False
     thirdPage.visible = False

     def changetab(e):
        my_index = e.control.selected_index
        firstPage.visible = True if my_index == 0 else False
        secondPage.visible = True if my_index == 1 else False
        thirdPage.visible = True if my_index == 2 else False
        page.update()
        
      
     n = Navigation(changetab)  
     c = ft.Container(content=ft.Column(controls = [firstPage,secondPage,thirdPage]))
     page.add(n)
     page.add(c)
      
     page.update()
      
     
ft.app(target=main)

        
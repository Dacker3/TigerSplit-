import flet as ft
BG = '#00D632'
WHITE = '#DDEEDF'
class SecondPage(ft.UserControl):
    
    def close_dlg(self, e):
        self.dlg.open = False
        self.page.update()
    
    def close_split(self, e):
        self.split.open = False
        self.page.update()
    
    def  __init__(self, page):
        super().__init__()
        self.page = page
        self.tf1 = ft.TextField(
                        label="Title of Bill",
                        hint_text="Add Title for Bill",
                        width=380,
                        color = BG, 
                        border_color=BG,
                        border="none"
                    )
        self.tf2 = ft.TextField(
                        label="Amount",
                        hint_text="Add Bill Amount here",
                        width=380,
                        border_color=BG,
                        color = BG, 
                        border="none"
                    )
        self.bill_option = ft.Dropdown(
                        label="Bill or Expense",
                        hint_text="Bill or Expense",
                        width=380,
                        border_color='transparent',
                        color = BG, 
                        options=[
                            ft.dropdown.Option("Bill"),
                            ft.dropdown.Option("Expense"),
                        ],
        )
        self.group = ft.Dropdown(
                        label="Select Group",
                        hint_text="Select Group",
                        width=380,
                        border_color='transparent',
                        color = BG,
                        options=[
                            ft.dropdown.Option("Group 1"),
                            ft.dropdown.Option("Group 2"),
                            ft.dropdown.Option("Group 3"),
                        ],
                    )
        self.split_action = ft.Dropdown(
                        label="Split Actions",
                        hint_text="Split Actions",
                        width=380,
                        border_color='transparent',
                        color = BG, 

                        options=[
                            ft.dropdown.Option("Split equally"),
                            ft.dropdown.Option("Custom"),
                            ft.dropdown.Option("According to item"),
                        ],
                    )
        self.dlg = ft.AlertDialog(
            title=ft.Text("Your Bill", size=30,weight='bold', color = BG), 
            content = ft.Column(
                controls= [ 
                     ft.Row(
                         controls=[
                            #  ft.Text("Bill Name:",weight='bold'), 
                                self.tf1, 
                         ]
                     ),
                     ft.Row(
                         controls=[
                            #  ft.Text("Bill Amount:",weight='bold'), 
                             self.tf2, 
                         ]
                     ),
                     ft.Row(
                         controls=[
                            #  ft.Text("Bill or Expense:",weight='bold'), 
                             self.bill_option, 
                         ]
                     ),
                     ft.Row(
                         controls=[
                            #  ft.Text("Selected Group:",weight='bold'), 
                             self.group 
                         ]
                     ),
                     ft.Row(
                         controls=[
                            #  ft.Text("Split Option:",weight='bold'), 
                             self.split_action, 
                         ]
                     )
                ]
            ),
            on_dismiss=lambda e: print("Dialog dismissed!")
            )
        self.t = ft.Text()
        
        def slider_changed(e):
            self.t.value = f"Your percentage owed is: {e.control.value}"
            self.page.update()
        
        self.split_slider = ft.Slider(min=0, max =100, divisions =10, label = "{value}%", thumb_color=BG, inactive_color=BG, on_change= slider_changed)                        

        self.split = ft.AlertDialog(
            title=ft.Text("Your Bill", size=30,weight='bold', color = BG), 
            content= ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text("Choose you percentage of the Bill"),
                            self.split_slider,
                            self.t
                        ]
                    )
                ]
            )

        )
    
    def open_dlg(self,e):
        self.page.dialog = self.dlg
        self.page.dialog.open = True
        self.page.update()
    def open_split(self,e):
        self.page.dialog = self.split
        self.page.dialog.open = True
        self.page.update()
    

 
    def build(self):
      
      
      return ft.Container(
        width = 400, 
        height = 850,
        bgcolor= WHITE, 
        border_radius = 20,
        padding = ft.padding.only(left = 10, top = 60, right = 200),
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text('Add Bill', size=20, weight=ft.FontWeight.BOLD, color = BG),
                    # padding=ft.padding.all(10),
                ),

                ft.Container(
                    content= self.tf1, 
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content=self.tf2, 
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content= self.bill_option, 
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content= self.group,
                    margin=ft.margin.only(top=10),
                ),

                # ft.Container(
                #     content= self.split_action, 
                #     margin=ft.margin.only(top=10),
                # ),

                ft.Container(
                    content = ft.Row(
                        alignment = 'center',
                        controls= [
                            ft.ElevatedButton(
                                text ='Split',
                                on_click =self.open_split,
                                color = WHITE,
                                bgcolor = BG,
                                width = 200,
                                height = 35
                            )
                        ]
                    )
                ),

                ft.Container(
                    content=ft.ElevatedButton(
                        text='Save',
                        color = WHITE, 
                        on_click=self.open_dlg,
                        bgcolor=BG,
                        width=100
                    ),

                    margin=ft.margin.only(top=20),
                ),

                ft.Text(),
            ]
        )
    )

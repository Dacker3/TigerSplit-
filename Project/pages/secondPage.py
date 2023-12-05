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
    def close_group_adder(self, e):
        self.group_adder.open = False
        self.page.update()
    
    def  __init__(self, page):
        super().__init__()
        self.page = page
        self.groups = []
        def get_amount(e):
            self.amount = int(e.control.value)

        self.tf1 = ft.TextField(
                        label="Title of Bill",
                        hint_text="Add Title for Bill",
                        width=380,
                        color = BG, 
                        border_color=BG,
                        border="none"
                    )     
        self.t = ft.Text()
        self.t2 = ft.Text()
        
        def slider_changed( e):
            self.t.value = self.amount * (0.01 * int(e.control.value))
            self.page.update()
        def tip_changed( e):
            self.t2.value = self.t.value + (self.t.value * (0.01 * int(e.control.value)))
            self.page.update()
        
        self.split_slider = ft.Slider(min=0, max =100, divisions =10, label = "{value}%", thumb_color=BG, inactive_color=BG, on_change= slider_changed)                        
        self.tip_slider = ft.Slider(min=0, max =100, divisions =20, label = "{value}%", thumb_color=BG, inactive_color=BG, on_change= tip_changed)                        

        self.split = ft.AlertDialog(
            title=ft.Text("Your Bill", size=30,weight='bold', color = BG), 
            content= ft.Column(
                controls=[
                    ft.Row(alignment = 'center',
                        controls=[
                            ft.Text("Choose you percentage of the Bill",weight = 'bold', size =15),
                        ]
                    ),
                    ft.Row(alignment = 'center',
                        controls=[
                            self.split_slider,
                        ]
                    ),
                    ft.Row(alignment = 'center',
                        controls=[
                            ft.Text("Your amount owed is: $"),self.t
                        ]
                    ),
                    ft.Row(alignment = 'center',
                        controls=[
                            ft.Text("Choose you Tip pecentage", weight = 'bold', size =15),
                        ]
                    ),
                    ft.Row(alignment = 'center',
                        controls=[
                            self.tip_slider,
                        ]
                    ),
                    ft.Row(alignment = 'center',
                        controls=[
                            ft.Text("Your amount owed is +TIP: $"),self.t2
                        ]
                    ),
                ]
            )

        )
        self.tf2 = ft.TextField(
                        label="Amount",
                        hint_text="Add Bill Amount here",
                        width=380,
                        border_color=BG,
                        color = BG, 
                        border="none",
                        on_submit= get_amount
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
                             ft.Text("Bill Amount:",weight='bold'), 
                             self.t2, 
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
        
    def open_group_added(self, e):
        self.toggle(e)
        self.page.update()
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
                    content = ft.Row(
                        alignment = 'center',
                        controls= [
                            ft.ElevatedButton(
                                text ='Add Group',
                                on_click =self.open_group_added,
                                color = WHITE,
                                bgcolor = BG,
                                width = 200,
                                height = 30
                            )
                        ]
                    )
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

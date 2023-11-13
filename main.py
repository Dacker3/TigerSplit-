from flet import *

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    WHITE = '#FFFFFF'

    dlg = AlertDialog(
        title=Text("Payment Complete"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()
        dlg.update = False
        page.update()
        

    dlg_modal = AlertDialog(
        modal=True,
        title=Text("Please Confirm"),
        content=Text("Do you really wish to make this payment"),
        actions=[
            TextButton("Yes", on_click=open_dlg),
            TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dismissed"),
    )

    bigSave = AlertDialog(
        modal=True,
        title=Text("Please Confirm"),
        content=Text("Are the final changes correct?"),
        actions=[
            TextButton("Yes", on_click=open_dlg),
            TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=MainAxisAlignment.END,
       on_dismiss=lambda e: print("Modal dismissed"),
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True

    def save(e):
        dlg_modal.open = False  # Close dlg_modal before opening bigSave
        page.dialog = bigSave
        bigSave.open = True
        page.update()

    def changetab(e):
        my_index = e.control.selected_index
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        tab_3.visible = True if my_index == 2 else False
        page.update()

    page.navigation_bar = NavigationBar(
        bgcolor="blue",
        on_change=changetab,
        selected_index=0,
        destinations=[
            NavigationDestination(icon="home"),
            NavigationDestination(icon="Add"),
            NavigationDestination(icon="settings"),
        ]
    )

    friends_card = Row(scroll='auto')

    friends = ['Sally', 'Fred', 'Ethan', 'Dos', 'Johnny']
    for index, value in enumerate(friends):
        friends_card.controls.append(
            Container(
                border_radius=20,
                bgcolor=FWG,
                width=150,
                height=110,
                
                padding=15,
                content=Column(
                    controls=[
                        Row(alignment='center', controls=[Text(value)]),
                        Row(alignment='center',
                            controls=[
                                Container(
                                    border_radius=20,
                                    
                                    
                                    width=85,
                                    height=45,
                                    padding=15,
                                    content=Container(
                                        bgcolor=FWG,
                                       
                                        on_click=open_dlg_modal,
                                        content=Column(
                                            controls=[
                                                Text("Pay", color='#FFFFFF')  
                                            ]
                                        )
                                    )
                                )
                            ]
                            )
                    ]
                )
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='spaceBetween',
                    controls=[
                        Container(
                            content=Icon(icons.MENU)),
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]
                    ),
                Container(height=20),
                Text(
                    size=25,
                    weight=FontWeight.BOLD,
                    value='What\'s up, Dos!'
                ),
                Text(
                    value='FRIENDS'
                ),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content=friends_card
                )
            ],
        ),
    )

    def button_clicked(e):
        output_text.value = f"Save Successful!!"
        page.update()
        output_text = Text()

  

    second_page_contents = Container(
    content=Column(
        controls=[
            Container(
                content=Text('Add Bill', size=20, weight=FontWeight.BOLD),
                bgcolor='green',
                padding=padding.all(10),
            ),

            Container(
                content=TextField(
                    label="Add Title for Bill",
                    hint_text="Add Title here",
                    width=380,
                    border_color="green",
                ),
                margin=margin.only(top=10),
            ),

            Container(
                content=TextField(
                    label="Amount",
                    hint_text="Add Amount here",
                    width=380,
                    border_color="green",
                ),
                margin=margin.only(top=10),
            ),

            Container(
                content=Dropdown(
                    label="Bill or Expense",
                    hint_text="click for options",
                    width=380,
                    border_color="green",
                    options=[
                        dropdown.Option("Bill"),
                        dropdown.Option("Expense"),
                    ],
                ),
                margin=margin.only(top=10),
            ),

            Container(
                content=Dropdown(
                    label="Select Group",
                    hint_text="click for options",
                    width=380,
                    border_color="green",
                    options=[
                        dropdown.Option("Group 1"),
                        dropdown.Option("Group 2"),
                        dropdown.Option("Group 3"),
                    ],
                ),
                margin=margin.only(top=10),
            ),

            Container(
                content=Dropdown(
                    label="Split Actions",
                    hint_text="click for options",
                    width=380,
                    border_color="green",
                    options=[
                        dropdown.Option("Split equally"),
                        dropdown.Option("Custom"),
                        dropdown.Option("According to item"),
                    ],
                ),
                margin=margin.only(top=10),
            ),

            

            Container(
                content=ElevatedButton(
                    text='Save',
                    on_click=save,
                    bgcolor='green',
                    width=100
                ),
                
                margin=margin.only(top=20),
            ),

            Text(),
        ]
    )
 )

    


    tab_1 = Container(
        visible=True,
        content=Column(
            controls=[
                first_page_contents
            ]
        )
    )

    tab_2 = Container(
        visible=True,
        content=Column(
            controls=[
                second_page_contents
            ]
        )
    )

    tab_3 = Text("Tab 3", size=30, visible=False)

    page.add(
        Container(
            margin=margin.only(
                left=50
            ),
            content=Column([
                tab_1,
                tab_2,
                tab_3
            ])
        )
    )

   


app(target=main)

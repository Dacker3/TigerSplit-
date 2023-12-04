from flet import *


def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    WHITE = '#FFFFFF'

    page.update()

    def close_dlg(e):
        dlg_modal.open = False
        page.update()

    dlg_modal = AlertDialog(
        modal=True,
        title=Text("Please Confirm"),
        content=Text("Do you really wish to make this payment"),
        actions=[
            TextButton("Yes", on_click=close_dlg),
            TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dismissed"),
    )

    def open_dlg_modal(e):
        
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()

    #These defs are for add bill buttons
    def close_dlg_bill(e):
        dlg_modal_bill.open = False
        page.update()

    dlg_modal_bill = AlertDialog(
        modal=True,
        title=Text("Adding bill"),
        content=Text("Are you sure you want to add this bill/expense?"),
        actions=[
            TextButton("Yes", on_click=close_dlg_bill),
            TextButton("No", on_click=close_dlg_bill),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dismissed"),
    )

    def open_dlg_modal_bill(e):
        page.dialog = dlg_modal_bill
        dlg_modal_bill.open = True
        page.update()


    #These defs are for settings when you want to add a payment
    def close_textfield(e):
        textfield_dialog.open = False
        page.update()
       # page.dialog = None  # Remove the reference to the dialog
        textfield_dialog.modal   = False
        page.remove(textfield_dialog)
        page.update()

    def close_dlg_settings(e):
        #dlg_modal_settings.open = False
        #textfield_dialog.open = False
        #dlg_modal_settings.visible = False
        #dlg_modal_settings.open = False
        #page.dialog.disabled = True
        #textfield_dialog.open = False
        
        dlg_modal_settings.open = False
        page.update()
        dlg_modal_settings.modal = False
       # page.dialog.visible = False
        page.remove(dlg_modal_settings)
        page.update()

    # Create an AlertDialog with the TextField
    textfield_dialog = AlertDialog(
       # modal=True,
        title=Text("Enter Payment tag"),
        content = Row(controls =[
            TextField(label="click here", width=200),
            TextButton("Submit", on_click=close_textfield),
            ElevatedButton("CANCEL", bgcolor="red", on_click=close_textfield),
        ],
      #  on_dismiss=lambda ev: page.update(), 
      alignment=MainAxisAlignment.END,

    ), on_dismiss=close_dlg_settings)
   
    def open_textfield(e):
        page.add(textfield_dialog)
        
       # page.dialog = textfield_dialog
        textfield_dialog.open = True
        page.update()



    dlg_modal_settings = AlertDialog(
       # modal=True,
        title=Text("Choose payment method"),
        content = Row(controls=[
            TextButton("Cashapp", icon="attach_money", on_click=open_textfield),
            TextButton("PayPal", icon="paypal", on_click=open_textfield),
            TextButton("Venmo", icon="v", on_click=open_textfield),
            ElevatedButton("CANCEL", bgcolor="red", on_click=close_dlg_settings),
        ],
        alignment=MainAxisAlignment.END,
        
       # on_dismiss=lambda e: print("Modal dismissed"),
    ))

    def open_dlg_modal_settings(e):
      #  page.dialog = dlg_modal_settings
        page.add(dlg_modal_settings)
        dlg_modal_settings.open = True
       # page.dialog.visible = True
        page.update()


    def changetab(e):
        my_index = e.control.selected_index
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        tab_3.visible = True if my_index == 2 else False
        page.update()

    page.navigation_bar = NavigationBar(
        bgcolor="green",
        on_change=changetab,
        selected_index=0,
        destinations=[
            NavigationDestination(icon="home"),
            NavigationDestination(icon="Add"),
            NavigationDestination(icon="settings"),
        ]
    )

    friends_card = Row(scroll='auto')

    # friends = ['Sally', 'Fred', 'Ethan', 'Dos', 'Johnny']
    # for index, value in enumerate(friends):
    #     friends_card.controls.append(
    #         Container(
    #             border_radius=20,
    #             bgcolor=FWG,
    #             width=150,
    #             height=110,
    #             padding=15,
    #             content=Column(
    #                 controls=[
    #                     Row(alignment='center', controls=[Text(value)]),
    #                     Row(alignment='center',
    #                         controls=[
    #                             Container(
    #                                 border_radius=20,
    #                                 bgcolor=FG,
    #                                 width=85,
    #                                 height=45,
    #                                 padding=15,
    #                                 content=Column(controls =[Container(
    #                                     Text("Pay"),
    #                                     on_click=open_dlg_modal,
    #                                 )
    #                                 ])
    #                             ), Container(
    #                                 border_radius=20,
    #                                 bgcolor=FG,
    #                                 width=85,
    #                                 height=45,
    #                                 padding=15,
    #                                 content=Column(controls =[Container(
    #                                     Text("delete"),
    #                                     on_click=open_dlg_modal,
    #                                 )
    #                                 ])
    #                             )
    #                         ]
    #                         )
    #                 ]
    #             )
    #         )
    #     )

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
                        on_click=open_dlg_modal_bill,
                        bgcolor='green',
                        width=100
                    ),

                    margin=margin.only(top=20),
                ),

                Text(),
            ]
        )
    )

    third_page_contents = Container(
        content=Column(
            controls=[
                Container(
                    content=Text('Settings', size=20, weight=FontWeight.BOLD),
                    bgcolor='green',
                    padding=padding.all(10),
                ),

                Container(
                    content=ElevatedButton(
                        text='Add new Payment',
                        on_click=open_dlg_modal_settings,
                        bgcolor='green',
                        width=100
                    ),

                    margin=margin.only(top=20),
                ),

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
        visible=False,
        content=Column(
            controls=[
                second_page_contents
            ]
        )
    )

    tab_3 = Container(
        visible=False,
        content=Column(
            controls=[
                third_page_contents
            ]
        )
    )
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

    page_1 = Container()

    page_2 = Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(
                    top=50, left=20,
                    right=20, bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_contents
                    ]
                )
            )
        ]
    )

    container = Container(
        width=500,
        height=500,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )


app(target=main)

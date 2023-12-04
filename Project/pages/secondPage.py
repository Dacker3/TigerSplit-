import flet as ft

class SecondPage(ft.UserControl):
 def build(self):

      return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text('Add Bill', size=20, weight=ft.FontWeight.BOLD),
                    bgcolor='green',
                    padding=ft.padding.all(10),
                ),

                ft.Container(
                    content=ft.TextField(
                        label="Add Title for Bill",
                        hint_text="Add Title here",
                        width=380,
                        border_color="green",
                    ),
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content=ft.TextField(
                        label="Amount",
                        hint_text="Add Amount here",
                        width=380,
                        border_color="green",
                    ),
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content=ft.Dropdown(
                        label="Bill or Expense",
                        hint_text="click for options",
                        width=380,
                        border_color="green",
                        options=[
                            ft.dropdown.Option("Bill"),
                            ft.dropdown.Option("Expense"),
                        ],
                    ),
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content=ft.Dropdown(
                        label="Select Group",
                        hint_text="click for options",
                        width=380,
                        border_color="green",
                        options=[
                            ft.dropdown.Option("Group 1"),
                            ft.dropdown.Option("Group 2"),
                            ft.dropdown.Option("Group 3"),
                        ],
                    ),
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content=ft.Dropdown(
                        label="Split Actions",
                        hint_text="click for options",
                        width=380,
                        border_color="green",
                        options=[
                            ft.dropdown.Option("Split equally"),
                            ft.dropdown.Option("Custom"),
                            ft.dropdown.Option("According to item"),
                        ],
                    ),
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content=ft.ElevatedButton(
                        text='Save',
                       # on_click=open_dlg_modal_bill,
                        bgcolor='green',
                        width=100
                    ),

                    margin=ft.margin.only(top=20),
                ),

                ft.Text(),
            ]
        )
    )
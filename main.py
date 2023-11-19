from flet import *
import array as arr

#searchbar classes
class Navigation(UserControl):

    def __init__(self, t, func):
        super().__init__()
        self.text = t
        self.changeFunc = func

        #   text = "a"
    def build(self):
        return NavigationBar(
            on_change=self.changeFunc,

            destinations=[
                NavigationDestination(icon=icons.EXPLORE, label=self.text),
                NavigationDestination(icon=icons.COMMUTE, label="Commute"),
                NavigationDestination(
                    icon=icons.BOOKMARK_BORDER,
                    selected_icon=icons.BOOKMARK,
                    label="Explore",
                    ),
                ]
            )

class FriendCard(UserControl):
    name = "noName"
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    WHITE = '#FFFFFF'
    friendlist = []

    def __init__(self, n, d, friendlist):
        super().__init__()
        self.friendlist = friendlist
        self.name = n
        self.deleteFriend = d

    def deleteClicked(self, e):
        self.deleteFriend(self)
        self.update()

    def build(self):
        return Container(


            border_radius=20,
            bgcolor=self.FWG,
            width=150,
            height=110,
            padding=15,
            content=Column(
                controls=[
                    ElevatedButton("Pay",
                        on_click=self.deleteClicked, bgcolor="green"
                    ),
                    Row(alignment='center', controls=[Text(self.name) ]),
                    Row(alignment='center',
                           controls=[
                               Container(
                                   border_radius=20,
                                   bgcolor=self.FWG,
                                   width=85,
                                   height=45,
                                   padding=15,
                                   content=Container(

                                   )
                               )
                           ]
                           )
                ]
            )
        )


class FriendsList(UserControl):
    friends_card = Row(scroll='auto')
    friends = []

    def renderFriends(self):
        return

    def build(self):
        return self.friends_card

    def deleteFriend(self, friend: FriendCard):
        self.friends_card.controls.remove(friend)
        self.update()
        return

    def addFriend(self, name):
        self.friends_card.controls.append(FriendCard(name, self.deleteFriend, 0))

        self.update()
        return


class Friend():
    name = ""
    username = ""


class Friends():
    friends = [arr]

    def __init__(self, friends: arr):
        self.friends = friends

    def getFriends(self):
        return self.friends

    def addFriend(self, name):
        f = Friend()
        f.name = name
        self.friends.append(f)
        return


class Users():
    users = ["avery", "tommy", "ethan", "derek", "todd", "justin", "michael"]

    def findUsers(self, str):
        matches = []
        for i in range(len(self.users)):
            if (str in self.users[i]):
                print(self.users[i])
                matches.append(self.users[i])

            print(matches)
        return matches


class SearchBar():
    changeText = 0

    page = 0

    def changeList(self, e):
        self.list = self.changeText(self, e.control.value)

    def __init__(self, change):
        self.changeText = change

    def getSearchBar(self):
        return TextField(
            label="avery",
            icon=icons.FORMAT_SIZE,
            hint_text="type a username",
            helper_text="",
            counter_text="0 symbols typed",
            prefix_icon=icons.SEARCH,
            suffix_text="",
            on_change=self.changeList
        )


class userCard(UserControl):
    addFriend = 0

    def __init__(self, name, addFriend):
        super().__init__()
        self.addFriend = addFriend
        self.name = name

    def build(self):
        return Container(content=Column(controls=[
            IconButton(
                icon=icons.DONE_OUTLINE_OUTLINED,
                icon_color=colors.GREEN,
                tooltip="Update To-Do",
                # on_click=self.addFriend,
                data=(self.name),
                ## <-------------------- store the reference to the button in a tuple. You could store it in a dictionary or whatever else you want
                on_click=lambda e: self.addFriend(e.control.data)
            ), Text(self.name)]))


def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'
    WHITE = '#FFFFFF'

    page.update()



    users = Users()
    lv = ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    def render(z):
        lv.controls.clear()
        print(len(z))
        for i in range(len(z)):
            lv.controls.append(userCard(z[i], addFriend))
            print(len(z))

            page.update()

    def change(self, e):
        # self.z = users.findUsers(e)
        print(users.findUsers(e))
        # print(z)
        render(users.findUsers(e))

    friends = ['Sally', 'Fred', 'Ethan', 'Dos', 'Johnny']
    friends_card = FriendsList()
    page.add(friends_card)
    for i in range(len(friends)):
        friends_card.addFriend(friends[i])

    def addFriend(name):
        friends_card.addFriend(name)
        friends.append(name)
        page.update()
        return

    def removeFriend():
        return

    #search bar stuff
    s = SearchBar(change)
    x = s.getSearchBar()

    nav = Navigation("his", change)



    # These are for controlling buttons
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
        dlg_modal_settings.open = False
        page.update()

    def close_dlg_settings(e):
        dlg_modal_settings.open = False
        page.update()

    # Create an AlertDialog with the TextField
    textfield_dialog = AlertDialog(
        modal=True,
        title=Text("Enter Payment tag"),
        actions=[
            TextField(label="click here", width=200),
            TextButton("Submit", on_click=close_textfield),
            ElevatedButton("CANCEL", bgcolor="red", on_click=close_textfield),
        ],
        on_dismiss=lambda e: print("Modal dismissed"),
    )

    def open_textfield(e):
        page.dialog = textfield_dialog
        textfield_dialog.open = True
        page.update()



    dlg_modal_settings = AlertDialog(
        modal=True,
        title=Text("Choose payment method"),
        actions=[
            TextButton("Cashapp", icon="attach_money", on_click=open_textfield),
            TextButton("PayPal", icon="paypal", on_click=open_textfield),
            TextButton("Venmo", icon="v", on_click=open_textfield),
            ElevatedButton("CANCEL", bgcolor="red", on_click=close_dlg_settings),
        ],
        actions_alignment=MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dismissed"),
    )

    def open_dlg_modal_settings(e):
        page.dialog = dlg_modal_settings
        dlg_modal_settings.open = True
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


    lv = ListView(expand=1, spacing=10, padding=20, auto_scroll=True)


    first_page_contents = Container(
        content=Column(
            controls=[
                Row(alignment='top',
                    controls=[
                        Text("People you owe")
                    ]
                    ),
                Container(height=20),
                Text(
                    size=25,
                    weight=FontWeight.BOLD,
                    value='What\'s up, Dos!'
                ),
                Text(
                    value='FRIENDS SEARCH'
                ),


                x,  # Search bar
                lv,  # ListView

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
                        width=200
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

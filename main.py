from flet import *

def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG ='#3450a1'
    PINK = '#eb06ff'

    friends_card = Row(
        scroll = 'auto'
    )

    friends = ['Sally', 'Fred', 'Ethan', 'Dos', 'Johnny']
    for index, value in enumerate(friends):
        friends_card.controls.append(
            Container(
                border_radius=20,
                bgcolor = BG,
                width =150,
                height = 110,
                padding = 15,
                content = Column(
                    controls=[
                        Row(alignment = 'center', controls= [Text(value)]),
                        Row(alignment = 'center',
                            controls = [
                                Container(
                                border_radius=20,
                                bgcolor = FG,
                                width =85,
                                height = 45,
                                padding = 15,
                                content = Container(
                                    Row(alignment = 'center', controls= [Text(value = 'Pay Now')])
                                    )
                                )
                            ]
                        )
                    ]
                )

            )
        )

    first_page_contents = Container(
        content = Column(
            controls = [
                Row(alignment = 'spaceBetween',
                    controls = [
                        Container(
                            content = Icon(icons.MENU)),
                            Row(
                                controls = [
                                    Icon(icons.SEARCH),
                                    Icon(icons.NOTIFICATIONS_OUTLINED)
                                ]
                        )
                    ]
                ),
                Container(height=20),
                Text(
                  size = 25,
                  weight = FontWeight.BOLD,
                  value = 'What\'s up, Dos!'
                ),
                Text(
                  value = 'FRIENDS'
                ),
                Container(
                    padding = padding.only(top=10,bottom=20,),
                    content = friends_card
                )
            ],
        ),
    )
    page_1 = Container()
    page_2 = Row(
        controls = [
            Container(
                width = 400,
                height = 850,
                bgcolor =FG,
                border_radius = 35,
                padding = padding.only(
                    top=50,left=20,
                    right=20,bottom=5
                ),
                content = Column(
                    controls= [
                        first_page_contents
                    ]
                )
            )
        ]
    )

    container = Container(
        width = 500,
        height = 500,
        bgcolor = BG,
        border_radius = 35,
        content = Stack (
            controls = [
                page_1,
                page_2
            ]
        )
    )
    page.add(container)

app(target=main)

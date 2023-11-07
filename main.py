
import flet as ft
from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment

def main(page: Page) -> None:
    page.title = "Split"

    def route_change(e: RouteChangeEvent) -> None:
        page.views.clear()

        # home
        page.views.append(
            View(
                route='/',
                controls=[
                    AppBar(title=Text('Home'), bgcolor='purple'),
                    Text(value='Home',size=80),
                    ElevatedButton(text="Split Bill", on_click=lambda _: page.go('/split'))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.Center,
                spacing=26
            )
        )

        if page.route == '/split':
             page.views.append(
                View(
                    route='/split',
                    controls=[
                        AppBar(title=Text('Split'), bgcolor='purple'),
                        Text(value='Split',size=80),
                        ElevatedButton(text="Go Back Home", on_click=lambda _: page.go('/home'))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.Center,
                    spacing=26
                )
            )
        page.update()


    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    if __name__ == '__main__':
        ft.app(target=main)

import reflex as rx 

from ..ui.base import base_page

# @rx.page(route='/about')
def about_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("About Us", size="9"),
            rx.text(
                "Something cool about us.",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id='my-child'
        )
    return base_page(my_child)
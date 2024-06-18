import reflex as rx 

from .. import navigation
from ..articles.list import article_public_list_component


def landing_component() -> rx.Component:
    return rx.vstack(
            # rx.theme_panel(default_open=True),
            rx.heading("Welcome to SaaS", size="9"),
            rx.link(
                rx.button("About us", color_scheme='gray'), 
                href=navigation.routes.ABOUT_US_ROUTE
            ),
            rx.divider(),
            rx.heading("Recent Articles", size="5"),
            article_public_list_component(columns=1, limit=1),
            spacing="5",
            justify="center",
            align="center",
            # text_align="center",
            min_height="85vh",
            id='my-child'
        )
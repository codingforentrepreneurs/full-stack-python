import reflex as rx

from reflex_local_auth.pages.login import LoginState, login_form
from reflex_local_auth.pages.registration import RegistrationState, register_form

from .. import navigation
from ..ui.base import base_page

from .forms import my_register_form
from .state import SessionState

def my_login_page()->rx.Component:
    return base_page(
        rx.center(
            rx.cond(
                LoginState.is_hydrated,  # type: ignore
                rx.card(login_form()),
            ),
             min_height="85vh",
        ),
       
    )

def my_register_page()->rx.Component:
    return base_page(
        rx.center(
            rx.cond(
                RegistrationState.success,
                rx.vstack(
                    rx.text("Registration successful!"),
                ),
                rx.card(my_register_form()),
                
            ),
             min_height="85vh",
        )
       
    )


def my_logout_page() -> rx.Component:
    # Welcome Page (Index)
    my_child = rx.vstack(
            rx.heading("Are you sure you want logout?", size="7"),
            rx.link(
                rx.button("No", color_scheme="gray"),
                href=navigation.routes.HOME_ROUTE
            ),
            rx.button("Yes, please logout", on_click=SessionState.perform_logout),
            spacing="5",
            justify="center",
            align="center",
            # text_align="center",
            min_height="85vh",
            id='my-child'
        )
    return base_page(my_child)


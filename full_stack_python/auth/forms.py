import reflex as rx
import reflex_local_auth
from reflex_local_auth.pages.components import input_100w, MIN_WIDTH

from .state import MyRegisterState

def register_error() -> rx.Component:
    """Render the registration error message."""
    return rx.cond(
        reflex_local_auth.RegistrationState.error_message != "",
        rx.callout(
            reflex_local_auth.RegistrationState.error_message,
            icon="triangle_alert",
            color_scheme="red",
            role="alert",
            width="100%",
        ),
    )


def my_register_form() -> rx.Component:
    """Render the registration form."""
    return rx.form(
        rx.vstack(
            rx.heading("Create an account", size="7"),
            register_error(),
            rx.text("Username"),
            input_100w("username"),
            rx.text("Email"),
            input_100w("email", type='email'),
            rx.text("Password"),
            input_100w("password", type="password"),
            rx.text("Confirm Password"),
            input_100w("confirm_password", type="password"),
            rx.button("Sign up", width="100%"),
            rx.center(
                rx.link("Login", on_click=lambda: rx.redirect(reflex_local_auth.routes.LOGIN_ROUTE)),
                width="100%",
            ),
            min_width=MIN_WIDTH,
        ),
        on_submit=MyRegisterState.handle_registration_email,
    )
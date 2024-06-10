"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    label = "This is my label"
    orginal_label = "This is my label"

    def change_label(self):
        if self.label == "Cool label.":
            self.label = self.orginal_label
        else:
            self.label = "Cool label."


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="bottom-left"),
        rx.vstack(
            rx.heading(State.label, " Welcome to Reflex!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                on_click=State.change_label,
                size="5",
            ),
            # rx.button("Do something!", on_click=State.change_label),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)

import reflex as rx

from ..auth.state import SessionState
from .nav import navbar
from .dashboard import base_dashboard_page

def base_layout_component(child, *args, **kwargs) -> rx.Component:
    return rx.fragment( # renders nada
        navbar(),
        rx.box(
            child,
            # bg=rx.color("accent", 3),
            padding="1em",
            width="100%",
            id="my-content-area-el"
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
        # padding='10em',
        # id="my-base-container"
    )

def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    if not isinstance(child,rx. Component):
        child = rx.heading("this is not a valid child element")
    return rx.cond(
        SessionState.is_authenticated,
        base_dashboard_page(child, *args, **kwargs),
        base_layout_component(child, *args, **kwargs ),
    )
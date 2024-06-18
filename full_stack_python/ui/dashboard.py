import reflex as rx

from .sidebar import sidebar

def base_dashboard_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    # print([type(x) for x in args])
    if not isinstance(child,rx. Component):
        child = rx.heading("this is not a valid child element")
    return rx.fragment( 
        rx.hstack(
            sidebar(),
            rx.box(
                child,
                rx.logo(),
                # bg=rx.color("accent", 3),
                padding="1em",
                width="100%",
                id="my-content-area-el"
            ),
            
        ),
        # rx.color_mode.button(position="bottom-left"),
        # padding='10em',
        # id="my-base-container"
    )
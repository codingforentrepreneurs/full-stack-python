import reflex as rx 

from ..ui.base import base_page

def feature_item(feature: str) -> rx.Component:
    return rx.hstack(
        rx.icon(
            "check", color=rx.color("blue", 9), size=21
        ),
        rx.text(feature, size="4", weight="regular"),
    )


def standard_features() -> rx.Component:
    return rx.vstack(
        feature_item("40 credits for image generation"),
        feature_item("Credits never expire"),
        feature_item("High quality images"),
        feature_item("Commercial license"),
        spacing="3",
        width="100%",
        align_items="start",
    )


def popular_features() -> rx.Component:
    return rx.vstack(
        feature_item("250 credits for image generation"),
        feature_item("+30% Extra free credits"),
        feature_item("Credits never expire"),
        feature_item("High quality images"),
        feature_item("Commercial license"),
        spacing="3",
        width="100%",
        align_items="start",
    )


def pricing_card_standard() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "$14.99",
                    trim="both",
                    as_="s",
                    size="3",
                    weight="regular",
                    opacity=0.8,
                ),
                rx.text(
                    "$3.99",
                    trim="both",
                    size="6",
                    weight="regular",
                ),
                width="100%",
                spacing="2",
                align_items="end",
            ),
            height="35px",
            align_items="center",
            justify="between",
            width="100%",
        ),
        rx.text(
            "40 Image Credits",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
        ),
        standard_features(),
        rx.spacer(),
        rx.button(
            "Purchase",
            size="3",
            variant="outline",
            width="100%",
            color_scheme="blue",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('gray', 5)}",
        background=rx.color("gray", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )


def pricing_card_popular() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.hstack(
                rx.text(
                    "$69.99",
                    trim="both",
                    as_="s",
                    size="3",
                    weight="regular",
                    opacity=0.8,
                ),
                rx.text(
                    "$18.99",
                    trim="both",
                    size="6",
                    weight="regular",
                ),
                width="100%",
                spacing="2",
                align_items="end",
            ),
            rx.badge(
                "POPULAR",
                size="2",
                radius="full",
                variant="soft",
                color_scheme="blue",
            ),
            align_items="center",
            justify="between",
            height="35px",
            width="100%",
        ),
        rx.text(
            "250 Image Credits",
            weight="bold",
            size="7",
            width="100%",
            text_align="left",
        ),
        popular_features(),
        rx.spacer(),
        rx.button(
            "Purchase",
            size="3",
            width="100%",
            color_scheme="blue",
        ),
        spacing="6",
        border=f"1.5px solid {rx.color('blue', 6)}",
        background=rx.color("blue", 1),
        padding="28px",
        width="100%",
        max_width="400px",
        min_height="475px",
        border_radius="0.5rem",
    )


def pricing_cards() -> rx.Component:
    return rx.flex(
        pricing_card_standard(),
        pricing_card_popular(),
        spacing="4",
        flex_direction=["column", "column", "row"],
        width="100%",
        align_items="center",
    )

def pricing_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Pricing", size="9"),
            pricing_cards(),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id='my-child'
        )
    return base_page(my_child)
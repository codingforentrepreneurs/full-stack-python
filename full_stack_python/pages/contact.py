import reflex as rx 

from .. import navigation
from ..ui.base import base_page


class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False

    @rx.var
    def thank_you(self):
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you {first_name}".strip() + "!"

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data
        self.did_submit = True
        # sleep -> timeout -> setTimeout
        # self.did_submit = False

@rx.page(route=navigation.routes.CONTACT_US_ROUTE)
def contact_page() -> rx.Component:
    my_form = rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        name="first_name",
                        placeholder="First Name",
                        required=True,
                        type='text',
                        width='100%',
                    ),
                    rx.input(
                        name="last_name",
                        placeholder="Last Name",
                        type='text',
                        width='100%',
                    ),
                    width='100%'
                ),
                rx.input(
                    name='email',
                    placeholder='Your email',
                    type='email',
                    width='100%',
                ),
                rx.text_area(
                    name='message',
                    placeholder="Your message",
                    required=True,
                    width='100%',
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
    )
    my_child = rx.vstack(
            rx.heading("Contact Us", size="9"),
            rx.cond(ContactState.did_submit, ContactState.thank_you, ""),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width='50vw'
                )
            ),
            rx.tablet_only(
                rx.box(
                    my_form,
                    width='75vw'
                )
            ),
            rx.mobile_only(
                rx.box(
                    my_form,
                    width='95vw'
                )
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id='my-child'
        )
    return base_page(my_child)
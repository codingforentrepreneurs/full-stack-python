import reflex as rx 
from ..ui.base import base_page
from ..models import ContactEntryModel
from . import form, state

def contact_entry_list_item(contact: ContactEntryModel):
    return rx.box(
        rx.heading(contact.first_name),
        rx.text("Message:", contact.message),
        rx.cond(contact.user_id, 
                rx.text("User Id:", f"{contact.user_id}",), 
                rx.fragment("")),
        padding='1em'
    )

# def foreach_callback(text):
#     return rx.box(rx.text(text))

def contact_entries_list_page() ->rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact Entries", size="5"),
            # rx.foreach(["abc", "abc", "cde"], foreach_callback),
            rx.foreach(state.ContactState.entries, contact_entry_list_item),
            spacing="5",
            align="center",
            min_height="85vh",
        )
    ) 

def contact_page() -> rx.Component:
    
    my_child = rx.vstack(
            rx.heading("Contact Us", size="9"),
            rx.cond(state.ContactState.did_submit, state.ContactState.thank_you, ""),
            rx.desktop_only(
                rx.box(
                    form.contact_form(),
                    width='50vw'
                )
            ),
            rx.tablet_only(
                rx.box(
                    form.contact_form(),
                    width='75vw'
                )
            ),
            rx.mobile_only(
                rx.box(
                    form.contact_form(),
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
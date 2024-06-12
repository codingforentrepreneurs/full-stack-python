import asyncio
import reflex as rx 

from .model import ContactEntryModel

class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False
    timeleft: int = 5

    @rx.var
    def timeleft_label(self):
        if self.timeleft < 1:
            return "No time left"
        return f"{self.timeleft} seconds"

    @rx.var
    def thank_you(self):
        first_name = self.form_data.get("first_name") or ""
        return f"Thank you {first_name}".strip() + "!"

    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        # print(form_data)
        self.form_data = form_data
        data = {}
        for k,v in form_data.items():
            if v == "" or v is None:
                continue
            data[k] = v
        with rx.session() as session:
            db_entry = ContactEntryModel(
                **data
            )
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            yield
        await asyncio.sleep(2)
        self.did_submit = False
        yield
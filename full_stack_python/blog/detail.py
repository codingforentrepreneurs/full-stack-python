import reflex as rx 

from ..ui.base import base_page

from . import state
from .notfound import blog_post_not_found
# @rx.page(route='/about')
def blog_post_detail_page() -> rx.Component:
    can_edit = True
    edit_link = rx.link("Edit", href=f"{state.BlogPostState.blog_post_edit_url}")
    edit_link_el = rx.cond(
        can_edit,
        edit_link,
        rx.fragment("")
    )
    my_child = rx.cond(state.BlogPostState.post, rx.vstack(
            rx.hstack(
                rx.heading(state.BlogPostState.post.title, size="9"),
                edit_link_el,
                align='end'
            ),
            rx.text("User info id ", state.BlogPostState.post.userinfo_id),
            rx.text("User info: ", state.BlogPostState.post.userinfo.to_string()),
            rx.text("User: ", state.BlogPostState.post.userinfo.user.to_string()),
            rx.text(state.BlogPostState.post.publish_date),
            rx.text(
                state.BlogPostState.post.content,
                white_space='pre-wrap'
            ),
            spacing="5",
            align="center",
            min_height="85vh"
        ), 
        blog_post_not_found()
        )
    return base_page(my_child)
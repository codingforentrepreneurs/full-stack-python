from typing import Optional, List
import reflex as rx 

from sqlmodel import select

from .model import BlogPostModel

class BlogPostState(rx.State):
    posts: List['BlogPostModel'] = []
    post: Optional['BlogPostModel'] = None

    def load_posts(self):
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel)
            ).all()
            self.posts = result
        # return

    # def get_post(self):
    #     with rx.session() as session:
    #         result = session.exec(
    #             select(BlogPostModel)
    #         )
    #         self.posts = result
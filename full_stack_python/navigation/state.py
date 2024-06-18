import reflex as rx
import reflex_local_auth
from . import routes

class NavState(rx.State):
    def to_home(self):
        return rx.redirect(routes.HOME_ROUTE)

    def to_register(self):
        return rx.redirect(reflex_local_auth.routes.REGISTER_ROUTE)
    
    def to_login(self):
        return rx.redirect(reflex_local_auth.routes.LOGIN_ROUTE)
    
    def to_logout(self):
        return rx.redirect(routes.LOGOUT_ROUTE)

    def to_about_us(self):
        return rx.redirect(routes.ABOUT_US_ROUTE)
    
    def to_articles(self):
        return rx.redirect(routes.ARTICLE_LIST_ROUTE)
    
    def to_blog(self):
        return rx.redirect(routes.BLOG_POSTS_ROUTE)
    def to_blog_add(self):
        return rx.redirect(routes.BLOG_POST_ADD_ROUTE)
    def to_blog_create(self):
        return self.to_blog_add()
    def to_contact(self):
        return rx.redirect(routes.CONTACT_US_ROUTE)
    def to_pricing(self):
        return rx.redirect(routes.PRICING_ROUTE)
    
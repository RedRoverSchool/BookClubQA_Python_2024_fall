from dotenv import load_dotenv
import os

load_dotenv()

username_teacher = os.getenv('USERNAME_TEACHER')
password_teacher = os.getenv('PASSWORD_TEACHER')

def test_create_listing_btn_changes_color_on_hover(header, login):
    header.visit()
    header.click_on_login_button()
    login.full_login(username_teacher, password_teacher)
    colors = header.hover_create_listing_btn()
    assert colors[0] != colors[1]

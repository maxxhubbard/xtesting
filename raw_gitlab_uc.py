from seleniumbase import SB
import time


with SB(uc=True, test=True) as sb:
    url = "https://kick.com/brutalles"
    sb.uc_open_with_reconnect(url, 5)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    sb.uc_gui_handle_captcha()
    start_time = time.time()
    duration = 100 * 60


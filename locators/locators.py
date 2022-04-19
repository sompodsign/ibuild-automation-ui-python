from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@placeholder='YOUR EMAIL *']")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='YOUR EMAIL *']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='LOGIN']")


class HomePageLocators:
    FAVICON = (By.XPATH, "//link[@rel='shortcut icon']")

    # TOP NAVIGATION
    LOGIN_LINK = (By.XPATH, "//a[normalize-space()='LogIn']")
    SIGNUP_LINK = (By.XPATH, "//a[normalize-space()='Sign Up']")
    LOGO = (By.XPATH, "//img[@src='assets/images/logo-IB.png']")

    # HERO SECTION
    MAIN_HERO_TEXT = (By.XPATH, "//div[@class='owl-item animated owl-animated-in fadeIn active']//div[contains(text(),"
                                "'Extraordinary Happens Everyday!')]")
    SUB_HERO_TEXT = (By.XPATH, "//div[@class='owl-item animated owl-animated-in fadeIn active']//div[@class='small-"
                               "banner-heading'][normalize-space()='The Community Where Something']")
    WATCH_NOW_BTN = (By.XPATH, "//div[@class='owl-item animated owl-animated-in fadeIn']//button[@class='rubik-font"
                               " IB_Button IB_Button_Watch_Video btn communityIB_Button_Watch_Video comon-btn blue']"
                               "[normalize-space()='Watch Video']")

    # SECOND HERO SECTION
    JOIN_TODAY_BTN = (By.XPATH, "(//button[.=' JOIN TODAY!'])[1]")
    INDYBUILD_FOR_FANS = (By.XPATH, "//button[normalize-space()='IndyBuild For Fans']")
    INDYBUILD_FOR_ARTISTS = (By.XPATH, "//button[normalize-space()='IndyBuild For Artists']")

    # footer section
    FOOTER_LOGO = (
        By.XPATH, "//img[@src='assets/images/join-logo.png']")
    FOOTER_MENU_ITEMS = (By.XPATH, "//footer[@class='footer-main']")
    COPYRIGHT_TEXT = (By.XPATH, "//div[@class='dae leftd']")

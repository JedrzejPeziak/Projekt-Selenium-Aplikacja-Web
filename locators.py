from selenium.webdriver.common.by import By

class MainPageLocators():
    SEARCH_BUTTON = (By.NAME, 'yt1')
    CLOSE_COOKIES_BUTTON = (By.CLASS_NAME, 'cc-cookie-accept')
    CONTACT_BUTTON = (By.XPATH, "//a[contains(text(),'Kontakt')]")

class SearchPageLocators():
    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(),'wyszukaj nieruchomość')]")
    AREA_FROM = (By.ID, 'area_from')
    AREA_TO = (By.ID, 'area_to')
    FIRST_OFFER = (By.XPATH, "//*[@class='invest-desc']/a")
    #following-sibling - point to the next node on the same tree level
    ALL_INVESTMENT_AREAS = (By.XPATH, "//td[contains(text(),'Powierzchnia')]/following-sibling::td/span")
    FAVOURITE_BUTTON = (By.XPATH, "//*[@class='icon icon-heart']")
    NUMBER_OF_FAVOURITES = (By.XPATH, "//*[@title='Schowek']/span")
    INFO_BAR_OPACITY_1 = (By.XPATH, "//*[@id='eCms-alert'][@style='opacity: 1; display: none;']")
    INFO_BAR_OPACITY_2 = (By.XPATH, "//*[@id='eCms-alert'][@style='display: none; opacity: 1;']")
    INFO_BAR_NO_OPACITY = (By.XPATH, "//*[@id='eCms-alert'][@style='display: none;']")

class InvestitionPageLocators():
    AREA_INFO = (By.XPATH, "//*[contains(text(),'Powierzchnia')]//strong")
    TELEPHONE_NUMBER = (By.XPATH, "//div[@class='hide_part tel']/span[@class='text']")
    SEND_BUTTON = (By.NAME, "submit_contact")
    SHOW_NUMBER_BUTTON = (By.CLASS_NAME, "hidde_button")
    PRICE_BUTTON = (By.XPATH, "//*[contains(text(),'Zapytaj o ceny')]")
    NAME_INPUT = (By.NAME, "Form[form_name]")
    EMAIL_INPUT = (By.NAME, "Form[form_email]")
    #parent::* - point to the last child in this node's tree
    ACCEPT_CHECKBOX = (By.XPATH, "//*[@name='Form[form_agreement]']/parent::*")
    SUCCESS_EMAIL_SENT = (By.CLASS_NAME, "alert in alert-block fade alert-success")

class ContactPageLocators():
    SEND_BUTTON = (By.XPATH, "//button[contains(text(),'wyślij wiadomość')]")
    EMAIL_FIELD = (By.ID, "EContactForm_email")
    EMAIL_ERROR = (By.ID, "EContactForm_email_em_")
    CHECKBOX = (By.CLASS_NAME, 'control-label')
    CHECKBOX_ERROR = (By.ID, "EContactForm_form_agreement_em_")
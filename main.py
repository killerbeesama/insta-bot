from instagram import Instagram



SEARCH = "<name of the person you wanna search>"

MESSAGE = "<your message>"

USER_NAME = "<your username>"
PASSWORD = "<your password>"

CHROME_DRIVER_PATH = "<your path to driver>"

instagram = Instagram(CHROME_DRIVER_PATH,USER_NAME,PASSWORD)

instagram.search(SEARCH)
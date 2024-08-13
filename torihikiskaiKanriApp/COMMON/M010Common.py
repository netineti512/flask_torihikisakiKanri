from typing import Final

class M010Common:
    def __init__(self):
        self.URL_HTML: Final[str] = "./M010LoginGmn.html"
        
        self.GMN_ID: Final[str] = "M010"
        
        self.SHAIN_CD: Final[dict] = {"id":"M010ShainCd", "name":"社員コード"}
        self.PASSWORD: Final[dict] = {"id":'M010Password', "name":"パスワード"}
        
        self.BACK_BTN: Final[str] = "M010BackBtn"
        self.HIDDEN_SHAIN_CD: Final[str] = "M010HiddenShainCd"
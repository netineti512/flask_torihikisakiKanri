from typing import Final

class M011Common:
    def __init__(self):
        self.URL_HTML: Final[str] = "./M011PasswordChangeGmn.html"
        
        self.GMN_ID: Final[str] = "M011"
        
        self.SHAIN_CD: Final[dict] = {"id":"M011ShainCd", "name":"社員コード"}
        self.OLD_PASSWORD: Final[dict] = {"id":"M011OldPassword", "name":"現在のパスワード"}
        self.NEW_PASSWORD: Final[dict] = {"id":"M011NewPassword", "name":"新規のパスワード"}
        
        self.PASSWORD_CHANGE_BTN: Final[str] = "M011PasswordChangeBtn"
        self.BACK_BTN: Final[str] = "M011BackBtn"
        
        self.HIDDEN_SHAIN_CD: Final[str] = "M011HiddenShainCd"
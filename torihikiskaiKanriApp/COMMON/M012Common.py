from typing import Final

class M012Common:
    def __init__(self):
        self.URL_HTML: Final[str] = "./M012KanrihaPageGmn.html"
        
        self.GMN_ID: Final[str] = "M012"
        
        self.SHAIN_CD: Final[dict] = {"id":"M012ShainCd", "name":"社員コード"}
        self.SHAIN_NM: Final[dict] = {"id":"M012ShainNm", "name":"社員名"}
        self.PASSWORD: Final[dict] = {"id":'M012Password', "name":"パスワード"}
        self.KENGEN_FLG: Final[dict] = {"id":'M012KengenFlg', "name":"権限"}
        
        self.BACK_BTN: Final[str] = "M012BackBtn"
        self.INSERT_BTN: Final[str] = "M012InsertBtn"
        self.DELETE_BTN: Final[str] = "M012DeleteBtn"
        
        self.HIDDEN_SHAIN_CD: Final[str] = "M12HiddenShainCd"
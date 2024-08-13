from typing import Final

class T011Common:
    def __init__(self):
        self.URL_HTML: Final[str] = "./T011TorihikisakiEditGmn.html"
        
        self.GMN_ID: Final[str] = "T011"
        
        self.TORI_CD: Final[dict] = {"id":"T011ToriCd", "name":"取引先コード"}
        self.TORI_NM: Final[dict] = {"id":"T011ToriNm", "name":"取引先名称"}
        self.TORI_KANA: Final[dict] = {"id":"T011ToriKana", "name":"取引先仮名"}
        self.TORI_KBN: Final[dict] = {"id":"T011ToriKbn", "name":"取引先区分"}
        self.TORI_TEL: Final[dict] = {"id":"T011ToriTel", "name":"取引先番号"}
        self.TORI_SHOHIN: Final[dict] = {"id":"T011ToriShohin", "name":"取引商品"}
        self.NAIGAI_KBN: Final[dict] = {"id":"T011NaigaiKbn", "name":"国内外区分"}
        self.ZIP_CODE: Final[dict] = {"id":"T011ZipCode", "name":"郵便番号"}
        self.ADD1: Final[dict] = {"id":"T011Add1", "name":"住所1"}
        self.ADD2: Final[dict] = {"id":"T011Add2", "name":"住所2"}
        self.TANTOBUSHO: Final[dict] = {"id":"T011Tantobusho", "name":"担当部署"}
        self.TANTOSHA: Final[dict] = {"id":"T011Tantosha", "name":"担当者"}
        self.TANTOBUSHO_TEL: Final[dict] = {"id":"T011TantoBushoTel", "name":"担当部署番号"}
        self.PAY_JOKEN: Final[dict] = {"id":"T011PayJoken", "name":"支払条件"}
        self.DEPO_JOKEN: Final[dict] = {"id":"T011DepoJoken", "name":"入金条件"}
        self.TORI_START_DATE: Final[dict] = {"id":"T011ToriStartDate", "name":"取引開始日"}
        self.TORI_END_DATE: Final[dict] = {"id":"T011ToriEndDate", "name":"取引終了日"}
        self.MEMO: Final[dict] = {"id":"T011Memo", "name":"メモ"}
        
        self.HIDDEN_TORI_CD: Final[str] = "T011HiddenToriCd"

        self.BACK_BTN: Final[str] = "T011BackBtn"
        self.UPDATE_BTN: Final[str] = "T011UpdateBtn"
        self.DELETE_BTN: Final[str] = "T011DeleteBtn"
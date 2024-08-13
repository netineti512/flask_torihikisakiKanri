from typing import Final

class Message:
    def __init__(self):
        self.SUCCESS_MSG1: Final[str] = "パスワードが変更されました。"
        self.SUCCESS_MSG2: Final[str] = "ユーザーが登録されました。"
        self.SUCCESS_MSG3: Final[str] = "取引先情報が登録されました。"
        self.SUCCESS_MSG4: Final[str] = "取引先情報が削除されました。"
        self.SUCCESS_MSG5: Final[str] = "ユーザーが削除されました。"
        self.SUCCESS_MSG6: Final[str] = "取込が完了しました。"
        self.SUCCESS_MSG7: Final[str] = "出力が完了しました。"
        
        self.ERROR_MSG1: Final[str] = "ログインに失敗しました。社員コードもしくはパスワードが間違っています。"
        self.ERROR_MSG2: Final[str] = "パスワードの変更に失敗しました。社員コードもしくは現在のパスワードが間違っています。"
        self.ERROR_MSG3: Final[str] = "権限がありません。"
        self.ERROR_MSG4: Final[str] = "取引先が選択されていません。"
        self.ERROR_MSG5: Final[str] = "取引先情報が存在しません。"
        self.ERROR_MSG6: Final[str] = "権限がないので削除できません。"
        self.ERROR_MSG7: Final[str] = "取引先情報の登録に失敗しました。"
        self.ERROR_MSG8: Final[str] = "取引先情報の削除に失敗しました。"
        self.ERROR_MSG9: Final[str] = "ユーザーの削除に失敗しました。"
    
    def msg001(self, param: str) -> str:
        return f"{param}を入力してください。"
    
    def msg002(self, param1: str, param2: str) -> str:
        return f"「{param1}」と「{param2}」が等しいです。"
    
    def msg003(self, param: str, minSize: int, maxSize: int) -> str:
        return f"「{param}」の文字数を{minSize}文字以上{maxSize}文字以下にしてください。"
    
    def msg004(self, param: str) -> str:
        return f"「{param}」に記号が含まれています。"

    def msg005(self, param: str) -> str:
        return f"「{param}」は既に使用されています。"
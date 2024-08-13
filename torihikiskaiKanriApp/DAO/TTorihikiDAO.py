import sqlite3
import copy
import datetime

from typing import Final

from COMMON.Common import Common

common: Final[Common] = Common()

class TTorihikiDAO:
    
    def __init__(self) -> None:
        self.__dbname: Final[str] = './DB/TTorihiki.db'
        
        self.TABLENAME: Final[str] = "TTorihiki"
        
        self.TORICD: Final[str] = "toriCd"
        self.TORINM: Final[str] = "toriNm"
        self.TORIKANA: Final[str] = "toriKana"
        self.TORIKBN: Final[str] = "toriKbn"
        self.TORITEL: Final[str] = "toriTel"
        self.TORISHOHIN: Final[str] = "toriShohin"
        self.NAIGAIKBN: Final[str] = "naigaiKbn"
        self.ZIPCODE: Final[str] = "zipCode"
        self.ADD1: Final[str] = "add1"
        self.ADD2: Final[str] = "add2"
        self.TANTOBUSHO: Final[str] = "tantoBusho"
        self.TANTOSHA: Final[str] = "tantosha"
        self.TANTOBUSHOTEL: Final[str] = "tantoBushoTel"
        self.PAYJOKEN: Final[str] = "payJoken"
        self.DEPOJOKEN: Final[str] = "depoJoken"
        self.TORISTARTDATE: Final[str] = "toriStartDate"
        self.TORIENDDATE: Final[str] = "toriEndDate"
        self.MEMO: Final[str] = "memo"
        self.DELETEFLG: Final[str] = "deleteFlg"
        self.CREATEDATE: Final[str] = "createDate"
        self.CREATEUSER: Final[str] = "createUser"
        self.UPDATEDATE: Final[str] = "updateDate"
        self.UPDATEUSER: Final[str] = "updateUser"

        self.DELETEFLG_0: Final[str] = "0"
        self.DELETEFLG_1: Final[str] = "1"
        
        self.dic: Final[dict] = {
                    f"{self.TORICD}": common.BLANK,
                    f"{self.TORINM}": common.BLANK,
                    f"{self.TORIKANA}": common.BLANK,
                    f"{self.TORIKBN}": common.BLANK,
                    f"{self.TORITEL}": common.BLANK,
                    f"{self.TORISHOHIN}": common.BLANK,
                    f"{self.NAIGAIKBN}": common.BLANK,
                    f"{self.ZIPCODE}": common.BLANK,
                    f"{self.ADD1}": common.BLANK,
                    f"{self.ADD2}": common.BLANK,
                    f"{self.TANTOBUSHO}": common.BLANK,
                    f"{self.TANTOSHA}": common.BLANK,
                    f"{self.TANTOBUSHOTEL}": common.BLANK,
                    f"{self.PAYJOKEN}": common.BLANK,
                    f"{self.DEPOJOKEN}": common.BLANK,
                    f"{self.TORISTARTDATE}": common.BLANK,
                    f"{self.TORIENDDATE}": common.BLANK,
                    f"{self.MEMO}": common.BLANK,
                    f"{self.DELETEFLG}": common.BLANK,
                    f"{self.CREATEDATE}": common.BLANK,
                    f"{self.CREATEUSER}": common.BLANK,
                    f"{self.UPDATEDATE}": common.BLANK,
                    f"{self.UPDATEUSER}": common.BLANK
                   }
        
    def createTTorihikiDBFile(self) -> None:
        conn = sqlite3.connect(self.__dbname)
        conn.close()
    
    def createTTorihikiTable(self) -> None:
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        
        sql: str = f'CREATE TABLE {self.TABLENAME} ( \
                {self.TORICD} STRING PRIMARY KEY, \
                {self.TORINM} STRING, \
                {self.TORIKANA} STRING, \
                {self.TORIKBN} STRING, \
                {self.TORITEL} STRING, \
                {self.TORISHOHIN} STRING, \
                {self.NAIGAIKBN} STRING, \
                {self.ZIPCODE} STRING, \
                {self.ADD1} STRING, \
                {self.ADD2} STRING, \
                {self.TANTOBUSHO} STRING, \
                {self.TANTOSHA} STRING, \
                {self.TANTOBUSHOTEL} STRING, \
                {self.PAYJOKEN} STRING, \
                {self.DEPOJOKEN} STRING, \
                {self.TORISTARTDATE} STRING, \
                {self.TORIENDDATE} STRING, \
                {self.MEMO} STRING, \
                {self.DELETEFLG} STRING, \
                {self.CREATEDATE} STRING, \
                {self.CREATEUSER} STRING, \
                {self.UPDATEDATE} STRING, \
                {self.UPDATEUSER} STRING \
                )'
        
        cur.execute(sql)

        conn.commit()
        conn.close()
        
        common.writeDaoLog(sql)
        
    def insertTTorihiki(self) -> None:
        today = datetime.datetime.now()
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        
        sqlList: list = [f'INSERT INTO {self.TABLENAME} values("0001", "AAA", "AAA", "1", "08011112222", "電池","1", "555-4444", "鹿児島", "中野市", "営業課", "斉藤", "09011112222", "1", "1", "2024/12/12", "2025/12/24", "追加あり", "0", "{str(today)}", "admin", "", "")']
        
        for sql in sqlList:
            cur.execute(sql)
            common.writeDaoLog(sql)

        conn.commit()

        cur.close()
        conn.close()
        
    def selectTTorihiki(self) -> None:
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        
        sql: str = f'SELECT * FROM {self.TABLENAME}'

        cur.execute(sql)

        for data in cur.fetchall():
            print(data)

        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
    
    def selectAll(self) -> list:
        selectAll: list = []
        sql: str = f"SELECT * FROM {self.TABLENAME} WHERE {self.DELETEFLG} = '{self.DELETEFLG_0}'"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        
        for low in sorted(cur.fetchall()):
            dic = copy.copy(self.dic)
            for i in range(len(low)):
                dic[list(dic)[i]] = low[i]
            selectAll.append(dic)
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        return selectAll
    
    def selectTarget(self, dicTorihikisakiInfo: dict) -> list:
        selectTarget: list = []
        sql: str = f'SELECT * FROM {self.TABLENAME}'
        
        if dicTorihikisakiInfo[self.TORICD] != common.BLANK or dicTorihikisakiInfo[self.TORINM] != common.BLANK:
            sql = sql + f" WHERE {self.DELETEFLG} = '{self.DELETEFLG_0}' AND "
            
        if dicTorihikisakiInfo[self.TORICD] != common.BLANK:
            sql = sql + f"{self.TORICD} = '{dicTorihikisakiInfo[self.TORICD]}' "
        
        if dicTorihikisakiInfo[self.TORICD] != common.BLANK and dicTorihikisakiInfo[self.TORINM] != common.BLANK:
            sql = sql + f"or {self.TORINM} = '{dicTorihikisakiInfo[self.TORINM]}'"
        elif dicTorihikisakiInfo[self.TORICD] == common.BLANK and dicTorihikisakiInfo[self.TORINM] != common.BLANK:
            sql = sql + f"{self.TORINM} = '{dicTorihikisakiInfo[self.TORINM]}'"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        
        for low in sorted(cur.fetchall()):
            dic: dict = copy.copy(self.dic)
            for i in range(len(low)):
                dic[list(dic)[i]] = low[i]
            selectTarget.append(dic)
            
        cur.close()
        conn.close()
        common.writeDaoLog(sql)
        
        return selectTarget
    
    def selectOne(self, toriCd: str) -> list:
        selectOne: list = []
        sql: str = f"SELECT * FROM {self.TABLENAME} WHERE {self.TORICD} = '{toriCd}' AND {self.DELETEFLG} = '{self.DELETEFLG_0}'"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        
        for low in cur.fetchall():
            dic: dict = copy.copy(self.dic)
            for i in range(len(low)):
                dic[list(dic)[i]] = low[i]
            selectOne.append(dic)

        cur.close()
        conn.close()
        common.writeDaoLog(sql)
        
        return selectOne
    
    def blSelectTorihikisakiInfo(self, toriCd: str) -> bool:
        sql: str = f"SELECT * FROM {self.TABLENAME} WHERE {self.TORICD} = '{toriCd} and {self.DELETEFLG} = '{self.DELETEFLG_0}'"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        
        if len(cur.fetchall()) == common.INT_ONE:
            cur.close()
            conn.close()
            common.writeDaoLog(sql)
            
            return True
        else:
            cur.close()
            conn.close()
            common.writeDaoLog(sql)
            
            return False
    
    def blUpdateTorihikisakiInfo(self, dicTorihikisakiInfo: dict) -> bool:
        today = datetime.datetime.now()
        
        sql: str = f"UPDATE {self.TABLENAME} SET \
            {self.TORINM} = '{dicTorihikisakiInfo[self.TORINM]}', \
            {self.TORIKANA} = '{dicTorihikisakiInfo[self.TORIKANA]}', \
            {self.TORIKBN} = '{dicTorihikisakiInfo[self.TORIKBN]}', \
            {self.TORITEL} = '{dicTorihikisakiInfo[self.TORITEL]}', \
            {self.TORISHOHIN} = '{dicTorihikisakiInfo[self.TORISHOHIN]}', \
            {self.NAIGAIKBN} = '{dicTorihikisakiInfo[self.NAIGAIKBN]}', \
            {self.ZIPCODE} = '{dicTorihikisakiInfo[self.ZIPCODE]}', \
            {self.ADD1} = '{dicTorihikisakiInfo[self.ADD1]}', \
            {self.ADD2} = '{dicTorihikisakiInfo[self.ADD2]}', \
            {self.TANTOBUSHO} = '{dicTorihikisakiInfo[self.TANTOBUSHO]}', \
            {self.TANTOSHA} = '{dicTorihikisakiInfo[self.TANTOSHA]}', \
            {self.TANTOBUSHOTEL} = '{dicTorihikisakiInfo[self.TANTOBUSHOTEL]}', \
            {self.PAYJOKEN} = '{dicTorihikisakiInfo[self.PAYJOKEN]}', \
            {self.DEPOJOKEN} = '{dicTorihikisakiInfo[self.DEPOJOKEN]}', \
            {self.TORISTARTDATE} = '{dicTorihikisakiInfo[self.TORISTARTDATE]}', \
            {self.TORIENDDATE} = '{dicTorihikisakiInfo[self.TORIENDDATE]}', \
            {self.MEMO} = '{dicTorihikisakiInfo[self.MEMO]}', \
            {self.UPDATEDATE} = '{str(today)}', \
            {self.UPDATEUSER} = '{dicTorihikisakiInfo[common.USER_ID]}' \
             WHERE {self.TORICD} = {int(dicTorihikisakiInfo[self.TORICD])}"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        return True
    
    def updateDeleteFlg(self) -> bool:
        today = datetime.datetime.now()
        
        sql: str = f"UPDATE {self.TABLENAME} SET \
            {self.DELETEFLG} = '{self.DELETEFLG_0}', \
            {self.UPDATEDATE} = '{str(today)}', \
            {self.UPDATEUSER} = '{common.SYSTEM}'"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        return True
    
    def blDeleteTorihikisakiInfo(self, dicTorihikisakiInfo: dict) -> bool:
        today = datetime.datetime.now()
        
        sql: str = f"UPDATE {self.TABLENAME} SET \
            {self.DELETEFLG} = '{self.DELETEFLG_1}', \
            {self.UPDATEDATE} = '{str(today)}', \
            {self.UPDATEUSER} = '{dicTorihikisakiInfo[common.USER_ID]}' \
             WHERE {self.TORICD} = '{dicTorihikisakiInfo[self.TORICD]}'"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        return True

import sqlite3
import copy
import datetime

from typing import Final

from COMMON.Common import Common
from COMMON.M011Common import M011Common

common: Final[Common] = Common()
m011common: Final[M011Common] = M011Common()

class MUserDAO:
    
    def __init__(self) -> None:
        self.__dbname: Final[str] = './DB/MUser.db'
        
        self.TABLENAME: Final[str] = "MUser"
        
        self.SHAINCD: Final[str] = "shainCd"
        self.PASSWORD: Final[str] = "password"
        self.SHAINNM: Final[str] = "shainNm"
        self.KENGENFLG: Final[str] = "kengenFlg"
        self.DELETEFLG: Final[str] = "deleteFlg"
        self.CREATEDATE: Final[str] = "createDate"
        self.CREATEUSER: Final[str] = "createUser"
        self.UPDATEDATE: Final[str] = "updateDate"
        self.UPDATEUSER: Final[str] = "updateUser"
        
        self.OLD_PASSWORD: Final[str] = "oldPassword"
        self.NEW_PASSWORD: Final[str] = "newPassword"
        
        self.KENGENFLG_0: Final[str] = "0"
        self.KENGENFLG_1: Final[str] = "1"

        self.DELETEFLG_0: Final[str] = "0"
        self.DELETEFLG_1: Final[str] = "1"
        
        self.dic: Final[dict] = {
                    f"{self.SHAINCD}": common.BLANK,
                    f"{self.PASSWORD}": common.BLANK,
                    f"{self.SHAINNM}": common.BLANK,
                    f"{self.KENGENFLG}": common.BLANK,
                    f"{self.DELETEFLG}": common.BLANK,
                    f"{self.CREATEDATE}": common.BLANK,
                    f"{self.CREATEUSER}": common.BLANK,
                    f"{self.UPDATEDATE}": common.BLANK,
                    f"{self.UPDATEUSER}": common.BLANK
                   }
        
    def createMUserTable(self) -> None:
        today = datetime.datetime.now()
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()

        sql: str = f'CREATE TABLE {self.TABLENAME} ( \
                    {self.SHAINCD} STRING PRIMARY KEY, \
                    {self.PASSWORD} STRING, \
                    {self.SHAINNM} STRING, \
                    {self.KENGENFLG} STRING, \
                    {self.DELETEFLG} STRING, \
                    {self.CREATEDATE} STRING, \
                    {self.CREATEUSER} STRING, \
                    {self.UPDATEDATE} STRING, \
                    {self.UPDATEUSER} STRING\
                    )'

        cur.execute(sql)

        conn.commit()
        common.writeDaoLog(sql)
        
        sqlList: list = [
            f'INSERT INTO {self.TABLENAME} values("admin", "admin", "system", "{self.KENGENFLG_1}", "{self.DELETEFLG_0}", "{str(today)}", "system", "{common.BLANK}", "{common.BLANK}")',
            f'INSERT INTO {self.TABLENAME} values("admin1", "admin", "system", "{self.KENGENFLG_1}", "{self.DELETEFLG_0}", "{str(today)}", "system", "{common.BLANK}", "{common.BLANK}")',
            f'INSERT INTO {self.TABLENAME} values("admin2", "admin", "system", "{self.KENGENFLG_1}", "{self.DELETEFLG_0}", "{str(today)}", "system", "{common.BLANK}", "{common.BLANK}")'
            ]
        
        for sql in sqlList:
            cur.execute(sql)
            common.writeDaoLog(sql)
            
        conn.commit()
        
        conn.close()
        conn.close()
    
    def selectMUser(self) -> None:
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
        selectAll = []
        sql: str = f"SELECT * FROM {self.TABLENAME} WHERE {self.DELETEFLG} = '{self.DELETEFLG_0}'"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        
        for low in cur.fetchall():
            dic: dict = copy.copy(self.dic)
            for i in range(len(low)):
                dic[list(dic)[i]] = low[i]
            selectAll.append(dic)
            
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        return selectAll
    
    def selectOne(self, userId: str, password: str) -> list:
        selectOne: list = []
        sql: str = f"SELECT * FROM {self.TABLENAME} WHERE {self.SHAINCD} = '{userId}' AND {self.PASSWORD} = '{password}' AND {self.DELETEFLG} = '{self.DELETEFLG_0}'"
        
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
    
    def blSelectShainInfo(self, dicUserInfo: dict) -> bool:
        if dicUserInfo[self.PASSWORD] == common.BLANK:
            sql: str = f"SELECT COUNT(*) FROM {self.TABLENAME} WHERE {self.SHAINCD} = '{dicUserInfo[self.SHAINCD]}' AND {self.DELETEFLG} = '{self.DELETEFLG_0}'"
        else:
            sql: str = f"SELECT COUNT(*) FROM {self.TABLENAME} WHERE {self.SHAINCD} = '{dicUserInfo[self.SHAINCD]}' AND {self.PASSWORD} = '{dicUserInfo[self.PASSWORD]}' AND {self.DELETEFLG} = '{self.DELETEFLG_0}'"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        
        kensu = cur.fetchall()[0][0]
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        return kensu == 1

    def blKengenInfo(self, userId: str) -> bool:
        sql: str = f"SELECT COUNT(*) FROM {self.TABLENAME} WHERE {self.SHAINCD} = '{userId}' AND {self.KENGENFLG} = '{self.KENGENFLG_1}' AND {self.DELETEFLG} = '{self.DELETEFLG_0}'"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        
        kensu = cur.fetchall()[0][0]

        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        return kensu == 1
    
    def updateNewPassword(self, dicUserInfo: dict) -> bool:
        today = datetime.datetime.now()
        
        sql: str = f"UPDATE {self.TABLENAME} SET {self.PASSWORD} = '{dicUserInfo[m011common.NEW_PASSWORD[common.ID]]}', {self.UPDATEDATE} = '{str(today)}', {self.UPDATEUSER} = '{dicUserInfo[self.SHAINCD]}' WHERE {self.SHAINCD} = '{dicUserInfo[self.SHAINCD]}' AND {self.PASSWORD} = '{dicUserInfo[m011common.OLD_PASSWORD[common.ID]]}' AND {self.DELETEFLG} = '{self.DELETEFLG_0}'"
        
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
        
        sql: str = f"UPDATE {self.TABLENAME} SET {self.DELETEFLG} = 0, {self.UPDATEDATE} = '{str(today)}', {self.UPDATEUSER} = '{common.SYSTEM}'"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        return True
    
    def insertUserInfo(self, dicUserInfo: dict) -> bool:
        today = datetime.datetime.now()
        
        sql: str = f"INSERT INTO {self.TABLENAME} \
        ({self.SHAINCD}, {self.PASSWORD}, {self.SHAINNM}, {self.KENGENFLG}, {self.DELETEFLG}, {self.CREATEDATE}, {self.CREATEUSER}, {self.UPDATEDATE}, {self.UPDATEUSER}) \
        VALUES ('{dicUserInfo[self.SHAINCD]}', '{dicUserInfo[self.PASSWORD]}', '{dicUserInfo[self.SHAINNM]}', '{dicUserInfo[self.KENGENFLG]}', '{self.DELETEFLG_0}', '{str(today)}', '{dicUserInfo[self.SHAINCD]}', '{common.BLANK}', '{common.BLANK}')"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        return True

    def deleteUserInfo(self, shainCd: str) -> bool:
        today = datetime.datetime.now()
        
        sql: str = f"UPDATE {self.TABLENAME} SET \
            {self.DELETEFLG} = '{self.DELETEFLG_1}', \
            {self.UPDATEDATE} = '{str(today)}', \
            {self.UPDATEUSER} = '{shainCd}' \
             WHERE {self.SHAINCD} = '{shainCd}'"
        
        conn = sqlite3.connect(self.__dbname)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        
        cur.close()
        conn.close()
        
        common.writeDaoLog(sql)
        
        return True
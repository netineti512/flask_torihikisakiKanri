import datetime
import csv

from flask import Flask,render_template, request, session, flash, Blueprint
from typing import Final

from COMMON.Common import Common
from COMMON.Message import Message
from COMMON.M010Common import M010Common
from COMMON.M011Common import M011Common
from COMMON.M012Common import M012Common
from COMMON.T010Common import T010Common
from COMMON.T011Common import T011Common
from DAO.MUserDAO import MUserDAO
from DAO.TTorihikiDAO import TTorihikiDAO

app = Flask(__name__, template_folder="templates")
app.secret_key = 'user'

common: Final[Common] = Common()
msg: Final[Message] = Message()

m010common: Final[M010Common] = M010Common()
m011common: Final[M011Common] = M011Common()
m012common: Final[M012Common] = M012Common()
t010common: Final[T010Common] = T010Common()
t011common: Final[T011Common] = T011Common()

#初期表示時
@app.route(common.SLASH)
def init():
    session[common.GMN_ID] = m010common.GMN_ID
    session[common.USER_ID] = common.BLANK
    
    return render_template(m010common.URL_HTML)

#「戻る」ボタン押下の処理
@app.route(common.BACK_BTN, methods=[common.POST])
def back():
    gmnId: Final[str] = session[common.GMN_ID]
    
    if gmnId == m011common.GMN_ID:
        backBtnFlg: Final[str] = request.form[m011common.BACK_BTN]
        
        if backBtnFlg == common.STR_TRUE:
            session[common.GMN_ID] = m010common.GMN_ID
            session[common.USER_ID] = common.BLANK
            return render_template(m010common.URL_HTML)
        else:
            hiddenShainCd: Final[str] = request.form[m011common.HIDDEN_SHAIN_CD]
            return render_template(m011common.URL_HTML, M011ShainCd=hiddenShainCd)
        
    if gmnId == t010common.GMN_ID:
        backBtnFlg: Final[str] = request.form[t010common.BACK_BTN]
        
        if backBtnFlg == common.STR_TRUE:
            session[common.GMN_ID] = m010common.GMN_ID
            session[common.USER_ID] = common.BLANK
            return render_template(m010common.URL_HTML)
        else:
            return render_template(t010common.URL_HTML)
        
    if gmnId == t011common.GMN_ID:
        backBtnFlg: Final[str] = request.form[t011common.BACK_BTN]
        
        if backBtnFlg == common.STR_TRUE:
            session[common.GMN_ID] = t010common.GMN_ID
            return render_template(t010common.URL_HTML)
        else:
            return render_template(t011common.URL_HTML, dictTorihikisakiInfo = session[common.DICT_TORIHIKISAKI_INFO])    
        
    if gmnId == m012common.GMN_ID:
        backBtnFlg: Final[str] = request.form[m012common.BACK_BTN]
        
        if backBtnFlg == common.STR_TRUE:            
            session[common.GMN_ID] = t010common.GMN_ID
            return render_template(t010common.URL_HTML)
        else:
            return render_template(m012common.URL_HTML)

####### 「M010 ログイン画面」#######################################
# M010
# ログイン画面
# 「ログイン」ボタン押下の処理
@app.route(common.M010_BTN_LOGIN, methods=[common.POST])
def moveT010():
    shainCd: Final[str] = request.form[m010common.SHAIN_CD[common.ID]]
    password: Final[str] = request.form[m010common.PASSWORD[common.ID]]
    
    blErrorFlg: bool = False

    if common.checkBLANK(shainCd):
        blErrorFlg: bool = True
        flash(msg.msg001(m010common.SHAIN_CD[common.NAME]), common.FAILED)
    if common.checkBLANK(password):
        blErrorFlg: bool = True
        flash(msg.msg001(m010common.PASSWORD[common.NAME]), common.FAILED)
        
    if blErrorFlg:
        return render_template(m010common.URL_HTML, shainCd=shainCd)
    
    mUserDao: Final[MUserDAO] = MUserDAO()
        
    dic: Final[dict] = {
        mUserDao.SHAINCD: shainCd,
        mUserDao.PASSWORD: password
    }
    
    if mUserDao.blSelectShainInfo(dic):
        session[common.GMN_ID] = t010common.GMN_ID
        session[common.USER_ID] = shainCd
        
        return render_template(t010common.URL_HTML, height=str(common.TABLE_HEIGHT))
    else:
        flash(msg.ERROR_MSG1, common.FAILED)
        return render_template(m010common.URL_HTML, shainCd=shainCd)

#「パスワード変更はこちら」リンク押下の処理
@app.route(common.M010_LINK_PASSWORD_CHANGE, methods=[common.GET])
def moveM011():
    session[common.GMN_ID] = m011common.GMN_ID
    
    return render_template(m011common.URL_HTML, shainCd=common.BLANK)

####### 「M011 パスワード変更画面」####################################### 
# M011
# パスワード変更画面
#「パスワード変更」ボタン押下の処理
@app.route(common.M011_BTN_PASSWORD_CHANGE, methods=[common.POST])
def passwordChange():
    shainCd: Final[str] = request.form[m011common.SHAIN_CD[common.ID]]
    oldPassword: Final[str] = request.form[m011common.OLD_PASSWORD[common.ID]]
    newPassword: Final[str] = request.form[m011common.NEW_PASSWORD[common.ID]]
    
    passwordChangeFlg: Final[str] = request.form[m011common.PASSWORD_CHANGE_BTN]
    
    if passwordChangeFlg == common.STR_FALSE:
        return render_template(m011common.URL_HTML, M011ShainCd=shainCd)
    
    blErrorFlg: bool = False
    
    if common.checkBLANK(shainCd):
        blErrorFlg: bool = True
        flash(msg.msg001(m011common.SHAIN_CD[common.NAME]), common.FAILED)
    if common.checkBLANK(oldPassword):
        blErrorFlg: bool = True
        flash(msg.msg001(m011common.OLD_PASSWORD[common.NAME]), common.FAILED)
    if common.checkBLANK(newPassword):
        blErrorFlg: bool = True
        flash(msg.msg001(m011common.NEW_PASSWORD[common.NAME]), common.FAILED)
    
    if blErrorFlg:
        return render_template(m011common.URL_HTML, shainCd=shainCd)
    
    if common.checkEqual(oldPassword, newPassword):
        blErrorFlg: bool = True
        flash(msg.msg002(m011common.OLD_PASSWORD[common.NAME], m011common.NEW_PASSWORD[common.NAME]), common.FAILED)
    
    if common.checkStrSize(newPassword, common.MIN_SIZE, common.MAX_SIZE):
        blErrorFlg: bool = True
        flash(msg.msg003(m011common.NEW_PASSWORD[common.NAME], common.MIN_SIZE, common.MAX_SIZE), common.FAILED)
        
    if common.checkSymbol(newPassword):
        blErrorFlg: bool = True
        flash(msg.msg004(m011common.NEW_PASSWORD[common.NAME]), common.FAILED)
    
    if blErrorFlg:
        return render_template(m011common.URL_HTML, shainCd=shainCd)
        
    mUserDao: Final[MUserDAO] = MUserDAO()
    
    dicOldUserInfo: Final[dict] = {
        mUserDao.SHAINCD: shainCd,
        mUserDao.PASSWORD: oldPassword
    }
    
    if mUserDao.blSelectShainInfo(dicOldUserInfo):
        dicNewUserInfo: Final[dict] = {
            mUserDao.SHAINCD: shainCd,
            m011common.OLD_PASSWORD[common.ID]: oldPassword,
            m011common.NEW_PASSWORD[common.ID]: newPassword
        }
        
        if mUserDao.updateNewPassword(dicNewUserInfo):
            flash(msg.SUCCESS_MSG1, common.SUCCESS)
            session[common.GMN_ID] = m010common.GMN_ID
            return render_template(m010common.URL_HTML)
    
    flash(msg.ERROR_MSG2, common.FAILED)
    return render_template(m011common.URL_HTML, shainCd=shainCd)

####### 「T010 取引先管理画面」####################################### 
# T010
# 取引先管理画面
# 「検索」ボタン押下時の処理
@app.route(common.T010_BTN_SEARCH, methods=[common.POST])
def searchTorihikisakiInfo():
    session[common.GMN_ID] = t010common.GMN_ID
    
    toriCd: Final[str] = request.form[t010common.TORI_CD]
    toriNm: Final[str] = request.form[t010common.TORI_NM]
    
    tTorihikiDao: Final[TTorihikiDAO] = TTorihikiDAO()
    
    if toriCd == common.BLANK and toriNm == common.BLANK:
        datas: Final[list] = tTorihikiDao.selectAll()
    elif toriCd != common.BLANK or toriNm != common.BLANK:
        dicTorihikisakiInfo: dict = {
            tTorihikiDao.TORICD: toriCd,
            tTorihikiDao.TORINM: toriNm
        }
        datas: Final[list] = tTorihikiDao.selectTarget(dicTorihikisakiInfo)
    
    lstToriCd: list = []
    lstToriNm: list = []
    lstToriKbn: list = []
    lstNaigaiKbn: list = []
    lstToriSstartDate: list = []
    lstToriEndDate: list = []
    
    for data in datas:
        if len(str(data[tTorihikiDao.TORICD])) == common.INT_ONE:
            lstToriCd.append("000" + str(data[tTorihikiDao.TORICD]))
        elif len(str(data[tTorihikiDao.TORICD])) == common.INT_TWO:
            lstToriCd.append("00" + str(data[tTorihikiDao.TORICD]))
        elif len(str(data[tTorihikiDao.TORICD])) == common.INT_THREE:
            lstToriCd.append("0" + str(data[tTorihikiDao.TORICD]))
        elif len(str(data[tTorihikiDao.TORICD])) == common.INT_FOUR:
            lstToriCd.append(str(data[tTorihikiDao.TORICD]))
            
        if len(str(data[tTorihikiDao.TORITEL])) in [common.INT_NINE, common.INT_TEN]:
            data[tTorihikiDao.TORITEL] = "0" + str(data[tTorihikiDao.TORITEL])
        
        if len(str(data[tTorihikiDao.TANTOBUSHOTEL])) in [common.INT_NINE, common.INT_TEN]:
            data[tTorihikiDao.TANTOBUSHOTEL] = "0" + str(data[tTorihikiDao.TANTOBUSHOTEL])
            
        lstToriNm.append(data[tTorihikiDao.TORINM])
        lstToriKbn.append(data[tTorihikiDao.TORIKBN])
        lstNaigaiKbn.append(data[tTorihikiDao.NAIGAIKBN])
        lstToriSstartDate.append(data[tTorihikiDao.TORISTARTDATE])
        lstToriEndDate.append(data[tTorihikiDao.TORIENDDATE])
    
    session[common.DATAS] = datas
        
    height: Final[str] = str(common.TABLE_HEIGHT + len(lstToriCd) * 36)
    
    torihikisakiInfo = zip(lstToriCd, lstToriNm, lstToriKbn, lstNaigaiKbn, lstToriSstartDate, lstToriEndDate)
    
    return render_template(t010common.URL_HTML, data = torihikisakiInfo, T010ToriCd=toriCd, T010ToriNm=toriNm, height=height)

# T010
# 取引先管理画面
#「管理者ページ」ボタン押下の処理
@app.route(common.T010_BTN_KANRI, methods=[common.POST])
def moveM012():
    shainCd: Final[str] = session[common.USER_ID]
    
    mUserDao: Final[MUserDAO] = MUserDAO()
    
    if mUserDao.blKengenInfo(shainCd):
        session[common.GMN_ID] = m012common.GMN_ID
        return render_template(m012common.URL_HTML, M012ShainCd=shainCd)

    flash(msg.ERROR_MSG3, common.FAILED)
    return render_template(t010common.URL_HTML)

# T010
# 取引先管理画面
#「編集」ボタン押下の処理
@app.route(common.T010_BTN_EDIT, methods=[common.POST])
def editTorihikisakiInfo():
    selectedToriCd: Final[str] = request.form[t010common.SELECTED_ROW]
    
    if selectedToriCd == common.BLANK:
        flash(msg.ERROR_MSG4, common.FAILED)
        return render_template(t010common.URL_HTML)
    
    tTorihikiDao: Final[TTorihikiDAO] = TTorihikiDAO()
    
    lstTorihikisakiInfo: Final[list] = tTorihikiDao.selectOne(selectedToriCd)
    
    if not lstTorihikisakiInfo or len(lstTorihikisakiInfo) == common.INT_ZERO:
        flash(msg.ERROR_MSG5, common.FAILED)
        return render_template(t010common.URL_HTML)
    
    dictTorihikisakiInfo: Final[dict] = lstTorihikisakiInfo[common.INT_ZERO]
    
    if dictTorihikisakiInfo[tTorihikiDao.TORICD] == common.INT_ONE:
        dictTorihikisakiInfo[tTorihikiDao.TORICD] = "000" + str(dictTorihikisakiInfo[tTorihikiDao.TORICD])
    elif dictTorihikisakiInfo[tTorihikiDao.TORICD] == common.INT_TWO:
        dictTorihikisakiInfo[tTorihikiDao.TORICD] = "00" + str(dictTorihikisakiInfo[tTorihikiDao.TORICD])
    elif dictTorihikisakiInfo[tTorihikiDao.TORICD] == common.INT_THREE:
        dictTorihikisakiInfo[tTorihikiDao.TORICD] = "0" + str(dictTorihikisakiInfo[tTorihikiDao.TORICD])

    if len(str(dictTorihikisakiInfo[tTorihikiDao.TORITEL])) in [common.INT_NINE, common.INT_TEN]:
        dictTorihikisakiInfo[tTorihikiDao.TORITEL] = "0" + str(dictTorihikisakiInfo[tTorihikiDao.TORITEL])
    
    if len(str(dictTorihikisakiInfo[tTorihikiDao.TANTOBUSHOTEL])) in [common.INT_NINE, common.INT_TEN]:
        dictTorihikisakiInfo[tTorihikiDao.TANTOBUSHOTEL] = "0" + str(dictTorihikisakiInfo[tTorihikiDao.TANTOBUSHOTEL])
    
    session[common.GMN_ID] = t011common.GMN_ID
    session[common.DICT_TORIHIKISAKI_INFO] = dictTorihikisakiInfo
    return render_template(t011common.URL_HTML, dictTorihikisakiInfo = dictTorihikisakiInfo, T011SelectedRow=selectedToriCd)

# T010
# 取引先管理画面
#「取込」ボタン押下の処理
@app.route(common.T010_BTN_IMPORT, methods=[common.POST])
def importTorihikisakiInfo():
    hiddenImportFile: Final[str] = request.form[t010common.HIDDEN_IMPORT_FILE]

    flash(msg.SUCCESS_MSG6, common.SUCCESS)
    return render_template(t010common.URL_HTML)

# T010
# 取引先管理画面
#「出力」ボタン押下の処理
@app.route(common.T010_BTN_EXPORT, methods=[common.POST])
def exportTorihikisakiInfo():
    today = datetime.datetime.now()
    
    path = "./app/templates/doc/"
    fileName = str(today) + "_TTorihiki.csv"
    
    datas = session[common.DATAS]
    tTorihikiDao: Final[TTorihikiDAO] = TTorihikiDAO()
    header = list(tTorihikiDao.dic.keys())
    csvDataList = [header]
    
    for data in datas:
        csvDataList.append(list(data.values()))
    
    with open(path + fileName, "w", newline="") as f:
        w = csv.writer(f, delimiter=",")
        for data_line in csvDataList:
                w.writerow(data_line)
    
    flash(msg.SUCCESS_MSG7, common.SUCCESS)
    return render_template(t010common.URL_HTML, fileName=fileName)

####### 「T011 取引先編集画面」####################################### 
# T011
# 取引先編集画面
# 「取引先情報更新」ボタン押下時の処理
@app.route(common.T011_BTN_UPDATE, methods=[common.POST])
def updateTorihikisakiInfo():
    updateBtnFlg: Final[bool] = request.form[t011common.UPDATE_BTN]

    dictTorihikisakiInfo: dict = session[common.DICT_TORIHIKISAKI_INFO]

    if updateBtnFlg == common.STR_TRUE:
        toriCd: Final[str] = request.form[t011common.TORI_CD[common.ID]]
        toriNm: Final[str] = request.form[t011common.TORI_NM[common.ID]]
        toriKana: Final[str] = request.form[t011common.TORI_KANA[common.ID]]
        toriKbn: Final[str] = request.form[t011common.TORI_KBN[common.ID]]
        toriTel: Final[str] = request.form[t011common.TORI_TEL[common.ID]]
        toriShohin: Final[str] = request.form[t011common.TORI_SHOHIN[common.ID]]
        naigaiKbn: Final[str] = request.form[t011common.NAIGAI_KBN[common.ID]]
        zipCode: Final[str] = request.form[t011common.ZIP_CODE[common.ID]]
        add1: Final[str] = request.form[t011common.ADD1[common.ID]]
        add2: Final[str] = request.form[t011common.ADD2[common.ID]]
        tantobusho: Final[str] = request.form[t011common.TANTOBUSHO[common.ID]]
        tantosha: Final[str] = request.form[t011common.TANTOSHA[common.ID]]
        tantoBushoTel: Final[str] = request.form[t011common.TANTOBUSHO_TEL[common.ID]]
        payJoken: Final[str] = request.form[t011common.PAY_JOKEN[common.ID]]
        depoJoken: Final[str] = request.form[t011common.DEPO_JOKEN[common.ID]]
        toriStartDate: Final[str] = request.form[t011common.TORI_START_DATE[common.ID]]
        toriEndDate: Final[str] = request.form[t011common.TORI_END_DATE[common.ID]]
        memo: Final[str] = request.form[t011common.MEMO[common.ID]]
    
        tTorihikiDao: Final[TTorihikiDAO] = TTorihikiDAO()
        
        dictTorihikisakiInfo[tTorihikiDao.TORICD] = toriCd
        dictTorihikisakiInfo[tTorihikiDao.TORINM] = toriNm
        dictTorihikisakiInfo[tTorihikiDao.TORIKANA] = toriKana
        dictTorihikisakiInfo[tTorihikiDao.TORIKBN] = toriKbn
        dictTorihikisakiInfo[tTorihikiDao.TORITEL] = toriTel
        dictTorihikisakiInfo[tTorihikiDao.TORISHOHIN] = toriShohin
        dictTorihikisakiInfo[tTorihikiDao.NAIGAIKBN] = naigaiKbn
        dictTorihikisakiInfo[tTorihikiDao.ZIPCODE] = zipCode
        dictTorihikisakiInfo[tTorihikiDao.ADD1] = add1
        dictTorihikisakiInfo[tTorihikiDao.ADD2] = add2
        dictTorihikisakiInfo[tTorihikiDao.TANTOBUSHO] = tantobusho
        dictTorihikisakiInfo[tTorihikiDao.TANTOSHA] = tantosha
        dictTorihikisakiInfo[tTorihikiDao.TANTOBUSHOTEL] = tantoBushoTel
        dictTorihikisakiInfo[tTorihikiDao.PAYJOKEN] = payJoken
        dictTorihikisakiInfo[tTorihikiDao.DEPOJOKEN] = depoJoken
        dictTorihikisakiInfo[tTorihikiDao.TORISTARTDATE] = toriStartDate
        dictTorihikisakiInfo[tTorihikiDao.TORIENDDATE] = toriEndDate
        dictTorihikisakiInfo[tTorihikiDao.MEMO] = memo
        
        dictTorihikisakiInfo[common.USER_ID] = session[common.USER_ID]
        
        if tTorihikiDao.blUpdateTorihikisakiInfo(dictTorihikisakiInfo):
            session[common.GMN_ID] = t010common.GMN_ID
            flash(msg.SUCCESS_MSG3, common.SUCCESS)
            return render_template(t010common.URL_HTML)
        else:
            flash(msg.ERROR_MSG7, common.FAILED)
            return render_template(t011common.URL_HTML)            
    else :
        return render_template(t011common.URL_HTML, dictTorihikisakiInfo = dictTorihikisakiInfo)

# T011
# 取引先編集画面
# 「取引先情報削除」ボタン押下時の処理
@app.route(common.T011_BTN_DELETE, methods=[common.POST])
def deleteTorihikisakiInfo():
    deleteBtnFlg: Final[str] = request.form[t011common.DELETE_BTN]
    
    if deleteBtnFlg == common.STR_FALSE:
        return render_template(t011common.URL_HTML, dictTorihikisakiInfo = session[common.DICT_TORIHIKISAKI_INFO])
    
    hiddenToriCd: Final[str] = request.form[t011common.HIDDEN_TORI_CD]
    
    shainCd: Final[str] = session[common.USER_ID]
    
    mUserDao: Final[MUserDAO] = MUserDAO()
    
    if not mUserDao.blKengenInfo(shainCd):
        flash(msg.ERROR_MSG6, common.FAILED)
        return render_template(t011common.URL_HTML, dictTorihikisakiInfo = session[common.DICT_TORIHIKISAKI_INFO])
    
    tTorihikiDao: Final[TTorihikiDAO] = TTorihikiDAO()
    
    dicTorihikisakiInfo: Final[str] = {
        common.USER_ID:shainCd,
        tTorihikiDao.TORICD:hiddenToriCd
    }
    
    if tTorihikiDao.blDeleteTorihikisakiInfo(dicTorihikisakiInfo):
        session[common.GMN_ID] = t010common.GMN_ID
        flash(msg.SUCCESS_MSG4, common.SUCCESS)
        return render_template(t010common.URL_HTML)
    else:
        flash(msg.ERROR_MSG8, common.FAILED)
        return render_template(t011common.URL_HTML, dictTorihikisakiInfo = session[common.DICT_TORIHIKISAKI_INFO])

####### 「M012 ユーザー管理画面」####################################### 
# M012
# ユーザー管理画面
# 「ユーザー登録」ボタン押下時の処理
@app.route(common.M012_BTN_USER_CREATE, methods=[common.POST])
def createUserInfo():
    shainCd: Final[str] = request.form[m012common.SHAIN_CD[common.ID]]
    shainNm: Final[str] = request.form[m012common.SHAIN_NM[common.ID]]

    
    insertBtnFlg: Final[str] = request.form[m012common.INSERT_BTN]
    
    if insertBtnFlg == common.STR_FALSE:
        return render_template(m012common.URL_HTML, sessionShainCd=shainCd, sessionShainNm=shainNm)
    
    password: Final[str] = request.form[m012common.PASSWORD[common.ID]]
    kengen: Final[str] = request.form[m012common.KENGEN_FLG[common.ID]]
    
    blErrorFlg: bool = False
    
    if common.checkBLANK(shainCd):
        blErrorFlg: bool = True
        flash(msg.msg001(m012common.SHAIN_CD[common.NAME]), common.FAILED)
    if common.checkBLANK(shainNm):
        blErrorFlg: bool = True
        flash(msg.msg001(m012common.SHAIN_NM[common.NAME]), common.FAILED)
    if common.checkBLANK(password):
        blErrorFlg: bool = True
        flash(msg.msg001(m012common.PASSWORD[common.NAME]), common.FAILED)
    
    if blErrorFlg:
        return render_template(m012common.URL_HTML)

    if common.checkStrSize(shainCd, common.MIN_SIZE, common.MAX_SIZE):
        blErrorFlg: bool = True
        flash(msg.msg003(m012common.SHAIN_CD[common.NAME], common.MIN_SIZE, common.MAX_SIZE), common.FAILED)
    
    if common.checkStrSize(password, common.MIN_SIZE, common.MAX_SIZE):
        blErrorFlg: bool = True
        flash(msg.msg003(m012common.PASSWORD[common.NAME], common.MIN_SIZE, common.MAX_SIZE), common.FAILED)

    if common.checkSymbol(shainCd):
        blErrorFlg: bool = True
        flash(msg.msg004(m012common.SHAIN_CD[common.NAME]), common.FAILED)
       
    if common.checkSymbol(password):
        blErrorFlg: bool = True
        flash(msg.msg004(m012common.PASSWORD[common.NAME]), common.FAILED)
    
    if blErrorFlg:
        return render_template(m012common.URL_HTML)
    
    mUserDao: Final[MUserDAO] = MUserDAO()
    
    dicCurrentUserInfo: Final[dict] = {
        mUserDao.SHAINCD: shainCd,
        mUserDao.PASSWORD: common.BLANK}
    
    if not mUserDao.blSelectShainInfo(dicCurrentUserInfo):
        dicNewUserInfo: Final[dict] = {
            mUserDao.SHAINCD: shainCd,
            mUserDao.SHAINNM: shainNm,
            mUserDao.PASSWORD: password,
            mUserDao.KENGENFLG: kengen}
        
        if mUserDao.insertUserInfo(dicNewUserInfo):
            flash(msg.SUCCESS_MSG2, common.SUCCESS)
            session[common.GMN_ID] = t010common.GMN_ID
            return render_template(t010common.URL_HTML)
        
    flash(msg.msg005(m012common.SHAIN_CD[common.NAME]), common.FAILED)
    session[common.GMN_ID] = m012common.GMN_ID
    return render_template(m012common.URL_HTML)

# M012
# ユーザー管理画面
# 「ユーザー削除」ボタン押下時の処理
@app.route(common.M012_BTN_USER_DELETE, methods=[common.POST])
def deleteUserInfo():
    deleteBtnFlg: Final[str] = request.form[m012common.DELETE_BTN]

    if deleteBtnFlg == common.STR_FALSE:
        return render_template(m012common.URL_HTML)
    
    hiddenShainCd: Final[str] = request.form[m012common.HIDDEN_SHAIN_CD]
    
    mUserDao: Final[MUserDAO] = MUserDAO()
    
    if mUserDao.deleteUserInfo(hiddenShainCd):
        session[common.GMN_ID] = m010common.GMN_ID
        flash(msg.SUCCESS_MSG5, common.SUCCESS)
        return render_template(m010common.URL_HTML)
    else:
        flash(msg.ERROR_MSG9, common.FAILED)
        return render_template(m012common.URL_HTML)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
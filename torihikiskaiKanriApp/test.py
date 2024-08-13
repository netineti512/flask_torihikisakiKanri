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

common: Final[Common] = Common()
msg: Final[Message] = Message()

m010common: Final[M010Common] = M010Common()
m011common: Final[M011Common] = M011Common()
m012common: Final[M012Common] = M012Common()
t010common: Final[T010Common] = T010Common()
t011common: Final[T011Common] = T011Common()

muserDao: Final[MUserDAO] = MUserDAO()
ttorihikiDao: Final[TTorihikiDAO] = TTorihikiDAO()

ttorihikiDao.updateDeleteFlg()

for i in ttorihikiDao.selectAll():
    print(i)
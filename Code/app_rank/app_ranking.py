import os,sys
import datetime as dt
from os.path import dirname,abspath
cd_dir = dirname(dirname(abspath(__file__)))
sys.path.append(dirname(cd_dir)+"/Function")
sys.path.append(dirname(abspath(__file__))+'\\'+abspath(__file__).split('\\')[-1].replace('.py',''))
import pandas as pd,numpy as np,japandas as jpd
from pandas.tseries import offsets
tse = jpd.TSEHolidayCalendar()
cday = pd.offsets.CDay(calendar=tse)

# 当日をターゲットにしたfunction群
def app_ranking(e_day):
    try:
        # e_day = dt.date.today() # + offsets.CBMonthEnd()
        s_day = pd.to_datetime(e_day - offsets.CBMonthEnd()*7).date()
        # ranking更新
        from appRank_ins import appRank_ins
        appRank_ins()
        # ranking更新
        from appRank_out import appRank_out
        appRank_out(s_day,e_day)
        # rankingから推定される売上を吐き出し
        from app_sales_estimate import monthly_sales,monthly_topline
        monthly_sales(s_day,e_day)
        monthly_topline(s_day,e_day)
        return True
    except:
        return False

if __name__ == '__main__':
    t_day = dt.date.today()
    # t_day = t_day + dt.timedelta(days=-1)
    from executer import exe,task_result
    if exe(t_day):
        flg = app_ranking(t_day)
        task_name = abspath(__file__).split('\\')[-1].replace('.py','')
        task_result(task_name,flg)

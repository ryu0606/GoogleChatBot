import datetime

#例11/23(月)のようにデータを返す
class NowTime :
    def getNowTime():
        dt_now = datetime.datetime.now()
        dt_now_week:str
        #weekdayメソッドでは、月曜日を 0、日曜日を 6 として、曜日を整数で返す
        #datetime.datetime(年,月,日)
        dt = datetime.datetime(dt_now.year,dt_now.month,dt_now.day)
        dtnt = dt.weekday()
        if(dtnt == 0) : dt_now_week = "月"
        elif(dtnt == 1) : dt_now_week = '火'
        elif(dtnt == 2) : dt_now_week = "水"
        elif(dtnt == 3) : dt_now_week = "木"
        elif(dtnt == 4) : dt_now_week = "金"
        elif(dtnt == 5) : dt_now_week = "土"
        elif(dtnt == 6) : dt_now_week = "日"

        return dt_now.strftime('%m/%d') + '(' + dt_now_week + ')'
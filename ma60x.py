import appconfig
import mysql.connector  
from mysql.connector import Error

# 当天当前价格计算MAxx的数值
def MAxx(stockcode,maxx,currprice):  
    # MySQL数据库连接参数  
    db_config = {  
        'host': appconfig.host,  
        'database': appconfig.database,  
        'user': appconfig.username,  
        'password': appconfig.password  
    }  
    connection = None  
    # MA xx 
    maxx = maxx - 1
    try:  
        # 连接数据库  
        connection = mysql.connector.connect(**db_config)  
        if connection.is_connected():  
            db_Info = connection.get_server_info()  
            # print(f"Connected to MySQL Server version {db_Info}")  
            cursor = connection.cursor()  
            sql = f"""  
                SELECT ROUND(AVG(a.cl), 2) AS avgclose  
                FROM (  
                    SELECT {currprice} AS cl, CURDATE() AS da  
                    UNION  
                    SELECT s.cl, s.da  
                    FROM (  
                        SELECT st.close AS cl, st.trade_date AS da  
                        FROM stock_data st  
                        WHERE st.ts_code = '{stockcode}'  
                        ORDER BY da DESC  
                        LIMIT 1, {maxx} -- MA60，这里直接使用maxx的值  
                    ) s  
                ) a  
            """  
            cursor.execute(sql)  
            result = cursor.fetchone()  
            # if result:  
            #     print(f"Average Close: {result[0]}")  
            # else:  
            #     print("No data found.")
            return result[0]
    except Error as e:  
        print(f"Error while connecting to MySQL {e}")  
    finally:  
        if connection.is_connected():  
            cursor.close()  
            connection.close()  
            # print("MySQL connection is closed")  

# 当天当前价格计算MAxx的数值
def YMAxx(stockcode,maxx):  
    # MySQL数据库连接参数  
    db_config = {  
        'host': appconfig.host,  
        'database': appconfig.database,  
        'user': appconfig.username,  
        'password': appconfig.password  
    }  
    connection = None  
    try:  
        # 连接数据库  
        connection = mysql.connector.connect(**db_config)  
        if connection.is_connected():  
            db_Info = connection.get_server_info()  
            # print(f"Connected to MySQL Server version {db_Info}")  
            cursor = connection.cursor()  
            sql = f"""  
                SELECT ROUND(AVG(a.cl), 2) AS avgclose  
                FROM (  
                    SELECT s.cl, s.da  
                    FROM (  
                        SELECT st.close AS cl, st.trade_date AS da  
                        FROM stock_data st  
                        WHERE st.ts_code = '{stockcode}'  
                        ORDER BY da DESC  
                        LIMIT 1, {maxx} -- MA60，这里直接使用maxx的值  
                    ) s  
                ) a  
            """  
            cursor.execute(sql)  
            result = cursor.fetchone()  
            # if result:  
            #     print(f"Average Close: {result[0]}")  
            # else:  
            #     print("No data found.")
            return result[0]
    except Error as e:  
        print(f"Error while connecting to MySQL {e}")  
    finally:  
        if connection.is_connected():  
            cursor.close()  
            connection.close()  
            # print("MySQL connection is closed") 

def MAsx(stockcode,maxx,currprice):  
    mav = MAxx(stockcode,maxx,currprice) - YMAxx(stockcode,maxx) 
    if mav > 0:
        return "MA%d↑%.2f" %(maxx,mav)
    elif mav == 0:
        return "MA%d=%.2f" %(maxx,mav) 
    elif mav < 0:
        return "MA%d↓%.2f" %(maxx,mav)

# print( MAxx('300531.SZ',60,14.61) )
# print( YMAxx('300531.SZ',60) )

print( MAsx('300531.SZ',60,11.35) )

# MAxx 今天当前MA价格
# select ROUND(AVG(a.cl),2) avgclose from (
# -- 当前价格写入
# select  12.18 as cl ,curdate() as da
# union
# select s.cl,s.da from (
# SELECT st.`close` as cl,st.trade_date as da
# FROM `stock_data` st
# where st.ts_code = '300531.SZ'
# order by  da desc
# limit 0,60 -- MA60 今天0
# ) s
# ) a

# 昨日MAxx价格
# select ROUND(AVG(a.cl),2) avgclose from (
# -- 当前价格写入
# select  12.18 as cl ,curdate() as da
# union
# select s.cl,s.da from (
# SELECT st.`close` as cl,st.trade_date as da
# FROM `stock_data` st
# where st.ts_code = '300531.SZ'
# order by  da desc
# limit 1,60 -- MA60 昨日1开头
# ) s
# ) a
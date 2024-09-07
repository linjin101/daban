import appconfig
# 导入tushare
import tushare as ts
from datetime import datetime, timedelta  
from sqlalchemy import create_engine  

# SELECT st.trade_date ,count(1)
# FROM `stock_data` st
# group by st.trade_date

def stockListPrice(yesterday):
    # 确定时间
    today = yesterday
    
    # 检查今天是否是周六（weekday() 返回 5）或周日（weekday() 返回 6）  
    if today.weekday() >= 5:  
        # 如果是周六或周日，计算上周五的日期  
        # 上周五是今天减去 (今天是周几的索引 - 4)，因为weekday()返回的是0（周一）到6（周日）  
        last_friday = today - timedelta(days=today.weekday() - 4)  
        # 格式化日期为 'YYYYMMDD'  
        formatted_date = last_friday.strftime('%Y%m%d')  
    else:  
        # 如果不是周六或周日，就输出当前日期  
        formatted_date = today.strftime('%Y%m%d')  
    
    # 输出结果  
    print(formatted_date)

    # 初始化pro接口
    pro = ts.pro_api('16fa068f73952f45f9e9c45ed0cd13d0f0f5aabc1112c4ac9ab956ec')

    # ts.set_token('16fa068f73952f45f9e9c45ed0cd13d0f0f5aabc1112c4ac9ab956ec')

    # #sina数据
    # df = ts.realtime_list(src='sina')
    # print(df)

    # 拉取数据
    df = pro.daily(**{
        "ts_code": "",
        "trade_date": formatted_date,
        "start_date": "",
        "end_date": "",
        "offset": "",
        "limit": ""
    }, fields=[
        "ts_code",
        "trade_date",
        "open",
        "high",
        "low",
        "close",
        "pre_close",
        "change",
        "pct_chg",
        "vol",
        "amount"
    ])

    print(df)

    # # 将trade_date列转换为日期类型（可选，但推荐）  
    # df['trade_date'] = df.to_datetime(df['trade_date'], format='%Y%m%d').dt.date  

    # MySQL数据库连接参数  
    username = appconfig.username
    password = appconfig.password
    host = appconfig.host
    database = appconfig.database
    
     
    # 创建数据库连接字符串  
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')  
        
    # 将DataFrame写入MySQL数据库  
    # 假设数据库中已经有一个名为'stock_data'的表，其结构与DataFrame相同  
    # 如果表不存在，你需要先创建它  
    df.to_sql('stock_data', con=engine, if_exists='append', index=False)  
    

# 获取当前日期
today = datetime.now()
i=0
# 采集range(1)几天前的数据
for i in range(60):  
    # 计算昨天的日期和时间  
    yesterday = today - timedelta(days=i) 
    # 这里写你想要在循环中执行的代码  
    print(i)  # 例如，打印当前的循环次数
    print(yesterday)
    try: 
        stockListPrice(yesterday)
    except:
        print("except!")

# 30 和 68
# SELECT *
# FROM `stock_data` st
# where st.trade_date  = '2024-08-23' 
# and  st.pct_chg > 9.5 
# and st.high = st.close 
# and SUBSTRING(st.ts_code, 8, 2) <> 'BJ'
# and ( SUBSTRING(st.ts_code, 1, 2) = '30' or SUBSTRING(st.ts_code, 1, 2) = '68' )

# 00 和 60
# SELECT *
# FROM `stock_data` st
# where st.trade_date  = '2024-08-23' 
# and  st.pct_chg > 9.5 
# and st.high = st.close 
# and SUBSTRING(st.ts_code, 8, 2) <> 'BJ'
# and ( SUBSTRING(st.ts_code, 1, 2) = '00' or SUBSTRING(st.ts_code, 1, 2) = '60' )

# MA60
# select ROUND(AVG(a.cl),2) avgclose from (
# -- 当前价格写入
# select  14.88 as cl ,curdate() as da
# union
# SELECT st.`close` as cl,st.trade_date as da
# FROM `stock_data` st
# where st.ts_code = '300531.SZ'
# order by  da desc
# limit 1,60 -- MA60
# ) a
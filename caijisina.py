import requests  
  
def fetch_stock_increase_ranking(url):  
    headers = {  
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'  
    }  
      
    try:  
        response = requests.get(url, headers=headers)  
        response.raise_for_status()  # 如果响应状态码不是200，则抛出HTTPError异常  
          
        data = response.json()  # 解析JSON数据  
          
        # 假设返回的JSON数据中有一个名为'data'的键，它包含了股票数据  
        # 注意：这里的键名（如'data'）需要根据实际返回的JSON结构来确定  
        stock_list = data
        for stock in stock_list:  
        # 假设每个股票数据包含'symbol'（股票代码）、'name'（股票名称）和'changepercent'（涨幅）等字段  
        # 注意：这里的字段名（如'symbol', 'name', 'changepercent'）需要根据实际返回的JSON结构来确定  
            if 'symbol' in stock and 'name' in stock and 'changepercent' in stock:  
                print(f"股票代码: {stock['symbol']}, 股票名称: {stock['name'].ljust(6)},涨幅: {stock['changepercent']}%,卖价：{stock['sell']},开盘{stock['open']},高{stock['high']},低{stock['low']},")  
               
    except requests.RequestException as e:  
        print(f"请求出错: {e}")  
  
# js列表 https://vip.stock.finance.sina.com.cn/mkt/js/stock_list_cn.js?ts=202002271549
# sian财经行情全部A股
url = 'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=100&sort=changepercent&asc=0&node=hs_a&symbol=&_s_r_a=init'  

# sian财经行情 上证A股
# url = 'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=100&sort=changepercent&asc=0&node=sh_a&symbol=&_s_r_a=init'  

# sian财经行情 深证A股
# url = 'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=100&sort=changepercent&asc=0&node=sz_a&symbol=&_s_r_a=init'  

# sina财经行情 创业板
# url = 'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=80&sort=changepercent&asc=0&node=cyb&symbol=&_s_r_a=sort'

# sina财经行情 科创板
# url = 'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=80&sort=changepercent&asc=0&node=kcb&symbol=&_s_r_a=sort'

fetch_stock_increase_ranking(url)


# C:\Python\project\daban>python caijisina.py
# 股票代码: bj832802, 股票名称: 保丽洁, 涨幅: 22.871%
# 股票代码: sz300187, 股票名称: 永清环保, 涨幅: 20.048%
# 股票代码: sz300639, 股票名称: 凯普生物, 涨幅: 20.042%
# 股票代码: sz301288, 股票名称: 清研环境, 涨幅: 20.033%
# 股票代码: sz300147, 股票名称: 香雪制药, 涨幅: 20.023%
# 股票代码: sz300875, 股票名称: 捷强装备, 涨幅: 19.99%
# 股票代码: sz300436, 股票名称: 广生堂, 涨幅: 19.978%
# 股票代码: sz301060, 股票名称: 兰卫医学, 涨幅: 19.95%
# 股票代码: sz300622, 股票名称: 博士眼镜, 涨幅: 19.855%
# 股票代码: sz300013, 股票名称: *ST新宁, 涨幅: 19.231%
# 股票代码: bj832145, 股票名称: 恒合股份, 涨幅: 16.736%
# 股票代码: sz300204, 股票名称: 舒泰神, 涨幅: 16.45%
# 股票代码: sz300256, 股票名称: 星星科技, 涨幅: 13.942%
# 股票代码: bj830946, 股票名称: 森萱医药, 涨幅: 13.69%
# 股票代码: sz300854, 股票名称: 中兰环保, 涨幅: 13.641%
# 股票代码: sz300261, 股票名称: 雅本化学, 涨幅: 13.406%
# 股票代码: sz301075, 股票名称: 多瑞医药, 涨幅: 12.008%
# 股票代码: sz300471, 股票名称: 厚普股份, 涨幅: 11.856%
# 股票代码: sz301399, 股票名称: 英特科技, 涨幅: 10.635%
# 股票代码: sz300149, 股票名称: 睿智医药, 涨幅: 10.297%
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
                print(f"股票代码: {stock['symbol']}, 股票名称: {stock['name']}, 涨幅: {stock['changepercent']}%")  
               
    except requests.RequestException as e:  
        print(f"请求出错: {e}")  
  
# 使用示例  
url = 'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=99&sort=changepercent&asc=0&node=hs_a&symbol=&_s_r_a=init'  
fetch_stock_increase_ranking(url)
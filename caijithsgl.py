import appconfig
import requests  
from bs4 import BeautifulSoup
import mysql.connector  
from mysql.connector import Error

def hy_str(s):
    # s = "计算机 -- IT服务Ⅱ -- IT服务Ⅲ （共117家）"  
  
    # 1. 去掉所有空格  
    s_no_spaces = s.replace(" ", "")  
    
    # 2. 去掉包括“（”及其后面的所有字符串  
    # 这里我们找到“（”的位置，并截取它之前的所有内容  
    index_of_bracket = s_no_spaces.find("（")  
    if index_of_bracket != -1:  # 如果找到了“（”  
        s_no_bracket_and_spaces = s_no_spaces[:index_of_bracket]  
    else:  
        s_no_bracket_and_spaces = s_no_spaces  # 如果没有找到“（”，则整个字符串都不变  
    
    # 3. 替换“--”为“,”  
    # 注意：由于之前已经去掉了空格，所以这里直接替换“--”即可  
    final_string = s_no_bracket_and_spaces.replace("--", ",")  
    
    return final_string  # 输出: 计算机,IT服务Ⅱ,IT服务Ⅲ
  
# 行业采集
def fetch_span_content(url):  
    headers = {  
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'  
    }  
    try:  
        response = requests.get(url, headers=headers)  
        response.raise_for_status()  # 如果响应状态码不是200，则抛出HTTPError异常  
          
        # 尝试显式指定UTF-8编码（尽管requests通常会这样做）  
        response.encoding = 'gbk'  
          
        # 解析HTML  
        soup = BeautifulSoup(response.text, 'html.parser')  
          
        # 查找<span class="tip f14">标签  
        span_tag = soup.find('span', class_='tip f14')  
        if span_tag:  
            # 获取并打印标签内的文本内容  
            content = span_tag.get_text(strip=True)  
            stockHy = hy_str(content)
            # print("找到的内容:", content)  
        # else:  
            # print("未找到<span class='tip f14'>标签")  
              
    except requests.RequestException as e:  
        print(e)  
    return stockHy

#概念采集
def fetch_concept_names(url):  
    conceptList = ""
    headers = {  
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'  
    }
    try:  
        # 发送HTTP GET请求
        response = requests.get(url, headers=headers)
        # 尝试显式指定UTF-8编码（尽管requests通常会这样做）  
        response.encoding = 'gbk'  
       
        # 检查请求是否成功  
        if response.status_code != 200:  
            print("Failed to retrieve the page")  
            return []  
        
        # 使用BeautifulSoup解析HTML  
        soup = BeautifulSoup(response.text, 'html.parser')  
        
        # 查找包含概念名称的表格行  
        # 注意：这里假设概念名称位于表格的<td>标签内，并且表格有特定的类或ID（这里需要根据实际HTML结构调整）  
    
       # 查找所有class为"gnName"的<td>标签  
        concept_names = soup.find_all('td', class_='gnName')  
    
        # 提取并打印概念名称  
        for concept in concept_names:  
            # 去除标签内的额外空格和换行符  
            clean_name = concept.get_text(strip=True)  
            conceptList +=  clean_name +  "," 

    except requests.RequestException as e:  
        print(e)  
    return conceptList  
  
def fetch_concept(ts_code):
    # 行业采集地址
    url = 'https://basic.10jqka.com.cn/'+ts_code+'/field.html'  
    concept_span = fetch_span_content(url)
    # print( fetch_span_content(url) )

    # 概念采集地址
    url = 'https://basic.10jqka.com.cn/'+ts_code+'/concept.html'  
    concept_names = fetch_concept_names(url)  
    # print(concept_names)  
    fetch_concept_list = concept_names + concept_span
    return fetch_concept_list

#######################################################################################################
def connect_to_mysql():  
    try:  
        connection = mysql.connector.connect(  
            host=appconfig.host,         # MySQL服务器地址  
            database=appconfig.database, # 数据库名  
            user=appconfig.username,     # 数据库用户名  
            password=appconfig.password  # 数据库密码  
        )  
        if connection.is_connected():  
            db_Info = connection.get_server_info()  
            print(f"Connected to MySQL Server version {db_Info}")  
            print("成功连接到MySQL数据库")  
            return connection  
        else:  
            print("连接失败")  
    except Error as e:  
        print(f"连接错误: {e}")  
  
def execute_query(connection, query, params=None):  
    cursor = connection.cursor()  
    try:  
        if params:  
            cursor.execute(query, params)  
        else:  
            cursor.execute(query)  
        # cursor.execute(query)  
        # connection.commit()  
        return cursor.fetchall()  
    except Error as e:  
        print(f"执行查询错误: {e}")  
    # finally:  
    #     if connection.is_connected():  
    #         cursor.close()  
    #         connection.close()  

def execute_insert(connection, query, params=None):  
    cursor = connection.cursor()  
    try:  
        cursor.execute(query,params)  
        connection.commit()  
    except Error as e:  
        print(f"执行查询错误: {e}") 
    finally:  
        if connection.is_connected():  
            cursor.close()  


def fetch_concept_caiji():  
    connection = connect_to_mysql()  
    if connection:  
        # 查询最新的trade_date和对应的ts_code  
        # query = f"""
        # SELECT left(sd.ts_code, 6) as ts_code, sd.trade_date  
        # FROM `stock_data` sd  
        # WHERE sd.trade_date = (SELECT MAX(sd2.trade_date) FROM `stock_data` sd2)  
        # """  

        query = f"""
        select * from (
            SELECT left(sd.ts_code, 6) as ts_code, sd.trade_date  
            FROM `stock_data` sd  
            WHERE sd.trade_date = (SELECT MAX(sd2.trade_date) FROM `stock_data` sd2)  
            ) ts
            where ts.ts_code not in (select sc.ts_code from stock_concepts sc   ) 
        """

        results = execute_query(connection, query)  
        print(results)
          
        if results:  
            for row in results: 
                # 假设我们只处理第一个结果（如果有多个结果，可以循环处理）  
                # ts_code, trade_date = results[0]  
                ts_code, trade_date = row
                # 采集判断同花顺概念+行业
                concepts = fetch_concept(ts_code)
                trade_date = trade_date.strftime('%Y-%m-%d')  

                # 插入到stock_concepts表  
                insert_query = """  
                INSERT INTO `stock_concepts` (`ts_code`, `trade_date`, `concepts`)  
                VALUES (%s, %s,  %s)  
                """  
                
                val = (ts_code, trade_date,concepts)  
                print(insert_query)
                print(val)
                execute_insert(connection, insert_query, val)  
                print(f"成功插入 {ts_code} 到 stock_concepts 表，trade_date: {trade_date},concepts:{concepts}")  
            else:  
                print("没有找到结果")  
  
        connection.close()  

if __name__ == "__main__":  
    fetch_concept_caiji()

# print( fetch_concept('000566') )
# 获取ts_code
# SELECT left(sd.ts_code ,6) as ts_code
# FROM `stock_data` sd
# where sd.trade_date = (select max(sd2.trade_date) from `stock_data` sd2)

# 采集程序由于mysql连接过多中断，取没有采集完的ts_code
# select * from (
# SELECT left(sd.ts_code, 6) as ts_code, sd.trade_date  
# FROM `stock_data` sd  
# WHERE sd.trade_date = (SELECT MAX(sd2.trade_date) FROM `stock_data` sd2)  
# ) ts
# where ts.ts_code not in (select sc.ts_code from stock_concepts sc   ) 

# 概念查询
# select * from  `stock_concepts`  sc
# where sc.concepts like '%AI%'
import requests  
from bs4 import BeautifulSoup  

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
  
if __name__ == "__main__":  
    url = 'https://basic.10jqka.com.cn/000058/field.html'  
    print( fetch_span_content(url) )
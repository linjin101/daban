from flask import Flask, render_template, jsonify, request
import caiji2 


app = Flask(__name__)
ipconfig = '192.168.10.3:5000'
app.config['SERVER_NAME'] = ipconfig


cmdlist = 'jinja2.exceptions.TemplateNotFound: index2.html \
127.0.0.1 - - [30/Jul/2024 16:43:29] "GET /?__debugger__=yes&cmd=resource&f=style.css HTTP/1.1" 304 - \
127.0.0.1 - - [30/Jul/2024 16:43:29] "GET /?__debugger__=yes&cmd=resource&f=debugger.js HTTP/1.1" 304 - \
127.0.0.1 - - [30/Jul/2024 16:43:29] "GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 304 - \
127.0.0.1 - - [30/Jul/2024 16:43:29] "GET /?__debugger__=yes&cmd=resource&f=console.png HTTP/1.1" 304 - \
127.0.0.1 - - [30/Jul/2024 16:43:43] "GET / HTTP/1.1" 200 - \
 * Detected change in  C:\\Python\\project\\gpcj\\flask\\app.py , reloading \
 * Restarting with stat \
 * Debugger is active! \
 * Debugger PIN: 545-969-117 \
 * Detected change in  C:\\Python\\project\\gpcj\\flask\\app.py , reloading \
 * Restarting with stat \
 * Debugger is active! \
 * Debugger PIN: 545-969-117'
 

@app.route('/getData')
def data():
    # 假设这是你要通过AJAX获取的数据
    # response_data = '假设这是你要通过AJAX获取的数据'
    response_data = caiji2.reList(1)
    return response_data
    # response_data = {'key': 'dddd'}
    # return jsonify(response_data)

@app.route('/getData2')
def data2():
    # 假设这是你要通过AJAX获取的数据
    # response_data = '假设这是你要通过AJAX获取的数据'
    response_data = caiji2.reList(2)
    return response_data
    # response_data = {'key': 'dddd'}
    # return jsonify(response_data)

@app.route('/')
def index():
    userconfig = {'ipconfig': ipconfig}  
    return render_template('index2.html',userconfig=userconfig)

# @app.route('/process_input', methods=['POST'])
# def process_input():
#     input_text = request.form['input_text']
#     # 在这里对接收到的数据进行处理，例如输出到控制台或返回给前端页面
#     print("Received input text:", input_text)
#     return "Input text received: " + input_text

if __name__ == '__main__':
    app.run(debug=True)

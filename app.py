from flask import Flask, render_template, jsonify, request
import caiji2 
import appconfig

app = Flask(__name__)
# 读取appconfig服务器配置
ipconfig = appconfig.ipconfig
ipconfigHtml = appconfig.ipconfigHtml

app.config['SERVER_NAME'] = ipconfig

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

@app.route('/getData3')
def data3():
    # 假设这是你要通过AJAX获取的数据
    # response_data = '假设这是你要通过AJAX获取的数据'
    response_data = caiji2.reList(3)
    return response_data
    # response_data = {'key': 'dddd'}
    # return jsonify(response_data)

@app.route('/')
def index():
    userconfig = {'ipconfig': ipconfigHtml}  
    return render_template('index2.html',userconfig=userconfig)

# @app.route('/process_input', methods=['POST'])
# def process_input():
#     input_text = request.form['input_text']
#     # 在这里对接收到的数据进行处理，例如输出到控制台或返回给前端页面
#     print("Received input text:", input_text)
#     return "Input text received: " + input_text

if __name__ == '__main__':
    app.run(debug=True)

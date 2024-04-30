from flask import Flask

app = Flask('test')

@app.route('/ping', methods = ['GET'])
def ping():
	return "PONG"


# 开始进行运行
if __name__ == '__main__':
	app.run(debug=True, host = '0.0.0.0', port = 9696)  # debug = True意味着出现bug会自动重启程序，host是web公开化，port是端口
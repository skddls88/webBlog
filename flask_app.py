from flask import Flask, redirect, render_template, request, session, url_for , g ,jsonify , abort , Response

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')



# 파이썬애니웨어(www.pythonanywhere.com)에서 구동할 때는
# 아래 코드를 사용해선 안 된다. 로컬에서 구동할 때만 사용한다.
# if __name__ == '__main__':
#     app.run(debug=True)


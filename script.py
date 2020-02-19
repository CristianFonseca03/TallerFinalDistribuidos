from flask import Flask, render_template, request
import connection as conn

app = Flask(__name__)

RPC_Server = '127.0.0.1:8000'
b_1 = '127.0.0.1'

@app.route("/", methods=['POST','GET'])
def index():
    if request.method == 'POST':
        sql = request.form['sql']
        try:
            conn.isRuning(RPC_Server)
            conn_1 = conn.create_conn(b_1)
        except NameError as e:
            conn.sendText(RPC_Server,e)
            return render_template('index.html', error='No se puede conectar a las bases de datos')
        except (TimeoutError,ConnectionRefusedError):
            return render_template('index.html', error='No se puede conectar al servidor RPC')
        else:
            try:
                conn.execute(conn_1,sql)
            except NameError as e:
                conn.sendText(RPC_Server,e)
                return render_template('index.html', error='Sql invalido')
            else:
                conn.commit(conn_1)
                conn.sendText(RPC_Server,'Consultas ejecutadas con exito')
                return render_template('index.html', message='Consultas ejecutadas con exito')
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    app.run()
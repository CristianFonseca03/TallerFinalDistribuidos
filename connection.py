import cx_Oracle
import xmlrpc.client
from datetime import datetime

def create_conn(ip):
    try:
        conn_str='HR/1234@'+ip+':1521/XE'
        db_conn = cx_Oracle.connect(conn_str)
    except cx_Oracle.DatabaseError as e:
        raise NameError('Error al conectar a oracle en '+ip)
    except TimeoutError as e:
        raise NameError('Error al conectar a oracle en '+ip)    
    return db_conn

def execute(conn,sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except cx_Oracle.DatabaseError as e:
        raise NameError('Sql no valido')

def commit(conn):
    conn.commit()

def sendText(ip,text):
    now = datetime.now()
    conn = xmlrpc.client.ServerProxy('http://'+ip+'/',allow_none=True)
    conn.sendText(str(text)+' '*4+now.strftime("%d")+'/'+now.strftime("%m")+'/'+now.strftime("%Y")+" "+now.strftime("%H:%M:%S"))

def isRuning(ip):
    conn = xmlrpc.client.ServerProxy('http://'+ip+'/',allow_none=True)
    conn.is_runing()
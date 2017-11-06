import pymysql

def login(usuario, password):
    resultado = 0
    try:
        conn = pymysql.connect(user="root",passwd="pires777",host="127.0.0.1",port=3306,database="dblaberinto")
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT nombre FROM Usuario WHERE usuario='"+usuario+"' AND password='"+password+"'")
            row = cursor.fetchone()
            nombre = str(row[0])
            resultado = 1
        except Exception:
            print("Error de logueo de"+str(self.client_address))
            resultado = 2
        conn.close()
    except Exception:
        resultado = 3
    return resultado

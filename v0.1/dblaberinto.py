import pymysql

def login(usuario, password):
    try:
        conn = pymysql.connect(user="root",passwd="pires777",host="127.0.0.1",port=3306,database="dblaberinto")
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT nombre FROM Usuario WHERE usuario='"+usuario+"' AND password='"+password+"'")
            row = cursor.fetchone()
            nombre = str(row[0])
            return True
        except Exception:
            print("Error de logueo")
        conn.close()
    except Exception:
        print("Error de base de datos")

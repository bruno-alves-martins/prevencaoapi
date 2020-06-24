from passlib.hash import pbkdf2_sha256 as sha256
import cx_Oracle


 
def generate_hash(password):
        return sha256.hash(password)


def verify_hash(password, hash):
        return sha256.verify(password, hash)


def save_to_db(nome, username, password):
         con = cx_Oracle.connect('prevencao/prevencao@piodb-scan.pioxii.com.br/hcb', encoding='UTF-8')
         print("conectou")


         password = generate_hash(password)

         print(password)

         cur = con.cursor()
         cur.execute("INSERT INTO PREV_USER (NOME, USERNAME, PASSWORD) values (:NOME, :USERNAME, :PASSWORD)", [nome,username,password])
         con.commit()

         cur.close()
         con.close()


         return


def valida_login(username, password):
    con = cx_Oracle.connect('prevencao/prevencao@piodb-scan.pioxii.com.br/hcb', encoding='UTF-8')
    cur = con.cursor()
    cur.prepare('SELECT PU.NOME, PU.USERNAME, PU.PASSWORD FROM PREV_USER PU WHERE PU.USERNAME = :username') 
    cur.execute(None, {'username': username})
    row = cur.fetchone()
    
    senha = row[2]
              
    cur.close()
    con.close()


    return verify_hash(password, senha)


        

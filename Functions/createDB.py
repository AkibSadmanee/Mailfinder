def createDB(hostname, username, passwrd):
    import pymysql

    conn = pymysql.connect(
        host = hostname,
        user = username,
        password = passwrd,
    )

    cursor = conn.cursor()

    sql = 'CREATE DATABASE Emails'
    try:
        cursor.execute(sql)
    except:
        pass

    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        db='Emails'
    )

    cursor = conn.cursor()

    sql = '''CREATE TABLE Emails_t(
            Email_id VARCHAR(50) NOT NULL,
            Mail_Open_Status BOOLEAN DEFAULT 0 NOT NULL,
            Link_Click_status BOOLEAN DEFAULT 0 NOT NULL,
            PRIMARY KEY(Email_id))
    '''
    try:
        cursor.execute(sql)
    except:
        pass
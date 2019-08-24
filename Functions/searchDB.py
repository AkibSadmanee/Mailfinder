def searchDB(hostname,username,passwrd):
    import pymysql

    conn = pymysql.connect(
        host = hostname,
        user = username,
        password = passwrd,
        db = 'Emails'
    )

    cursor = conn.cursor()

    sql = 'SELECT * from `Emails_t`;'
    data = cursor.execute(sql)
    fetched_tuple = cursor.fetchall()
    fetched_list=[]
    for Tuple in fetched_tuple:
        fetched_list.append(list(Tuple))

    return fetched_list
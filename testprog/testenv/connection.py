import cx_Oracle

def ApsDbConn():
    host = "localhost"  #資料庫ip
    port = "1521"   #埠
    sid = "ORCL"  #資料庫名稱
    dsn = cx_Oracle.makedsn(host, port, sid)
    #scott是資料使用者名稱，tiger是登入密碼（預設使用者名稱和密碼）
    conn = cx_Oracle.connect("aps", "aps", dsn)
    return conn
import os
import connection 
import collections
import sqldata
import datetime

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

def ifnull(var, val):
  if var is None:
    return val
  return var

def QueryWip():
  sql = 'SELECT * FROM "DALAB".F_WIP'
  # 使用pandas 的read_sql函式，可以直接將資料存放在dataframe中
  mediumconn=connection.MediumDbConn()
  cursor = mediumconn.cursor()
  cursor.execute(sql)
  names = [c[0] for c in cursor.description]
  cursor.rowfactory = collections.namedtuple("Data", names)
  # mediumconn.close()
  return cursor,mediumconn
 

def MergeWip():
  wip = QueryWip()
  apsdata =  wip[0]
  mediumconn = wip[1]
  apsconn=connection.ApsDbConn()
  cursor = apsconn.cursor()
  try:
    for row in apsdata:
      result = sqldata.WipMergeSql(row.ORDERNO, row.LOT , row.IS_HOLD , row.WDATE , row.PRODUCT_REVISION , row.OP_NO , row.OP_NAME, row.LAYER, row.QTY, row.PCSQTY, row.PRODUCT_TYPE, row.ARRIVAL_TIME, row.HODINGTIME, row.IS_ROCKET, row.LOTTYPE, row.PRODUCT_ID, )
      sql=result[0]
      param=result[1]
      print(tuple(param))
      
      cursor.execute(sql,tuple(param))
  except ValueError:
      print(ValueError)
  finally:
    apsconn.commit()
    cursor.close()
    apsconn.close()
    mediumconn.close()

MergeWip()


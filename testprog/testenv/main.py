import os
import connection 
import collections
import sqldata
import json
import wiptest

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
apsconn=connection.ApsDbConn()
cursor = apsconn.cursor()

def main():
    downtimedata = Query(sqldata.downtime(),"Downtime")
    opelimitdata = Query(sqldata.opelimit(),"Opelimit")
    availabletimedata = Query(sqldata.availabletime(),"Availabletime")
    shippingdatedata = Query(sqldata.shippingdate(),"Shippingdate")
    rocketdata = Query(sqldata.rocket(),"Rocket")
    lotcountdata = Query(sqldata.lotcount(),"Lotcount")
    lotcountdata = Query(sqldata.safeope(),"Safeope")
    # wiplimitdata = Query(sqldata.getschedule(),"Wiplimit")
    # fixturelimitdata = Query(sqldata.getschedule(),"FixtureLimit")

    shippinglist=[]
    for data in shippingdatedata:
        ele={}
        ele["PRODUCEQTY"] = data.PRODUCEQTY
        ele["PRODUCT_ID"] = data.PRODUCT_ID
        ele["SHIPPING_DATE"] = str(data.SHIPPING_DATE)
        ele["SHEEPQTY"] = data.SHEEPQTY
        ele["DIFF"] = data.DIFF
        shippinglist.append(ele)

    output = {}
    output['downtime'] = downtimedata[0].CNT
    output['opelimit'] = opelimitdata[0].CNT
    output['availabletime'] = availabletimedata[0].CNT
    output['rocket'] = rocketdata[0].CNT
    output['lotcount'] = lotcountdata[0].CNT
    output['safeope'] = lotcountdata[0].CNT
    return output,shippinglist

def Query(sql,method):
  cursor.execute(sql)
  names = [c[0] for c in cursor.description]
  cursor.rowfactory = collections.namedtuple(method, names)
  data = cursor
  if method == "Wiplimit":
    list = {}
    for i in data:
          ele={}
          ele["LOT"] = i.GROUP_LOT
          ele["QTY"] = i.QTY
          ele["OPE_ID"] = i.OPE_ID
          ele["START_TIME"] =str(i.START_TIME)
          ele["END_TIME"] = str(i.END_TIME)
          ele["MAX_WIP"] = i.MAX_WIP
          list[i.GROUP_LOT] = ele
  elif method == "FixtureLimit":
    list = {}
    for i in data:
      ele={}
      ele["LOT"] = i.GROUP_LOT
      ele["QTY"] = i.QTY
      ele["OPE_ID"] = i.OPE_ID
      ele["LAYER"] = str(i.LAYER)
      ele["PRODUCT_ID"] = i.PRODUCT_ID
      ele["START_TIME"] =str(i.START_TIME)
      ele["END_TIME"] = str(i.END_TIME)
      ele["FIXTURE_QTY"] = i.FIXTURE_QTY
      list[i.GROUP_LOT] = ele
  else:
    list = []
    for ele in data:
        list.append(ele)
  return list

output = main()
# jsonoutput = json.loads(str(output))
with open('./outputdata/testoutput.json', 'w' ,encoding="utf-8") as f:
    json.dump(output[0], f)
with open('./outputdata/shippingoutput.json', 'w' ,encoding="utf-8") as f:
    json.dump(output[1], f)
cursor.close()
apsconn.close()
wiptest.main()



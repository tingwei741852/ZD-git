import os
import connection 
import collections
import sqldata
import json

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
    output['shippingdate'] = shippinglist
    return output

def Query(sql,method):
    cursor.execute(sql)
    names = [c[0] for c in cursor.description]
    cursor.rowfactory = collections.namedtuple(method, names)
    # data = cursor.fetchall() 
    data = cursor
    list = []
    for ele in data:
        list.append(ele)
    return list

output = main()
# jsonoutput = json.loads(str(output))
with open('testoutput.json', 'w') as f:
    json.dump(output, f)

print(output)
cursor.close()
apsconn.close()



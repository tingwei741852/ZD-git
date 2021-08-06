import connection 
import collections
import sqldata
import json
import datetime

apsconn=connection.ApsDbConn()
cursor = apsconn.cursor()

def wiptest(data):
    timedict = {}
    for schedule in data:
        id = schedule
        # starttime = data.get(schedule)["START_TIME"]
        # endtime = data.get(schedule)["END_TIME"]
        starttime = datetime.datetime.strptime(data.get(schedule)["START_TIME"], "%Y-%m-%d %H:%M:%S")
        endtime = datetime.datetime.strptime(data.get(schedule)["END_TIME"], "%Y-%m-%d %H:%M:%S")
        ope = data.get(schedule)["OPE_ID"]
        qty = data.get(schedule)["QTY"]
        maxwip = data.get(schedule)["MAX_WIP"]
        dictid = str(starttime)+"-"+str(endtime)
        if not ope in timedict:
            element = {}
            element["maxwip"] = maxwip
            element["timelist"] = {}
            timedict[ope] = element
        if not dictid in timedict[ope]["timelist"]:
            ele = {}
            ele["time"] = [starttime,endtime]
            ele["schlist"] = [id]
            ele["qty"] = qty
            timedict[ope]["timelist"][dictid] = ele
            # print(timedict)
        for item in list(timedict[ope]["timelist"]):#檢查dict每個時間區間
            itemtime = timedict.get(ope)["timelist"].get(item).get("time")
            overlaplist = overlap(itemtime,[starttime,endtime])#檢查時間是否重疊
            if(len(overlaplist)!=0):#如果時間有重疊
                timeid = overlaplist[0]+"-"+overlaplist[1]#重疊時間id
                if timeid in timedict.get(ope).get("timelist"):#如果時間id存在
                    templist = [id]
                    for a in timedict.get(ope)["timelist"].get(item).get("schlist"):
                        templist.append(a)
                    for i in templist:
                        if not i in timedict.get(ope)["timelist"].get(timeid).get("schlist"):#如果重疊的時間中沒有目前的schedul id
                            timedict.get(ope)["timelist"].get(timeid).get("schlist").append(i)#新增
                            tempqty = int(timedict.get(ope)["timelist"].get(timeid).get("qty"))+qty
                            timedict.get(ope)["timelist"].get(timeid)["qty"]= tempqty
                else: #如果時間id不存在
                    eleqty =  timedict.get(ope)["timelist"].get(item).get("qty")
                    ele = {}
                    ele["time"] = [datetime.datetime.strptime(overlaplist[0], "%Y-%m-%d %H:%M:%S"),datetime.datetime.strptime(overlaplist[1], "%Y-%m-%d %H:%M:%S")]
                    templist = [id]
                    for a in timedict.get(ope)["timelist"].get(item).get("schlist"):
                        templist.append(a)
                    ele["schlist"] = templist
                    ele["qty"] = eleqty+qty
                    timedict[ope]["timelist"][timeid] = ele
        # print(timedict)
    return timedict
def fixturetest(data):
    timedict = {}
    for schedule in data:
        id = schedule
        # starttime = data.get(schedule)["START_TIME"]
        # endtime = data.get(schedule)["END_TIME"]
        starttime = datetime.datetime.strptime(data.get(schedule)["START_TIME"], "%Y-%m-%d %H:%M:%S")
        endtime = datetime.datetime.strptime(data.get(schedule)["END_TIME"], "%Y-%m-%d %H:%M:%S")
        ope = data.get(schedule)["OPE_ID"]
        layer = data.get(schedule)["LAYER"]
        product = data.get(schedule)["PRODUCT_ID"]
        qty = data.get(schedule)["QTY"]
        fixture_qty = data.get(schedule)["FIXTURE_QTY"]
        dictid = str(starttime)+"-"+str(endtime)
        typeid = ope+"-"+layer+"-"+product
        if not typeid in timedict:
            element = {}
            element["fixture_qty"] = fixture_qty
            element["timelist"] = {}
            timedict[typeid] = element
        if not dictid in timedict[typeid]["timelist"]:
            ele = {}
            ele["time"] = [starttime,endtime]
            ele["schlist"] = [id]
            ele["qty"] = qty
            timedict[typeid]["timelist"][dictid] = ele
        for item in list(timedict[typeid]["timelist"]):#檢查dict每個時間區間
            itemtime = timedict.get(typeid)["timelist"].get(item).get("time")
            overlaplist = overlap(itemtime,[starttime,endtime])#檢查時間是否重疊
            if(len(overlaplist)!=0):#如果時間有重疊
                timeid = overlaplist[0]+"-"+overlaplist[1]#重疊時間id
                if timeid in timedict.get(typeid).get("timelist"):#如果時間id存在
                    templist = [id]
                    for a in timedict.get(typeid)["timelist"].get(item).get("schlist"):
                        templist.append(a)
                    for i in templist:
                        if not i in timedict.get(typeid)["timelist"].get(timeid).get("schlist"):#如果重疊的時間中沒有目前的schedul id
                            timedict.get(typeid)["timelist"].get(timeid).get("schlist").append(i)#新增
                            tempqty = int(timedict.get(typeid)["timelist"].get(timeid).get("qty"))+qty
                            timedict.get(typeid)["timelist"].get(timeid)["qty"]= tempqty
                else: #如果時間id不存在
                    eleqty =  timedict.get(typeid)["timelist"].get(item).get("qty")
                    ele = {}
                    ele["time"] = [datetime.datetime.strptime(overlaplist[0], "%Y-%m-%d %H:%M:%S"),datetime.datetime.strptime(overlaplist[1], "%Y-%m-%d %H:%M:%S")]
                    templist = [id]
                    for a in timedict.get(typeid)["timelist"].get(item).get("schlist"):
                        templist.append(a)
                    ele["schlist"] = templist
                    ele["qty"] = eleqty+qty
                    timedict[typeid]["timelist"][timeid] = ele
        # print(timedict)
    return timedict


def overlap(timelist1,timelist2):
    if timelist2[0]<timelist1[0]:
        time1 = timelist2
        time2 = timelist1
    else:
        time1 = timelist1
        time2 = timelist2
    if((time1[0] <=time2[1] and time1[1]>time2[0])):
        starttime=max(time1[0],time2[0])
        endtime=min(time1[1],time2[1])
        return [str(starttime),str(endtime)]
    else:
        return []
def Query(sql,method):
    cursor.execute(sql)
    names = [c[0] for c in cursor.description]
    cursor.rowfactory = collections.namedtuple(method, names)
    # data = cursor.fetchall() 
    data = cursor
    list = {}
    if method == "wip":
      for i in data:
          ele={}
          ele["LOT"] = i.GROUP_LOT
          ele["QTY"] = i.QTY
          ele["OPE_ID"] = i.OPE_ID
          ele["START_TIME"] =str(i.START_TIME)
          ele["END_TIME"] = str(i.END_TIME)
          ele["MAX_WIP"] = i.MAX_WIP
          list[i.GROUP_LOT] = ele
    elif method == "fixture":
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
    return list

def main():
  # 取得各工序每個時段的WIP數量
  wipoutput = wiptest(Query(sqldata.getschedule(),"wip"))
  # 取得個工序層別產品每個時段的製程數量
  fixtureoutput = fixturetest(Query(sqldata.getfixturelimit(),"fixture"))
  wipresult = {}
  fixtureresult = {}
  # 整理WIP限制資料，取出超過限制WIP數量的資料
  for typeid in wipoutput:
      element = {}
      element["maxwip"] = wipoutput.get(typeid).get("maxwip")
      element["timelist"] = []
      for time in wipoutput.get(typeid).get("timelist"):
          timeele = {}
          timeele["start_time"] = str(wipoutput.get(typeid).get("timelist").get(time).get("time")[0])
          timeele["end_time"] = str(wipoutput.get(typeid).get("timelist").get(time).get("time")[1])
          timeele["qty"] = wipoutput.get(typeid).get("timelist").get(time).get("qty")
          timeele["diff"] = element["maxwip"] - timeele["qty"] 
          if timeele["diff"] <0:
            element["timelist"].append(timeele) 
      wipresult[typeid] = element
  # 整理治具限制數量，取出超過該工站、層別、產品治具數量的資料
  for typeid in fixtureoutput:
    element = {}
    element["fixture_qty"] = fixtureoutput.get(typeid).get("fixture_qty")
    element["timelist"] = []
    for time in fixtureoutput.get(typeid).get("timelist"):
        timeele = {}
        timeele["start_time"] = str(fixtureoutput.get(typeid).get("timelist").get(time).get("time")[0])
        timeele["end_time"] = str(fixtureoutput.get(typeid).get("timelist").get(time).get("time")[1])
        timeele["qty"] = fixtureoutput.get(typeid).get("timelist").get(time).get("qty")
        timeele["diff"] = element["fixture_qty"] - timeele["qty"] 
        if timeele["diff"] <0:
          element["timelist"].append(timeele) 
    fixtureresult[typeid] = element
  # 寫入檔案
  with open('./outputdata/wipoutput.json', 'w' ,encoding="utf-8") as f:
      json.dump(wipresult, f)
  # 寫入檔案
  with open('./outputdata/fixturelimitoutput.json', 'w' ,encoding="utf-8") as f:
      json.dump(fixtureresult, f)


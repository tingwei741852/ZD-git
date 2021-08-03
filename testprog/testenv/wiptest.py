# import os
# import connection 
# import collections
# import sqldata
import json
import datetime

# apsconn=connection.ApsDbConn()
# cursor = apsconn.cursor()

def main():
    # data = Query(sqldata.getschedul(),"schedule")
    with open('testfile.json') as json_file:
        data = json.load(json_file)
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
            ele["maxwip"] = maxwip
            timedict[ope]["timelist"][dictid] = ele
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
# def Query(sql,method):
#     cursor.execute(sql)
#     names = [c[0] for c in cursor.description]
#     cursor.rowfactory = collections.namedtuple(method, names)
#     # data = cursor.fetchall() 
#     data = cursor
#     list = {}
#     for i in data:
#         ele={}
#         ele["LOT"] = i.LOT
#         ele["QTY"] = i.QTY
#         ele["OPE_ID"] = i.OPE_ID
#         ele["START_TIME"] =str(i.START_TIME)
#         ele["END_TIME"] = str(i.END_TIME)
#         ele["MAX_WIP"] = i.MAX_WIP
#         list[i.LOT] = ele
#     return list

# print(main())
time1 = [datetime.datetime(2021, 4, 23, 21, 29, 20), datetime.datetime(2021, 4, 23, 11, 8, 11)]
time2 = [datetime.datetime(2021, 4, 23, 11, 8, 11), datetime.datetime(2021, 4, 23, 23, 8, 11)]
output = main()
result = {}
for ope in output:
    element = {}
    element["maxwip"] = output.get(ope).get("maxwip")
    element["timelist"] = []
    for time in output.get(ope).get("timelist"):
        timeele = {}
        timeele["start_time"] = str(output.get(ope).get("timelist").get(time).get("time")[0])
        timeele["end_time"] = str(output.get(ope).get("timelist").get(time).get("time")[1])
        timeele["qty"] = output.get(ope).get("timelist").get(time).get("qty")
        timeele["diff"] = element["maxwip"] - timeele["qty"] 
        if timeele["diff"] <0:
            element["timelist"].append(timeele) 
    result[ope] = element
with open('wipoutput.json', 'w') as f:
    json.dump(result, f)
import datetime
def WipMergeSql(ORDERNO,  LOT,  IS_HOLD,  WDATE,  PRODUCT_REVISION,  OP_NO,  OP_NAME,  LAYER,  QTY,  PCSQTY,  PRODUCT_TYPE,  ARRIVAL_TIME,  HODINGTIME,  IS_ROCKET,  LOTTYPE,  PRODUCT_ID):
  sql1 = 'MERGE INTO "APS".F_WIP A\n'+\
             '    USING  (\n'+\
             '        SELECT\n'
  sql2 =  '        FROM\n'+\
            '            DUAL\n'+\
            '    ) M ON(\n'+\
            '      A.LOT = M.LOT\n'+\
            '    )\n'+\
            '    WHEN MATCHED THEN \n'+\
            '        UPDATE SET \n'
  sql3 = '    WHEN NOT MATCHED THEN \n'+\
         '        INSERT (\n'
  sql4 = '        ) VALUES (\n'
  sql5 = ')'
  
  sql_select =''
  sql_update =''
  sql_col =''
  sql_insert =''
  cnt = 0
  param=[]


  if not ORDERNO is None:
    if cnt>0:
      sql_select+=", :"+str(str(cnt+1))+" ORDERNO\n"
      sql_update+=", A.ORDERNO=M.ORDERNO\n"
      sql_col+=", ORDERNO\n"
      sql_insert+=", M.ORDERNO\n"
    else:
      sql_select+=":"+str(cnt+1)+" ORDERNO\n"
      sql_update+="A.ORDERNO=M.ORDERNO\n"
      sql_col+="ORDERNO\n"
      sql_insert+="M.ORDERNO\n"
    param.append(ORDERNO)
    cnt+=1
  if not LOT  is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" LOT \n"
      sql_col+=", LOT \n"
      sql_insert+=", M.LOT \n"
    else:
      sql_select+=":"+str(cnt+1)+" LOT \n"
      sql_update+="A.LOT =M.LOT \n"
      sql_col+="LOT \n"
      sql_insert+="M.LOT \n"
    param.append(LOT)
    cnt+=1
  if not IS_HOLD  is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" IS_HOLD \n"
      sql_update+=", A.IS_HOLD =M.IS_HOLD \n"
      sql_col+=", IS_HOLD \n"
      sql_insert+=", M.IS_HOLD \n"
    else:
      sql_select+=":"+str(cnt+1)+" IS_HOLD \n"
      sql_update+="A.IS_HOLD =M.IS_HOLD \n"
      sql_col+="IS_HOLD \n"
      sql_insert+="M.IS_HOLD \n"
    param.append(IS_HOLD)
    cnt+=1
  if not WDATE  is None:
    if cnt>0:
      sql_select+=", to_date( :"+str(cnt+1)+" ,'yyyy-mm-dd hh24:mi:ss') WDATE\n"
      sql_update+=", A.WDATE =M.WDATE \n"
      sql_col+=", WDATE \n"
      sql_insert+=", M.WDATE \n"
    else:
      sql_select+=":"+str(cnt+1)+" WDATE \n"
      sql_update+="A.WDATE =M.WDATE \n"
      sql_col+="WDATE \n"
      sql_insert+="M.WDATE \n"
    param.append(str(WDATE))
    cnt+=1
  if not PRODUCT_REVISION  is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" PRODUCT_REVISION \n"
      sql_update+=", A.PRODUCT_REVISION =M.PRODUCT_REVISION \n"
      sql_col+=", PRODUCT_REVISION \n"
      sql_insert+=", M.PRODUCT_REVISION \n"
    else:
      sql_select+=":"+str(cnt+1)+" PRODUCT_REVISION \n"
      sql_update+="A.PRODUCT_REVISION =M.PRODUCT_REVISION \n"
      sql_col+="PRODUCT_REVISION \n"
      sql_insert+="M.PRODUCT_REVISION \n"
    param.append(PRODUCT_REVISION)
    cnt+=1
  if not OP_NO  is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" OP_NO \n"
      sql_update+=", A.OP_NO =M.OP_NO \n"
      sql_col+=", OP_NO \n"
      sql_insert+=", M.OP_NO \n"
    else:
      sql_select+=":"+str(cnt+1)+" OP_NO \n"
      sql_update+="A.OP_NO =M.OP_NO \n"
      sql_col+="OP_NO \n"
      sql_insert+="M.OP_NO \n"
    param.append(OP_NO)
    cnt+=1
  if not OP_NAME is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" OP_NAME\n"
      sql_update+=", A.OP_NAME=M.OP_NAME\n"
      sql_col+=", OP_NAME\n"
      sql_insert+=", M.OP_NAME\n"
    else:
      sql_select+=":"+str(cnt+1)+" OP_NAME\n"
      sql_update+="A.OP_NAME=M.OP_NAME\n"
      sql_col+="OP_NAME\n"
      sql_insert+="M.OP_NAME\n"
    param.append(OP_NAME)
    cnt+=1
  if not LAYER is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" \"LAYER\"\n"
      sql_update+=", A.\"LAYER\"=M.LAYER\n"
      sql_col+=", \"LAYER\"\n"
      sql_insert+=", M.\"LAYER\"\n"
    else:
      sql_select+=":"+str(cnt+1)+" \"LAYER\"\n"
      sql_update+="A.\"LAYER\"=M.\"LAYER\"\n"
      sql_col+="\"LAYER\"\n"
      sql_insert+="M.\"LAYER\"\n"
    param.append(LAYER)
    cnt+=1
  if not QTY is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" QTY\n"
      sql_update+=", A.QTY=M.QTY\n"
      sql_col+=", QTY\n"
      sql_insert+=", M.QTY\n"
    else:
      sql_select+=":"+str(cnt+1)+" QTY\n"
      sql_update+="A.QTY=M.QTY\n"
      sql_col+="QTY\n"
      sql_insert+="M.QTY\n"
    param.append(QTY)
    cnt+=1
  if not PCSQTY is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" PCSQTY\n"
      sql_update+=", A.PCSQTY=M.PCSQTY\n"
      sql_col+=", PCSQTY\n"
      sql_insert+=", M.PCSQTY\n"
    else:
      sql_select+=":"+str(cnt+1)+" PCSQTY\n"
      sql_update+="A.PCSQTY=M.PCSQTY\n"
      sql_col+="PCSQTY\n"
      sql_insert+="M.PCSQTY\n"
    param.append(PCSQTY)
    cnt+=1
  if not PRODUCT_TYPE is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" PRODUCT_TYPE\n"
      sql_update+=", A.PRODUCT_TYPE=M.PRODUCT_TYPE\n"
      sql_col+=", PRODUCT_TYPE\n"
      sql_insert+=", M.PRODUCT_TYPE\n"
    else:
      sql_select+=":"+str(cnt+1)+" PRODUCT_TYPE\n"
      sql_update+="A.PRODUCT_TYPE=M.PRODUCT_TYPE\n"
      sql_col+="PRODUCT_TYPE\n"
      sql_insert+="M.PRODUCT_TYPE\n"
    param.append(PRODUCT_TYPE)
    cnt+=1
  if not ARRIVAL_TIME is None:
    if cnt>0:
      sql_select+=", to_date( :"+str(cnt+1)+" ,'yyyy-mm-dd hh24:mi:ss') ARRIVAL_TIME\n"
      sql_update+=", A.ARRIVAL_TIME=M.ARRIVAL_TIME\n"
      sql_col+=", ARRIVAL_TIME\n"
      sql_insert+=", M.ARRIVAL_TIME\n"
    else:
      sql_select+=":"+str(cnt+1)+" ARRIVAL_TIME\n"
      sql_update+="A.ARRIVAL_TIME=M.ARRIVAL_TIME\n"
      sql_col+="ARRIVAL_TIME\n"
      sql_insert+="M.ARRIVAL_TIME\n"
    param.append(str(ARRIVAL_TIME))
    cnt+=1
  if not HODINGTIME is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" HODINGTIME\n"
      sql_update+=", A.HODINGTIME=M.HODINGTIME\n"
      sql_col+=", HODINGTIME\n"
      sql_insert+=", M.HODINGTIME\n"
    else:
      sql_select+=":"+str(cnt+1)+" HODINGTIME\n"
      sql_update+="A.HODINGTIME=M.HODINGTIME\n"
      sql_col+="HODINGTIME\n"
      sql_insert+="M.HODINGTIME\n"
    param.append(HODINGTIME)
    cnt+=1
  if not IS_ROCKET is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" IS_ROCKET\n"
      sql_update+=", A.IS_ROCKET=M.IS_ROCKET\n"
      sql_col+=", IS_ROCKET\n"
      sql_insert+=", M.IS_ROCKET\n"
    else:
      sql_select+=":"+str(cnt+1)+" IS_ROCKET\n"
      sql_update+="A.IS_ROCKET=M.IS_ROCKET\n"
      sql_col+="IS_ROCKET\n"
      sql_insert+="M.IS_ROCKET\n"
    param.append(IS_ROCKET)
    cnt+=1
  if not LOTTYPE is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" LOTTYPE\n"
      sql_update+=", A.LOTTYPE=M.LOTTYPE\n"
      sql_col+=", LOTTYPE\n"
      sql_insert+=", M.LOTTYPE\n"
    else:
      sql_select+=":"+str(cnt+1)+" LOTTYPE\n"
      sql_update+="A.LOTTYPE=M.LOTTYPE\n"
      sql_col+="LOTTYPE\n"
      sql_insert+="M.LOTTYPE\n"
    param.append(LOTTYPE)
    cnt+=1
  if not PRODUCT_ID is None:
    if cnt>0:
      sql_select+=", :"+str(cnt+1)+" PRODUCT_ID\n"
      sql_update+=", A.PRODUCT_ID=M.PRODUCT_ID\n"
      sql_col+=", PRODUCT_ID\n"
      sql_insert+=", M.PRODUCT_ID\n"
    else:
      sql_select+=":"+str(cnt+1)+" PRODUCT_ID\n"
      sql_update+="A.PRODUCT_ID=M.PRODUCT_ID\n"
      sql_col+="PRODUCT_ID\n"
      sql_insert+="M.PRODUCT_ID\n"
    param.append(PRODUCT_ID)
    cnt+=1


  sql = sql1+sql_select+sql2+sql_update+sql3+sql_col+sql4+sql_insert+sql5
  return sql,param

result = WipMergeSql("1001590026",  "1001590026-A00-1-1",  "Y",  "2021-04-23 00:00:00",  "M0AP0175G0A",  "A00",  "OP_NAME",  1,  220,  240,  "PRODUCT_TYPE",  "2021-04-23 00:00:00",  210,  "N",  "LOTTYPE",  "M0AP0175G0A")
print(result[0])
print(result[1])
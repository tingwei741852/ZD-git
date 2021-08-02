def main(array):
  code = ''
  for ele in array:
    
    code+='if not '+ele+' is None:\n'
    code+='  if cnt>0:\n'
    code+='    sql_select+=", %s ' + ele +'\\n"\n'
    code+='    sql_update+=", A.'+ele+'=M.'+ele+'\\n"\n'
    code+='    sql_col+=", '+ele+'\\n"\n'
    code+='    sql_insert+=", M.'+ele+'\\n"\n'
    code+='  else:\n'
    code+='    sql_select+="%s ' + ele +'\\n"\n'
    code+='    sql_update+="A.'+ele+'=M.'+ele+'\\n"\n'
    code+='    sql_col+="'+ele+'\\n"\n'
    code+='    sql_insert+="M.'+ele+'\\n"\n'
    code+='  cnt+=1\n'
  return code

array=['ORDERNO', 'LOT ', 'IS_HOLD ', 'WDATE ', 'PRODUCT_REVISION ', 'OP_NO ', 'OP_NAME', 'LAYER', 'QTY', 'PCSQTY', 'PRODUCT_TYPE', 'ARRIVAL_TIME', 'HODINGTIME', 'IS_ROCKET', 'LOTTYPE', 'PRODUCT_ID', ]
print(main(array))

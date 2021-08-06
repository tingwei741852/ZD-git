def downtime():
    sql = 'SELECT COUNT(*) cnt FROM \n'+\
    '"APS"."APS_SCHEDULE" S INNER JOIN "APS"."A_DOWNTIME" D \n'+\
    'ON S.MACHINE_ID = D.MACHINE_ID \n'+\
    'WHERE D.END_TIME > S.START_TIME \n'+\
    'AND D.START_TIME < S.END_TIME \n'
    return sql

def opelimit():
    sql = 'SELECT COUNT(*) cnt FROM\n'+\
    '"APS"."APS_SCHEDULE" A INNER JOIN "APS"."APS_SCHEDULE" B\n'+\
    'ON A."ORDER_ID" = B."ORDER_ID" \n'+\
    'WHERE\n'+\
    'A. "OPE_ID" <> B. "OPE_ID" AND \n'+\
    'A.END_TIME > B.START_TIME   AND A.START_TIME < B.END_TIME \n'
    return sql

def availabletime():
    sql = 'SELECT COUNT(*) cnt FROM\n'+\
    '"APS"."APS_WO" A INNER JOIN "APS"."APS_SCHEDULE" B\n'+\
    'ON A.WORKNO = B. ORDER_ID\n'+\
    'WHERE B.START_TIME< A. AVAILABLE_TIME \n'
    return sql

def shippingdate():
    sql = 'SELECT \n'+\
    ' A.PRODUCEQTY, \n'+\
    ' A.PRODUCT_ID, \n'+\
    ' A.SHIPPING_DATE, \n'+\
    ' B.SHEEPQTY, \n'+\
    ' (A.PRODUCEQTY-B.SHEEPQTY) DIFF \n'+\
    'FROM( \n'+\
    '  SELECT SUM(A.QTY)PRODUCEQTY,B.PRODUCT_ID,B.SHIPPING_DATE \n'+\
    '  FROM ( \n'+\
    '    SELECT DISTINCT QTY,SHIPPING_DATE,PRODUCT_ID \n'+\
    '    FROM "APS"."APS_SCHEDULE" \n'+\
    '  ) A \n'+\
    '  RIGHT JOIN( \n'+\
    '    SELECT DISTINCT A.PRODUCT_ID,A.SHIPPING_DATE \n'+\
    '    FROM "APS"."S_SHIPPING" A \n'+\
    '  ) B \n'+\
    '  ON A.PRODUCT_ID = B.PRODUCT_ID \n'+\
    '  WHERE A.SHIPPING_DATE<B.SHIPPING_DATE \n'+\
    '  GROUP BY B.PRODUCT_ID,B.SHIPPING_DATE \n'+\
    ')A \n'+\
    'INNER JOIN ( \n'+\
    '  SELECT SUM(B.QTY_SHEET) AS SHEEPQTY,A.PRODUCT_ID,A.SHIPPING_DATE \n'+\
    '  FROM "APS"."S_SHIPPING" A \n'+\
    '  INNER JOIN "APS"."S_SHIPPING" B \n'+\
    '  ON A.PRODUCT_ID = B.PRODUCT_ID \n'+\
    '  WHERE B.SHIPPING_DATE <= A.SHIPPING_DATE \n'+\
    '  GROUP BY A.PRODUCT_ID,A.SHIPPING_DATE \n'+\
    ')B \n'+\
    'ON (A.PRODUCT_ID = B.PRODUCT_ID AND A.SHIPPING_DATE = B.SHIPPING_DATE)'
    return sql

def rocket():
  sql = 'SELECT COUNT(*)CNT FROM( \n'+\
        '  SELECT  \n'+\
        '  A.*, \n'+\
        '  B.IS_ROCKET \n'+\
        '  FROM  \n'+\
        '  "APS"."APS_SCHEDULE" A \n'+\
        '  INNER JOIN "APS"."F_WIP" B \n'+\
        '  ON A.LOT = B.LOT \n'+\
        '  WHERE B.IS_ROCKET = \'Y\' \n'+\
        ')A \n'+\
        'INNER JOIN ( \n'+\
        '  SELECT  \n'+\
        '  A.*, \n'+\
        '  B.IS_ROCKET \n'+\
        '  FROM  \n'+\
        '  "APS"."APS_SCHEDULE" A \n'+\
        '  INNER JOIN "APS"."F_WIP" B \n'+\
        '  ON A.LOT = B.LOT \n'+\
        '  WHERE B.IS_ROCKET = \'N\' \n'+\
        ')B    \n'+\
        'ON A.OPE_ID = B.OPE_ID \n'+\
        'WHERE A.LAYER = B.LAYER \n'+\
        'AND B.ARRIVAL_TIME>A.ARRIVAL_TIME \n'+\
        'AND B.START_TIME<A.START_TIME'
  return sql

def lotcount():
  sql = 'SELECT  \n'+\
  'COUNT(*) CNT \n'+\
  'FROM( \n'+\
  '  SELECT \n'+\
  '  COUNT(*) LOTCNT, \n'+\
  '  GROUP_ID, \n'+\
  '  LOT  \n'+\
  '  FROM( \n'+\
  '    SELECT  \n'+\
  '    A.LOT, \n'+\
  '    A.GROUP_ID \n'+\
  '    FROM \n'+\
  '    ( \n'+\
  '      SELECT  \n'+\
  '      A.*, \n'+\
  '      B.GROUP_ID \n'+\
  '      FROM "APS"."APS_SCHEDULE" A \n'+\
  '      INNER JOIN "APS"."A_EQ" B \n'+\
  '      ON A.MACHINE_ID = B.EQ_ID \n'+\
  '    ) A \n'+\
  '  ) \n'+\
  '  GROUP BY LOT,GROUP_ID \n'+\
  ')A \n'+\
  'INNER JOIN "APS"."A_EQGROUPUSE" B  \n'+\
  'ON A.GROUP_ID = B.GROUP_ID \n'+\
  'WHERE A.LOTCNT < B.MIN_PNL'
  return sql

def safeope():
  sql = 'SELECT COUNT(*) cnt FROM \n'+\
  '"APS"."APS_SCHEDULE" S INNER JOIN "APS"."A_DOWNTIME" D \n'+\
  'ON S.MACHINE_ID = D.MACHINE_ID \n'+\
  'WHERE D.END_TIME > S.ARRIVAL_TIME  \n'+\
  'AND D.START_TIME < S.OUT_TIME \n'+\
  'AND D.MTYPE = \'holiday\' \n'+\
  'AND D.SAFTY = \'0\' \n'
  return sql

def getschedule():
  sql = 'SELECT A.*,B.MAX_WIP \n'+\
  'FROM \n'+\
  'APS_SCHEDULE A \n'+\
  'INNER JOIN \n'+\
  'A_OPELIMIT B \n'+\
  'ON A.OPE_ID = B.OP_NO'
  return sql

def getfixturelimit():
  sql = 'SELECT A.*,B.FIXTURE_QTY FROM APS_SCHEDULE A \n'+\
  'INNER JOIN ( \n'+\
  '  SELECT COUNT(*) FIXTURE_QTY,OPNO,OPLEVEL,PARTNO \n'+\
  '  FROM A_FIXTURE \n'+\
  '  GROUP BY OPNO,OPLEVEL,PARTNO \n'+\
  ') B \n'+\
  'ON A.OPE_ID = B.OPNO AND A.LAYER = B.OPLEVEL AND A.PRODUCT_ID = B.PARTNO \n'
  return sql
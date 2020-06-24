from datetime import datetime, timedelta, time
import pandas as pd
from datetime import datetime
import cx_Oracle
import pandas
import datetime   




def read_query(connection, query, param):
    cursor = connection.cursor()
    try:
        cursor.execute( query , param)
        names = [ x[0] for x in cursor.description]
        rows = cursor.fetchall()
        return pandas.DataFrame( rows, columns=names)
    finally:
        if cursor is not None:
            cursor.close()


def getProdMmgMensalCC(ano1,ano2,centrocusto):
    print(ano1)
    print(ano2)
    print(centrocusto)

    query = """SELECT C.ANO,
       NVL(C.JANEIRO, 0)JANEIRO,
       NVL(C.FEVEREIRO, 0)FEVEREIRO,
       NVL(C.MARCO, 0)MARCO,
       NVL(C.ABRIL, 0)ABRIL,
       NVL(C.MAIO, 0)MAIO,
       NVL(C.JUNHO, 0)JUNHO,
       NVL(C.JULHO, 0)JULHO,
       NVL(C.AGOSTO, 0)AGOSTO,
       NVL(C.SETEMBRO, 0)SETEMBRO,
       NVL(C.OUTUBRO, 0)OUTRUBRO,
       NVL(C.NOVEMBRO, 0)NOVEMBRO,
       NVL(C.DEZEMBRO, 0)DEZEMBRO
  FROM (
SELECT DISTINCT A.ANO, A.MES,
       COUNT(1) OVER (PARTITION BY A.MES) QTD
  FROM (
SELECT SEP.SOLIC_EXAME_PROC_ID,
       TO_CHAR(SEP.DT_EFETIVACAO, 'MM') MES,
        TO_CHAR(SEP.DT_EFETIVACAO, 'RRRR') ANO
  FROM SOLICITACAO_EXAME_PROCEDIMENTO SEP
 WHERE SEP.PRO_ID IN (966,967,968,969,965,14804,20420,38909,51992,60971)
   AND EXTRACT(YEAR FROM SEP.DT_EFETIVACAO ) = """+ano1+"""
   AND SEP.CENTRO_CUSTO_ID = """+centrocusto+""") A
 )

PIVOT(
SUM(QTD)
   FOR MES IN('01' as "JANEIRO",
              '02' as "FEVEREIRO",
              '03' as "MARCO",
              '04' as "ABRIL",
              '05' as "MAIO",
              '06' as "JUNHO",
              '07' as "JULHO",
              '08' as "AGOSTO",
              '09' as "SETEMBRO",
              '10' as "OUTUBRO",
              '11' as "NOVEMBRO",
              '12' as "DEZEMBRO")
)C
UNION ALL

SELECT C.ANO,
       NVL(C.JANEIRO, 0)JANEIRO,
       NVL(C.FEVEREIRO, 0)FEVEREIRO,
       NVL(C.MARCO, 0)MARCO,
       NVL(C.ABRIL, 0)ABRIL,
       NVL(C.MAIO, 0)MAIO,
       NVL(C.JUNHO, 0)JUNHO,
       NVL(C.JULHO, 0)JULHO,
       NVL(C.AGOSTO, 0)AGOSTO,
       NVL(C.SETEMBRO, 0)SETEMBRO,
       NVL(C.OUTUBRO, 0)OUTRUBRO,
       NVL(C.NOVEMBRO, 0)NOVEMBRO,
       NVL(C.DEZEMBRO, 0)DEZEMBRO
  FROM (
SELECT DISTINCT A.ANO, A.MES,
       COUNT(1) OVER (PARTITION BY A.MES) QTD
  FROM (
SELECT SEP.SOLIC_EXAME_PROC_ID,
       TO_CHAR(SEP.DT_EFETIVACAO, 'MM') MES,
        TO_CHAR(SEP.DT_EFETIVACAO, 'RRRR') ANO
  FROM SOLICITACAO_EXAME_PROCEDIMENTO SEP
 WHERE SEP.PRO_ID IN (966,967,968,969,965,14804,20420,38909,51992,60971)
   AND EXTRACT(YEAR FROM SEP.DT_EFETIVACAO ) = """+ano2+"""
   AND SEP.CENTRO_CUSTO_ID = """+centrocusto+""") A
 )

PIVOT(
SUM(QTD)
   FOR MES IN('01' as "JANEIRO",
              '02' as "FEVEREIRO",
              '03' as "MARCO",
              '04' as "ABRIL",
              '05' as "MAIO",
              '06' as "JUNHO",
              '07' as "JULHO",
              '08' as "AGOSTO",
              '09' as "SETEMBRO",
              '10' as "OUTUBRO",
              '11' as "NOVEMBRO",
              '12' as "DEZEMBRO")
)C



                
                        """




    #param = (cpf, p_nome, nascimento)
    param = ()

    #print(param)


    c = cx_Oracle.connect('prevencao/prevencao@piodb-scan.pioxii.com.br/hcb', encoding='UTF-8')
    cursor = c.cursor() # cria um cursor
    result = read_query(c, query, param)

    #print(result)
    cursor.close()
    c.close()
  

    
    if (result.empty):
        r = [] 
        
    else:
        r = result.to_dict(orient='records')
    
        

    return r


def getProdMmgSemanaCC(ano, mes, centrocusto):

    query = """
        SELECT 'SEMANA '||ROW_NUMBER() OVER (PARTITION BY B.MES ORDER BY B.SEMANA) ||'  ('||B.QTD_DIAS||')' SEMANA_DESC,
              B.*
        FROM (
        SELECT DISTINCT A.ANO,
              A.MES,
              A.SEMANA,
              (SELECT count(1)
                        FROM (SELECT dia
                                    ,TO_CHAR(dia, 'iw') semana
                                    ,TO_CHAR(dia, 'd') dia_semana
                                FROM (SELECT data_inicial + LEVEL - 1 dia
                                        FROM (SELECT  TO_DATE('01/01/"""+ano+"""', 'DD/MM/RRRR') data_inicial
                                                FROM dual)
                                      CONNECT BY LEVEL <= 365 + 1))
                      WHERE semana = a.semana) QTD_DIAS,
              COUNT(1) OVER (PARTITION BY A.ANO, A.SEMANA) QTD_SEMANA
          FROM (
        SELECT SEP.SOLIC_EXAME_PROC_ID,
              TO_CHAR(SEP.DT_EFETIVACAO, 'MM') MES,
              TO_CHAR(SEP.DT_EFETIVACAO, 'RRRR') ANO,
              TO_CHAR(SEP.DT_EFETIVACAO, 'iw') SEMANA
          FROM SOLICITACAO_EXAME_PROCEDIMENTO SEP
        WHERE SEP.PRO_ID IN (966,967,968,969,965,14804,20420,38909,51992,60971)
          AND EXTRACT(YEAR FROM SEP.DT_EFETIVACAO ) = """+ano+"""
          AND EXTRACT(MONTH FROM SEP.DT_EFETIVACAO) = """+mes+"""
          AND SEP.CENTRO_CUSTO_ID = """+centrocusto+"""
          )A)B
          """
    param = ()

    #print(param)


    c = cx_Oracle.connect('prevencao/prevencao@piodb-scan.pioxii.com.br/hcb', encoding='UTF-8')
    cursor = c.cursor() # cria um cursor
    result = read_query(c, query, param)

    #print(result)
    cursor.close()
    c.close()
  

    
    if (result.empty):
        r = [] 
        
    else:
        r = result.to_dict(orient='records')
    
        

    return r


import pymysql
import pandas as pd

# 创建数据库连接
conn = pymysql.connect(host='localhost', user='root', password='ReallySweet@0619', db='test')

# 执行 SQL 查询
sql = """
SELECT 
    SUBSTRING_INDEX(SUBSTRING_INDEX(domain, '/', 3), '://', -1) as domain_name, 
    COUNT(*) as num 
FROM 
    weburl 
WHERE 
    domain LIKE 'http%'
GROUP BY 
    domain_name 
ORDER BY 
    num DESC
"""

df = pd.read_sql_query(sql, conn)

# 将 DataFrame 导出为 Excel 文件
df.to_excel('summary.xlsx', index=False)

# 关闭数据库连接
conn.close()

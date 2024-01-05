import sys
import sqlite3
import pandas as pd

def main()->None:
    con = sqlite3.connect('db/ww-price.db')
    wb = pd.read_excel(
        r'C:\Users\I340544\OneDrive - SAP SE\400-PA AD & Integration\100-Customer Engagements\Woolworths (ANZ)\GenAI Bot\prices-for-upload_with_desc.xlsx', 
        sheet_name=None, 
        header=[0,1])

    for sheet in wb:
        wb[sheet].to_sql(sheet,con,index=False)
    con.commit()
    con.close()

if __name__ == '__main__':
    sys.exit(main())


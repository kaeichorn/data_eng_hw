#!/usr/bin/python3
import pandas as pd
import glob
import psycopg2
import os

#connect to db
con = psycopg2.connect(host="localhost",database="mypgdb",user="postgres",password="password",port="5432")

cur=con.cursor()

#create tables
cur.execute("""  
        CREATE TABLE marketing(  
       event_id text,  
       phone_id text,  
       ad_id text,  
       provider varchar,  
       placement text,  
       length decimal,  
       event_ts timestamp, 
       PRIMARY KEY (event_id,phone_id))  
       """) 

#create tables
cur.execute("""  
            CREATE TABLE "user"(  
            event_id text,  
           user_id text,  
            phone_id text,  
            property text,  
           value text,  
            event_ts timestamp, 
          PRIMARY KEY (event_id,phone_id))""")


#clean and load data
marketing_data = pd.concat([pd.read_csv(f) for f in glob.glob('dataset/marketing_*.csv')], ignore_index = True)
outdir='./dataset/clean_data/'
#create file directory
if not os.path.exists(outdir):
	os.mkdir(outdir)
marketing_filename=os.path.join(outdir,'marketing.csv')
#exclude data that is missing id's
marketing_data[~marketing_data['event_id'].isna()].to_csv(marketing_filename,index=False)

try: 
	with open(marketing_filename,'r') as f: 
		next(f) 
		cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format('marketing'), f) 
		con.commit() 
except Exception as e: 
	print("Error:{}".format(str(e))) 
	con.commit()

user_data = pd.concat([pd.read_csv(f) for f in glob.glob('dataset/user_*.csv')], ignore_index = True)
user_filename=os.path.join(outdir,'user.csv')
#exclude data that is missing id's
user_data[~((user_data['event_id'].isna()) | (user_data['phone_id'].isna()))].to_csv(user_filename,index=False)

try:
        with open(user_filename,'r') as f:
                next(f)
                cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format('"user"'), f)
                con.commit()
except Exception as e:
        print("Error:{}".format(str(e)))
        con.commit()

con.commit()

cur.close()

con.close()




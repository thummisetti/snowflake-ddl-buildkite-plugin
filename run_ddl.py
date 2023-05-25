import snowflake.connector


# SNOWFLAKE_ACCOUNT: rippling
# SNOWFLAKE_USER: PROD_RIPPLING_GIT_USER
# SNOWFLAKE_PASSWORD: D9aLYrS@829H
# SNOWFLAKE_DB: PROD_RIPPLING_DWH

conn = snowflake.connector.connect(user='USER_NAME',
                                     host='HOST_ADDRESS',
                                     account='ACCOUNT_ADDRESS',
                                     password ='PASSWORD',
                                     database='DB_NAME',     
                                     warehouse='WH_NAME',
                                     autocommit=True)


order_of_operations = ['tables', 'views', 'udfs', 'masks']

files = ordered_list_of_files


for file in files:
	if str(file).startswith('definition') or str(file).startswith('incremental'):
		with open(file, "r") as f:
			ddl_query = f.read()
		cursor = conn.cursor()
		cursor.execute(ddl_query)
		logging.info(cursor.fetchone()[0])


conn.close()


if __name__ == "__main__":
  main()
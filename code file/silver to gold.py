# Databricks notebook source
# MAGIC %md
# MAGIC ## Let's Start with data cleaning in this we will change the ColumnName to Column_Name, also we will add and extra feature called Total_Amount in sales facttable

# COMMAND ----------

dbutils.fs.ls('/mnt/silver/SalesLT/')

# COMMAND ----------

dbutils.fs.ls('/mnt/gold/')

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls('/mnt/silver/SalesLT/'):
    table_name.append(i.name.split('/')[0])

# COMMAND ----------

table_name

# COMMAND ----------

#  List of table names to process
# table_names = ['SalesOrderDetail', 'SalesOrderHeader', 'Product', 'ProductCategory', 'Customer', 'CustomerAddress', 'Address', 'ProductModel', 'ProductDescription', 'ProductModelProductDescription']

# Dictionary to store DataFrames
dfs = {}

# Load each table into a DataFrame and show the schema
for name in table_name:
    path = f'/mnt/silver/SalesLT/{name}'
    print(f'Loading table: {name}')
    df = spark.read.format('delta').load(path)
    dfs[name] = df
    print(f'Schema for {name}:')
    df.printSchema()
    print()

# Show the first few rows of each DataFrame
for name, df in dfs.items():
    print(f'First few rows for {name}:')
    df.show(5)
    print()

# COMMAND ----------

# # Calculate the average unit price and fill missing values
# avg_price = df_sales_order_detail.select(mean(col('UnitPrice')).cast("float")).collect()[0][0]
# df_sales_order_detail = df_sales_order_detail.na.fill({'UnitPrice': avg_price})

# # Create TotalAmount column
# df_sales_order_detail = df_sales_order_detail.withColumn('TotalAmount', col('OrderQty') * col('UnitPrice'))

# # Show the transformed DataFrame schema and the first few rows
# df_sales_order_detail.printSchema()
# df_sales_order_detail.show(10)


# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import mean, col

# Initialize Spark session
spark = SparkSession.builder.appName('DataCleaning').getOrCreate()

# List of table names to process
table_names = ['SalesOrderDetail', 'SalesOrderHeader', 'Product', 'ProductCategory', 'Customer', 'CustomerAddress', 'Address', 'ProductModel', 'ProductDescription', 'ProductModelProductDescription']

for name in table_names:
    path = '/mnt/silver/SalesLT/' + name
    print(f'Processing table: {name}')
    df = spark.read.format('delta').load(path)

    # Get the list of column names
    column_names = df.columns
    
    # Apply specific data transformations
    if name == 'SalesOrderDetail':
        avg_price = df.select(mean(col('unitprice')).cast("float")).collect()[0][0]
        df = df.na.fill({'unitprice': avg_price})
        df = df.withColumn('unitprice', col('unitprice').cast('float'))
        df = df.withColumn('total_amount', col('orderqty') * col('unitprice'))

    if name == 'SalesOrderHeader':
        df = df.dropDuplicates(['salesorderid'])

    for old_col_name in column_names:
        # Converting column name from CamelCase to snake_case format
        new_col_name = "".join(["_" + char if char.isupper() and (i != 0 and not old_col_name[i-1].isupper()) else char for i, char in enumerate(old_col_name)]).lstrip("_")
        
        # Change the column name
        df = df.withColumnRenamed(old_col_name, new_col_name)

    # Save the transformed data to the gold layer
    output_path = '/mnt/gold/SalesLT/' + name + '/'
    df.write.format('delta').mode('overwrite').save(output_path)

print("Data transformation and loading to gold layer completed for all tables.")


# COMMAND ----------

# MAGIC %md
# MAGIC ### Since we have done all the transformation we can load the data to synapse

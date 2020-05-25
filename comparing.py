import datetime
# import datacompy
from pyspark.sql import Row

# This example assumes you have a SparkSession named "spark" in your environment, as you
# do when running `pyspark` from the terminal or in a Databricks notebook (Spark v2.0 and higher)

data1 = [
    Row(acct_id=10000001234, dollar_amt=123.45, name='George Maharis', float_fld=14530.1555,
        date_fld=datetime.date(2017, 1, 1)),
    Row(acct_id=10000001235, dollar_amt=0.45, name='Michael Bluth', float_fld=1.0,
        date_fld=datetime.date(2017, 1, 1)),
    Row(acct_id=10000001236, dollar_amt=1345.0, name='George Bluth', float_fld=None,
        date_fld=datetime.date(2017, 1, 1)),
    Row(acct_id=10000001237, dollar_amt=123456.0, name='Bob Loblaw', float_fld=345.12,
        date_fld=datetime.date(2017, 1, 1)),
    Row(acct_id=10000001239, dollar_amt=1.05, name='Lucille Bluth', float_fld=None,
        date_fld=datetime.date(2017, 1, 1))
]

data2 = [
    Row(acct_id=10000001234, dollar_amt=123.4, name='George Michael Bluth', float_fld=14530.155),
    Row(acct_id=10000001235, dollar_amt=0.45, name='Michael Bluth', float_fld=None),
    Row(acct_id=10000001236, dollar_amt=1345.0, name='George Bluth', float_fld=1.0),
    Row(acct_id=10000001237, dollar_amt=123456.0, name='Robert Loblaw', float_fld=345.12),
    Row(acct_id=10000001238, dollar_amt=1.05, name='Loose Seal Bluth', float_fld=111.0)
]

base_df = spark.createDataFrame(data1)
compare_df = spark.createDataFrame(data2)

comparison = datacompy.SparkCompare(spark, base_df, compare_df, join_columns=['acct_id'])
print(comparison)

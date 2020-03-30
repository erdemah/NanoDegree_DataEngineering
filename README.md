This project includes data modelling and an ETL (Extract, Transform, Load) job for song data and log data. The purpose of the project
is to analyze data easily coming from the new music streaming app called Sparkify. Any insight from such analyses is important to businesses
which can help them understand their customers better, provide better services. To make data analysis and reporting easier, the data are 
pipelined through a Postgres database. During this job, the Postgres database model has been created using a star schema with a total of 
5 tables - 1 Fact, 4 dimensional tables.

sql_queries.py: PostgreSQL drop, create, insert tables. Data modelling occurs here.
create_tables.py: A wrapper built on top sql_queries.py to make the database console commands easier.
test.ipynb: Every time you manipulate the database, run this file to check if the code is doing what is supposed to be doing.
            Restart Jupyter Kernel for cleanup in every run.
etl.ipynb: A prototype of etl.py
etl.py: Data is extracted, transformed and loaded into PostgreSQL database.

Build Environment:

Python 3.7
PostgreSQL 12.2
# Databricks notebook source


###workflow for nunning ochestration of workloads
####supports BI and SQL workloads on Delta lake
####intergration with Bi tools
####direct querying of data
####natural language to write AI queries
####DI engine support natural language to write sql queries
####AI driven serverless computing - cost serving and peak perfoming speeds
####AI supporting debugging
####unity catalogue- unified governance and AI
####unity catalog supoort data leneage, access controls and governance
####delta lake - optimised storage layer  provides foundation for storing data and tables in the databricks data intelligence platform
####extends parquet datafiles with transaction log for ACID transactions and scalable metadata handling



# COMMAND ----------

# MAGIC %md
# MAGIC repos allow integration with gi
# MAGIC leads to maintanace of immutable recod of changes/ history
# MAGIC -repos provide external intergration points to suppot a CI/CD pipeline
# MAGIC -Dbricks suports Azure, Devops, Bitbucket, Github and Gitlab
# MAGIC -bo support of privates gits
# MAGIC - clone repository: create a local working copy of a remote repository
# MAGIC -Pull: synhcronise upstream changes with local copy
# MAGIC -create: create a new item to your local copy
# MAGIC -move- move or rename existing items of your local copy
# MAGIC -commit and push to synhcronise local changes with your local copyu
# MAGIC -create branch- create code base without impact other branches in the repository
# MAGIC -avoid interfering with the main. 

# COMMAND ----------

# MAGIC %md
# MAGIC #basic compte structures
# MAGIC
# MAGIC ##Clusters
# MAGIC -made up of one or more VM instances
# MAGIC - distributes workloads accross workers
# MAGIC
# MAGIC - Driver coordinates activites of executors
# MAGIC - Workers run tasts composing a spark job
# MAGIC
# MAGIC #Three types of compute
# MAGIC - All purpose clusters:  clusters for interactive development
# MAGIC - job clusters: automating workloads
# MAGIC -Sql Warehouses: compute to run DBSQL queries and dashboards
# MAGIC
# MAGIC #houw to create all purpose clusters
# MAGIC -through interactive notebooks
# MAGIC -through workspace
# MAGIC -programmatical using the commmand prompt line interface or rest API
# MAGIC Job cluster
# MAGIC
# MAGIC #job clusters
# MAGIC -running automated jobs
# MAGIC -job scheduler creates new job cluster and terminates when job is complete
# MAGIC -cannot restart a job cluster
# MAGIC
# MAGIC
# MAGIC #SQL warehouses
# MAGIC
# MAGIC -DBSQL queries and updating dashboards
# MAGIC -single nodes - low cost single instance for single node machine learning workloads and lightweight exploratory analysis
# MAGIC Mlti-node-default for workloads developed in any supported language -  VM instance for the driver and at least one additional instance for workers
# MAGIC
# MAGIC -must use appropreate runtime for each one
# MAGIC DB runtime has essential software components eg apache spark , machine learning workloads, 
# MAGIC
# MAGIC Photon:  The next generation engine on Databricks DI platform 
# MAGIC    - cheaper and faster
# MAGIC    - buildt for all use cases
# MAGIC    - No code changes- can be used seemlessly with db runtime without any code changes
# MAGIC    - data ingestion, ETL and streaming, data science and interactive queries directly on your datalake
# MAGIC
# MAGIC
# MAGIC #daabricks sql warehouses 
# MAGIC   - to execute queries and business applications at scale
# MAGIC   
# MAGIC   -Classic SQL warehouses:
# MAGIC      - compute resources run in your cloud account
# MAGIC      -takes several minutes to start-up
# MAGIC      -classic compute plane hasnatural isolation
# MAGIC      -natural isolation
# MAGIC      -exploratory SQL workloads
# MAGIC      -Mandates that uoui contrl your own resources
# MAGIC      -manage own resources including launching and cleaning clusters
# MAGIC      -more control but more effort 
# MAGIC
# MAGIC   - Severless SQL Warehouse
# MAGIC      - Compute resources run in a compute later within your databricks account
# MAGIC      - rapid startup time 2-6secs
# MAGIC      runs withing the network boundary in the workspace
# MAGIC      - Best for high-concurrenty BI SQL, and DSML using SQL , data science and machine learning
# MAGIC      -FUlly managed by Databricks
# MAGIC      -privides instant, elastic and zero management compute
# MAGIC      -high performance high concurrency workloads
# MAGIC      - auro stop feature setting
# MAGIC      
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------



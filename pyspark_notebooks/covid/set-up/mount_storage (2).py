# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers
# MAGIC 1. raw
# MAGIC 2. processed
# MAGIC 3. lookup

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

client_id = dbutils.secrets.get(scope = 'clientid',key = 'clientId')
directory_id = dbutils.secrets.get(scope = 'clientid',key = 'directoryId')
client_secret = dbutils.secrets.get(scope = 'clientid',key = 'clientsecret')

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": client_id,
          "fs.azure.account.oauth2.client.secret": client_secret,
          "fs.azure.account.oauth2.client.endpoint": f"https://login.microsoftonline.com/{directory_id}/oauth2/token"}


# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://raw@devcicddemodl9.dfs.core.windows.net/",
  mount_point = "/mnt/devcicddemodl9/raw",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the processed container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://processed@devcicddemodl9.dfs.core.windows.net/",
  mount_point = "/mnt/devcicddemodl9/processed",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the lookup container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://lookup@devcicddemodl9.dfs.core.windows.net/",
  mount_point = "/mnt/devcicddemodl9/lookup",
  extra_configs = configs)

# COMMAND ----------

spark.conf.get("spark.databricks.clusterUsageTags.clusterName")

# COMMAND ----------

spark.conf.get("spark.databricks.clusterUsageTags.clusterId")
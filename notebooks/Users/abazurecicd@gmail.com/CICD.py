# Databricks notebook source
spark.conf.set(
  "fs.azure.account.key.kronosdatabricks.dfs.core.windows.net",
  "ChpXel84Sor4ZZ6N9DO+dP/H8JxtCFDkCGhYuKm0SsmWkI3JLo03j7MTaSJAfA6GBOAWvRyBAbkwW95uohBbrg=="
)

# COMMAND ----------

dbutils.fs.ls("abfss://product@kronosdatabricks.dfs.core.windows.net")
# -*- coding: utf-8 -*-
"""KDM_ICP4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15_ECqAhB_cwoHwQtEEez3Bsf7QdT3HTj

**1 ->` Setting up PySpark in Colab**

Spark is written in the Scala programming language and requires the Java Virtual Machine (JVM) to run. Therefore, I'm downloading Java in the first step
"""

!sudo apt-get update
!apt-get install openjdk-8-jdk-headless -qq > /dev/null

"""2.a -> Next, I'm installing Apache Spark 3.0.1 with Hadoop 2.7"""

!wget -q https://www-us.apache.org/dist/spark/spark-3.0.1/spark-3.0.1-bin-hadoop2.7.tgz

"""2.b -> Now, unzip that folder that we just downloaded."""

!tar xf spark-3.0.1-bin-hadoop2.7.tgz

"""3 -> Installing the findspark library. It will locate Spark on the system and import it as a regular library."""

!pip install -q findspark

"""4 -> We have done with all the Installations part. Now, I'm setting the environmenta path. This will enable us to run Pyspark in the Colab environment."""

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.0.1-bin-hadoop2.7"

"""5 -> We need to locate Spark in the system."""

import findspark
findspark.init() 
findspark.find()  # This will provide the location where Spark is installed

"""Now, I'm importing the SparkSession from pyspark.sql and creating a SparkSession, which is the entry point to Spark.

We can assign the name to session using appName
"""

from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

spark  = SparkSession.builder\
                  .master("local")\
                  .appName("KDM")\
                  .config('spark.ui.port', '4050')\
                  .getOrCreate()

spark  # printing the SparkSession variable.

"""Now, load the dataset. For that I'm using the **.csv** module.

And passing the inferSchema parameter = true; it will enable the Spark to automatically determine the data type for each column but it has to go over the data once. This is optional parameter. If we didn't set inderShema to True, then are the tokens are considered as **string.**
"""

data = spark.read.csv("/content/data.csv", header=True, inferSchema= True)
data.printSchema()

"""**Performing Actions on the data**

**Operation 1: Printing all the Column names**
"""

data.columns #This will print all the column names present in the input file.

"""**Operation 2: Printing only the 'n' number of rows using limit function**"""

data.limit(3).collect()  # Limits the result count to the number specified.

"""**Operation 3: Returns the first row**"""

data.first() # It will return first row as output

"""**Performing Transformations on the data**

**Operation 1: Grouping the data**
"""

op1 = data.groupBy('gender').count() # It will group the data based on "Gender" and display the count of each
op1.show()

"""**Operation 2: Ordering the data**"""

op2 = data.orderBy('InternetService').take(4) # It will order the data based on "InternetService"
op2

"""**Operation 3: Filter the rows using the given condition.**"""

data.where(data.tenure == 34).collect() # It will print all the rows where tenure is equal to 34
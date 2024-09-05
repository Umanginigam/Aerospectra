# -*- coding: utf-8 -*-
"""Big Data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ex7L9HLGA0DXepcVVWpAOUV7-3ZnBDZx
"""

!apt-get update
!apt-get install openjdk-8-jdk-headless -qq > /dev/null

!wget http://apache.mirror.digitalpacific.com.au/hadoop/common/hadoop-x.y.z/hadoop-x.y.z.tar.gz

!wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz
!tar -xzf hadoop-3.3.6.tar.gz

import os

os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["HADOOP_HOME"] = "/content/hadoop-3.3.6"
os.environ["PATH"] = os.environ["HADOOP_HOME"] + "/bin:" + os.environ["JAVA_HOME"] + "/bin:" + os.environ["PATH"]

# Verify Hadoop version to check if it's installed correctly
!hadoop version

!jps

def mapper(line):
    words = line.strip().split()
    for word in words:
        yield (word, 1)

def reducer(mapped_data):
    word_counts = {}
    for word, count in mapped_data:
        if word in word_counts:
            word_counts[word] += count
        else:
            word_counts[word] = count
    return word_counts

# Step 3.1: Read the input file
with open('files.txt', 'r') as file:
    lines = file.readlines()

# Step 3.2: Apply the mapper to each line
mapped_data = []
for line in lines:
    mapped_data.extend(mapper(line))

# Step 3.3: Apply the reducer to the mapped data
word_counts = reducer(mapped_data)

# Step 3.4: Print the results
for word, count in word_counts.items():
    print(f"{word}: {count}")

!hdfs dfs -ls /

#Assignment 2
!hdfs dfs -ls /content/files.txt

!hdfs dfs -ls -R  /content/files.txt
!hdfs dfs -mkdir /content/files
!hdfs dfs -mkdir -p /content/files
!hdfs dfs -put /content/files.txt /content/files

!hdfs dfs -copyFromLocal /content/files.txt /content/files

!hdfs dfs -get /content/files /content/files.txt

!hdfs dfs -copyToLocal /content/files /content/files.txt

!hdfs dfs -cat /content/files.txt

!hdfs dfs -rm /content/files.txt

!hdfs dfs -rm -r /content/files

!hdfs dfs -rm -skipTrash /content/files.txt

!hdfs dfs -mv /content/files.txt /content/filess

!hdfs dfs -cp /content/files.txt /content/filess

!hdfs dfs -appendToFile /content/files.txt /content/files

!hdfs dfs -tail /content/files.txt

!hdfs dfs -head /content/files.txt

!hdfs dfs -text /content/files.txt

!sudo useradd newowner
!sudo groupadd newgroup

!hdfs dfs -chmod 755 /content/files.txt
!hdfs dfs -chown newowner:newgroup /content/files.txt
!hdfs dfs -chgrp newgroup /content/files.txt

!hdfs dfs -du  /content/files.txt
!hdfs dfs -du -s /content/files.txt
!hdfs dfs -du -h /content/files.txt
!hdfs dfsadmin -report

!hdfs namenode
!hdfs namenode -format

# Provides a detailed report on the HDFS, including the status of the NameNode, DataNodes, and storage capacity
!hdfs dfsadmin -report

# Saves the current NameNode metadata (such as block locations) to a file
!hdfs dfsadmin -metasave /content/files.txt
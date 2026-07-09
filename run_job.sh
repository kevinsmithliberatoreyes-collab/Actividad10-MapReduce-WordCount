#!/bin/bash
# Ejecución del job utilizando la utilidad de Hadoop Streaming
hadoop jar /usr/lib/hadoop/hadoop-streaming.jar \
  -input /user/hdfs/entrada/*.txt \
  -output /user/hdfs/salida_wordcount \
  -mapper "python3 mapper.py" \
  -reducer "python3 reducer.py" \
  -file mapper.py \
  -file reducer.py

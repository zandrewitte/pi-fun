#!/usr/bin/env bash
declare -a arr=("test-topic1" "test-topic2" "test-topic3")

for i in "${arr[@]}"
do
   kafka-topics --create --zookeeper localhost:2181 --replication-factor 3 --partitions 1 --topic $i
done


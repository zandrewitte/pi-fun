#!/usr/bin/env bash
zookeeper=$1
replication_factor=$2
partitions=$3
topics=$4

for i in $(echo ${topics} | sed "s/,/ /g")
do
    kafka-topics --create --zookeeper ${zookeeper} --replication-factor ${replication_factor} --partitions ${partitions} --topic ${i}
done

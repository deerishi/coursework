#! /bin/bash
i=1
while [ $i -lt 2 ] ; do
    git add . 
    git commit -m "adding files"
    git push
    sleep 20m
done

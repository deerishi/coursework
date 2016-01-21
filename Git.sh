#! /bin/bash
i=1
while [ $i -lt 2 ] ; do
    git add . --ignore-removal
    git commit -m "adding files"
    git push
    sleep 10
done

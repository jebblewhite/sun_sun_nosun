for f in crier widow landowner herbalist innkeeper doctor alderman butcher 
do
    for i in {1..9}
    do
    echo -e "label ${f}scene${i}: 
return" > "scenes/${f}scene${i}.rpy"
    done
done
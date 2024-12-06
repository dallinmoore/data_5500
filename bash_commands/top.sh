for i in {1..10}; 
do top -b -n 1 > top$i.txt && sleep 10; 
done
n=$1

for (( i=1; i<=n; ++i))
do
  python gen_testcases.py

  python bruteforce.py < testcases.txt > brute_out.txt
  python optimal.py < testcases.txt > optimal_out.txt


    if [[ $(diff brute_out.txt optimal_out.txt) ]]
    then
      
      echo "$(diff -Z brute_out.txt optimal_out.txt)" > difference_out.txt
      
      echo "Difference reported in file difference_out.txt"
      echo "----------------------------------------------"
      echo "You can find the testcase where your optimal solution failed in testcases.txt"
      echo "and their respective outputs in brute out.txt and optimal_out.txt"

      break
    else
     echo "AC on super-test #i"
    fi
done

echo "------------Testing done------------"
#!/usr/bin/bash

## Takes apart a canvas download and processes each 
## student's assignment
##
## noynaert
## September 2021
##
## Written for hmwk01
## Must be in the directory with student files
## and data.*.txt files

for f in *.py; do

   #get student name
   echo "Processing $f"
   student=$(echo $f | cut -d _ -f 1)

   #Get python file name
   jName=${f##*_}
   #echo $jName
   
   #Does the directory exist?  If so, remove
   if [ -d $student ]; then
      rm -r $student
   fi

   #make dir and copy file file
   mkdir $student
   cp $f $student
    
   #go to the directory and operate on the file(s)
   cd $student
   echo "STUDENT IS $student"
   #rename the file
   for p in *.py ;do
      mv $p ${p##*_}
   done

   #start out.txt with source code
   for p in *.py 
   do
       pr -n -h "$student $p" $p > out.txt

      python3 -m py_compile $p &>> out.txt
      if [ $? -eq 0 ]; then
         cowsay "No Syntax Errors Found!  Great!!!" >> out.txt
         for data in ../data*.txt; do
            echo "------------------------------ input $data -----------------------------" >> out.txt
            echo "Data is $(cat $data)" >> out.txt
            echo >> out.txt
            
            
              python3 $p < $data &>> out.txt
              if [ $? -ne 0 ]; then
                 cowsay -d "Run aborted" >> out.txt
              fi
              echo >> out.txt
            
         done
      else
         cowsay -d "Sytax Error Found" >> out.txt
          cowsay -d "Sytax Error Found"
      fi
   done
   
   echo NOTE THAT THE LAST DATASET SHOULD HAVE ENDEDED IN AN ERROR >> out.txt
   echo BECAUSE THE DATA FILE CONTAINED TEXT, NOT A NUMBER.  >> out.txt

   if [ -d __pycache__ ] ; then
     rm -r __pycache__
   fi 

   # cowsay -f /home/noynaert/cowsay-files/cows/ackbar.cow  "IT'S A TRAP!  The last run should have ended in an error because the input was text, not a number." >> out.txt


   # Go back to parent
   cd ..

   sleep 1
   

done

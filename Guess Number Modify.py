import time
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str);
guess = 18
count = 1
loop  = 0
loops = 5
print("\n")
print("__________________PYTHON GAME________________________\n")
while(loop<5) :
          loops = loops-1
          loop = loop+1
         
          print("\n")
          num = int(input("Guess Number = "))
          print("\n")          
          if(num==18):
                     print("YOU GUESSED CORRECT ✅ ")
                     print("NO. OF GUESSES = ",count)
                     print("!!!____YOU WON____!!!")
                     break 

          elif(num!= 18):
                        if(num>18):
                                  print(" GUESS IS WRONG ❌ \n ACTUALLY MY NUMBER IS SMALLER \n")
                                  count = count + 1
                                  print("_________________________")
                                  print("LIVES REMAIN =>> ",loops)
                                  print("^^^^^^^^^^^^^^^^^^^^^^^^^")
                                  
                        if(num<18):
                                  print(" GUESS IS WRONG ❌ \n ACTUALLY MY NUMBER IS GREATER \n")   
                                  count = count + 1
                                  print("_________________________")
                                  print("LIVES REMAIN =>> ",loops)
                                  print("^^^^^^^^^^^^^^^^^^^^^^^^^")                                  
                                  continue 
          else:
               print(" Enter Valid input \n")
               continue

if(loops==0): 
            print(".:.:.:.:.:.:.:.:..:LIVES OVER:.:.:.:.:.:.:.:.:.:.:.")              
            print("___________________TRY AGAIN_______________________")
else:
    print("<< 6527 THANKYOU 6527 >>")            
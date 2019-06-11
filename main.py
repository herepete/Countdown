#!/usr/bin/python3.7
import random
import os

#use argparse and accept inputs (useful for testing rather than hard coding)

import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-n", help="Hardcode numbers to use they need to be seperated by commas i.e -n 1,3,5,7,25,50")
parser.add_argument("-t", help="Hardcode target i.e -t 300")
parser.add_argument("-v", help="Verbose output 1 is on. i.e -v 1")

args= parser.parse_args()
npassed=0
verbose_output=0

rv=0


if args.n:

    #messey work but convert from parameter to dict to string to list :(
    npassed=1
    ninput=vars(args) #convert to dict

    #[pdw@g4 countdown]$ ./fixing.py -n 1,2,3,4 -t 500
    #ninput (Pdb) ninput
    #{'n': '1,2,3,4', 't': '500'}
    
    ninputlist=[]
    l_our_large_numbers=[]
    l_our_small_numbers=[]

    for key,val in ninput.items():    
        if key=="n":
            list1=val.split(',')
            for i in list1:
                if int(i) > 10:
                    l_our_large_numbers.append(i)
                else:
                    l_our_small_numbers.append(i)
        if key=="t":
            l_target=int(val)
        if key=="v" and val=="1":
        # with no parameter passed you still get an empty parameter
        # [pdw@g4 countdown]$ ./fixing.py -n 1,2,3,4,25,50 -t 500
        #(Pdb) ninput
        #{'n': '1,2,3,4,25,50', 't': '500', 'v': None}

            verbose_output=1
            

from itertools import permutations
from itertools import combinations_with_replacement 
from itertools import product

os.system('clear')

large_numbers=2 # max allowed 4 min 0
small_numbers=4 # 6 - large number
target_to_hit=0
our_large_numbers=[]
our_small_numbers=[]

global nearest_answer
global nearest_solution

nearest_answer=999999999999
nearest_solution=99999999999


def reversepolishnotation(input1):
    # using Reverse Polish notation
 
    stack = []
 
    for val in input1.split(' '):
        if val in ['-', '+', '*', '/']:
            op1 = stack.pop()
            op2 = stack.pop()
            if op2 > op1:
                if val=='-': result = op2 - op1
            else:
                if val=='-': result = op1 - op2
            if val=='+': result = op2 + op1
            if val=='*': result = op2 * op1
            try:
                if val=='/':
                    check_left_over = op2 % op1
                    if check_left_over==0:
                        result = op2 / op1
                        result = int(result)
                    else:
                        result=999999999999 
            except:
                #catching divide by 0 errors
                result=999999999999 
            stack.append(result)
        else:
            try:
                stack.append(int(val))
            except Exception as e:
                print(e)
                breakpoint()
 
    return stack.pop()

def pick_numbers(smalln,largen):

    #this function chooses the user x large nums and y small nums and a target to hit
    #using random to help select the numbers

    if npassed==1:
        selected_large_numbers=l_our_large_numbers
        selected_small_numbers= l_our_small_numbers
        target=l_target
        return (target,selected_large_numbers,selected_small_numbers)

    else:
        large_nums=[ "25" , "50" , "75" , "100" ]
        small_nums=["1" , "1" , "2" , "2" , "3" , "3" , "4" , "4" , "5" , "5" , "6" , "6" , "7" , "7" , "8" , "8" , "9" , "9" , "10" , "10" ]

        selected_large_numbers=[]
        selected_small_numbers=[]
    
        target=random.randint(100,999)
        for i in range(largen):
            lnc=random.choice(large_nums)
            selected_large_numbers.append(lnc)
            large_nums.remove(lnc)

        for i in range(smalln):
            snc=random.choice(small_nums)
            selected_small_numbers.append(snc)
            small_nums.remove(snc)
        return (target,selected_large_numbers,selected_small_numbers)

def hownear(target,answer,formula):

    global nearest_answer
    global nearest_solution

    if int(target) == int(answer):
        print ("Woop")
        nearest_answer=answer
        nearest_solution=formula
        return (1)
    else:
        distance=abs(target-answer)
        if distance < abs(nearest_answer-target):
            nearest_answer=answer
            nearest_solution=formula
        return (0)

def make_formula_more_readable(nearest_solution):


    # data in format 
        #{'nearest_solution': '100 5 7 50 4 6 - / * * +'}
    nearest_solution_list=nearest_solution.split(" ")

    digit_solution=[]
    symbol_solution=[]
    for i in nearest_solution_list:
        if i.isdigit():
            digit_solution.append(i)
        else:
            symbol_solution.append(i)

    # data in format:
        # nearest_solution_list': ['100', '5', '7', '50', '4', '6', '-', '/', '*', '*', '+']
        #digit_solution: ['100', '5', '7', '50', '4', '6']
        #symbol_solution': ['-', '/', '*', '*', '+']


    while True:
        #loop until nothing left in symbol_solution, break out at bottom of loop

        # get numbers for caculation
        # 

        lastdigit=digit_solution.pop()
        sec_lastdigit=digit_solution.pop()
        tmp_list=[]
        tmp_list.append(int(lastdigit))
        tmp_list.append(int(sec_lastdigit))
        tmp_list.sort()
        lastdigit=tmp_list[1]
        sec_lastdigit=tmp_list[0]


        #  the above logic helps with if the second number is bigger than first reverse them i.e 2 -100 is revered to 100 - 2 this helps with - and division

        # get symbol for caculation
        l_symbol=symbol_solution.pop(0)
        # data in format
            #'l_symbol': '-'

    
        #calc answer and print 
        if l_symbol=='*':
            answer = int(lastdigit) * int(sec_lastdigit)
        if l_symbol=='/':
            answer = int(lastdigit) / int(sec_lastdigit)
            # make a int i.e 25 rather than a float 25.0
            answer=int(answer)
        if l_symbol=='-':
            answer = int(lastdigit) - int(sec_lastdigit)
        if l_symbol=='+':
            answer = int(lastdigit) + int(sec_lastdigit)

        # put the answer back into the digit list
        digit_solution.append(str(answer))

        print ("%s %s %s = %s"%(lastdigit,l_symbol,sec_lastdigit,answer))

        if symbol_solution==[]:
            break
        

# get our numbers to play with
target_to_hit,our_large_numbers,our_small_numbers=pick_numbers(smalln=small_numbers,largen=large_numbers)

print ("Your target is ",target_to_hit)
print ("Our large number(s) are ",our_large_numbers)
print ("Our small number(s) are ",our_small_numbers)

numbers_to_use=2

while (numbers_to_use < 8) or (rv==1) :


    # we have our numbers and the taget lets start getting funcky
    master_numbers=our_large_numbers+our_small_numbers

    # we need 1 less symbol than the number of numbers
    comb_needed=numbers_to_use

    #create all the perumataions of our numbers
    perm = permutations(master_numbers,numbers_to_use)
    comb_needed_m1=numbers_to_use-1
    symbol1 = product(["+", "*", "-","/"],repeat=comb_needed_m1)

    #using permutations inside a nested loop doesn't work as expected so i have taken the smaller permutation and converted into a list
    # might have to test with large datasets as this may slow things down
    symbol2=[]
    for i1 in symbol1:
        t1=i1[0]
        try:
            t2=i1[1]
        except:
            pass
        try:
            t3=i1[2]
        except:
            pass
        try:
            t4=i1[3]
        except:
            pass
        try:
            t5=i1[4]
        except:
            pass
        
        t9=[]
        t9.append(t1)
        try:
            t9.append(t2)
        except: 
            pass
        try:
            t9.append(t3)
        except:
             pass
        try:
            t9.append(t4)
        except:
            pass
        try:
            t9.append(t5)
        except:
            pass
        
        symbol2.append(t9)

    # pass permutations to memory
    for i in perm:
        fn1=int(i[0])
        fn2=int(i[1])
        try:
            fn3=int(i[2])
        except:
            pass
        try:
            fn4=int(i[3])
        except:
            pass
        try:
            fn5=int(i[4])
        except:
            pass
        try:
            fn6=int(i[5])
        except:
            pass
        for sy1 in symbol2:
            s1=sy1[0]
            try:
                s2=sy1[1]
            except:
                pass
            try:
                s3=sy1[2]
            except:
                pass
            try:
                s4=sy1[3]
            except:
                pass
            try:
                s5=sy1[4]
            except:
                pass
            if numbers_to_use==2:
                expression = "%s %s %s" % (fn1,fn2,s1)
            elif numbers_to_use==3:
                expression = "%s %s %s %s %s" % (fn1,fn2,fn3,s1,s2)
            elif numbers_to_use==4:
                expression = "%s %s %s %s %s %s %s" % (fn1,fn2,fn3,fn4,s1,s2,s3)
            elif numbers_to_use==5:
                expression = "%s %s %s %s %s %s %s %s %s" % (fn1,fn2,fn3,fn4,fn5,s1,s2,s3,s4)
            elif numbers_to_use==6:
                expression = "%s %s %s %s %s %s %s %s %s %s %s" % (fn1,fn2,fn3,fn4,fn5,fn6,s1,s2,s3,s4,s5)
            else:
                print ("Err what")
                breakpoint()


            result = reversepolishnotation(expression)
            if verbose_output==1:
                print (expression,result)
                #make_formula_more_readable(expression)
            rv=hownear(target=target_to_hit,answer=result,formula=expression)
            if rv==1:
                break
        if rv==1:
            break
    if rv==1:
        break
    else:
        numbers_to_use+=1
print ("\nSummary")
outby=abs(target_to_hit-nearest_answer)
if outby !=0:
    print ("We were %s out" %(outby))
else:
    print ("Yep we found the answer :)")
print ("We tried to hit %s the nearest we could get was %s made up of %s" %(target_to_hit,nearest_answer,nearest_solution))
make_formula_more_readable(nearest_solution)




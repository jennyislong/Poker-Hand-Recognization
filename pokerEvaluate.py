#================     Functions for each Ranks   ==============================




## Four of a Kind
def fourK(hand,decision):
    decision = decision         # decision is the criteria for function to run 
    RanksA=[]                   # Empty list for Ranks
    for i in hand[0:10:2]:      # goes through each rank in hand (skip suits)
        RanksA.append(i)        # Adds each indiv rank into the empty string
    RanksA_count = []           # Empty list for amount/count of ranks
    for j in RanksA:            # loop through rank list we just made
        z= RanksA.count(j)      # count the amount of ranks in the rank list
        RanksA_count.append(z)  # add the total amount of each rank into list
    if (4 in RanksA_count):     # if theres 4 of one rank
        decision = 1            # set decision as 1
    return(decision)            # return four of a kind when decision is 1 in 
                                # function
                                



## Full House
def fullH(hand,decision):        #The process is same as above
    decision = decision          # decision is the criteria for function to run
    RanksA=[]                    # empty list for ranks
    for i in hand[0:10:2]:       # goes through each rank in hand (skip suits)
        RanksA.append(i)         # Adds each individual rank to empty string
    RanksA_count = []            # empty list for amount/count of ranks
    for j in RanksA:             # loop through the rank list 
        z= RanksA.count(j)       # count the amount of ranks in rank list
        RanksA_count.append(z)   # add the total amount of ranks into count list
    if (3 in RanksA_count) and (2 in RanksA_count): 
                        # here if there are 3 of one rank and 2 of another rank
        decision = 2    # set the decision as 2
    return(decision)   # return full house when the decision is 2 in the function
    
  
## Three of a Kind
def threeK(hand, decision):     #process is same as above 
    decision = decision         #criteria for the function to run
    RanksA = []                 # empty list for ranks
    for i in hand [0:10:2]:     # goes through each rank in hands( skip suits)
        RanksA.append(i)        # add each rank onto rank list
    RanksA_count = []           # empty list for counting ranks
    for j in RanksA:            # goes through rank list
        z = RanksA.count(j)     # counts the amount of ranks in rank list
        RanksA_count.append(z)  # add the total of counts in count list
    if (3 in RanksA_count):      #if theres 3 of one rank 
        decision = 3             #set decision as 3
    return(decision)             # return Three of a kind when decision is 3 in
                                 # the function
    
## Pair 
def pair(hand, decision):        #process is same as above
    decision = decision          # criteria for function to run
    RanksA = []                  # empty list for ranks
    for i in hand [0:10:2]:      # goes through each rank in hands (skip suits)
        RanksA.append(i)         # add each rank onto rank list
    RanksA_count = []            # empty list for count/amount of ranks
    for j in RanksA:             # goes through ranks in rank list
        z = RanksA.count(j)      # count the amount of ranks in rank list
        RanksA_count.append(z)   # add the count to count list
    if (2 in RanksA_count):      # if theres 2 of one rank
        decision = 4             # set decision as 4
    return (decision)            # return Pair when decision is 2 in function


## High
def high(hand,decision):        # similar to processes above but slight diff
    decision = decision         # criteria for function to run
    RanksA = []                 # Empty list for ranks
    RanksIntA = []              # Empty list for ranks ( integer form)
    for i in hand [0:10:2]:     # goes through indiv ranks in hand (no suits)
        RanksA.append(i)        # add those ranks to the empty list for ranks
        RanksIntA.append(i)     # also add it to empty list for ranks( integer)
    RanksA_count = []           # empty list for counting the ranks
    if ('T' in RanksIntA):      # convert the ranks to numeric value(str) in rank
        RanksIntA[RanksIntA.index('T')] = '10'   #i.e. T to '10'
    if ('J' in RanksIntA):
        RanksIntA[RanksIntA.index('J')] = '11'
    if ('Q' in RanksIntA):
        RanksIntA[RanksIntA.index('Q')] = '12' 
    if ('K' in RanksIntA):
        RanksIntA[RanksIntA.index('K')] = '13'    
    if ('A' in RanksIntA):
        RanksIntA[RanksIntA.index('A')] = '14'    
    RanksIntA = [int(a) for a in RanksIntA]   # Converts all ranks to int
    for j in RanksIntA:                     # goes through rank (numeric) list
        RanksA_count.append( RanksIntA.count(j) )
                                    # How many occur once? is it all of them?
    if RanksA_count.count(1) == 5: # if each ranks occur only once in hand
        max_val = RanksA[RanksIntA.index(max(RanksIntA))] 
        # find positioning of the max value from rank list (numeric)
        decision = 5 # set decision as 5
    return(max_val, 5)   # return the highest value when decision 5 is in function

## Flush 
def flush(hand,decision):           # similar to above
    decision = decision             # criteria for function to run
    Suits = []                      # empty string for suits
    for i in hand [1:10:2]:         # goes through the suits in hand (not ranks)
        Suits.append(i)             # adds each suit into the empty list               
    Suits_count = []                # empty list for amount/count of suits
    for j in Suits:                 # goes through suit list
        z= Suits.count(j)           # count the amount of suits in list
        Suits_count.append(z)       # add the amount/count to suit count list
    if (5 in Suits_count):          # if there are 5 same suits in the list
        decision = 6                # set decision as 6
    return (decision)               # return Flush when decision 6 is in function

#=================   Function to evaluate hand   ==============================

def evaluate(hand):
    decision = 0                            #criteria begins at 0
    if flush(hand,decision)==6:             #when decision is 6
        return(print('Flush'))                  # return and print and return Flush
    if fourK(hand,decision) == 1:           # when decision is 1
        return(print('Four of a Kind'))         # return and print four of a kind
    if fullH(hand,decision) == 2:           # when decision is 2
        return(print('Full House'))             # return and print full house
    if threeK(hand,decision) ==3 :          # When decision is 3
        return(print('Three of a Kind'))        # return and print three of kind
    if pair(hand, decision) ==4:            # when decision is 4
        return(print('Pair'))                   #return and print pair
    if high(hand,decision)[1]==5:           # when decision is 5
        return(print(high(hand,decision)[0] +' High'))  #print max value + high 
                                                            # i.e. Q high
        

#====================       Test Function           ===========================
        
        
test_values = ('Qs7s2s4s5s','7h8hKsTs8s','2h4d2d4s4c',
                'KsKhKc8sKd','3s9hTh9s9d','2s8hThQs9d')

for test in test_values:     # goes through each test values    
    evaluate(test)              # in to the evaluate function and show which
                                    #rank the hands should be
# SHOULD PRINT OUT : 
## Flush
## Pair
## Full House
## Four of a Kind
## Three of a Kind
## Q High


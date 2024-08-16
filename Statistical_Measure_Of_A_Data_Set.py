import statistics

def mainrun():
    while True:
        amount=int(input("\nHow many numbers are in your data set that you would like to analyze? "))
        numbers=[]

        if(int(amount))<2:
            print("\nI'm sorry, at least two numbers are required.")
        else:
            break 

    for i in range(amount):
        num=float(input("\nType each number here: "))
        numbers.append(num)
        
    
    print(numbers)
    global mean, median, mode, rangeofdata, variance, standarddev, q1, q3, iqr
    mean=sum(numbers)/len(numbers)
    median=statistics.median(numbers)
    mode=statistics.mode(numbers)
    rangeofdata=max(numbers)-min(numbers)
    variance=statistics.variance(numbers)
    standarddev=statistics.stdev(numbers)
    q1=statistics.quantiles(numbers, n=4)[0]
    q3=statistics.quantiles(numbers, n=4)[2]
    iqr=q3-q1



def whichmeasure():
    measures=[]
    posschoices=[1,2,3,4,5,6,7,8,9]
    while True:
        try:
            whichone = int(input("\nWhich measure would you like to select for your data set? You may choose from: \n1) mean\n2) median\n3) mode\n4) range\n5) variance\n6) standard deviation\n7) the first quartile\n8) the third quartile\n9) the interquartile range\nType the number correlating with your response here: "))
            if whichone not in posschoices:
                print("\nThis is not a valid option. Try again.")
                continue
        except ValueError:
            print("\nInvalid input. Please enter a number from 1 to 9.")
            continue
        another=input("\nWould you like to choose another measure? Type yes or no: ")
        measures.append(whichone)
        if another.lower()=="yes":
                     continue
                     measures+=whichone
        else:
            print("\nYou either said no or you typed something random, so I'll assume you do not want another measure.")
            break

    if 1 in measures:
        print("\nYour mean is " +str(mean))
    if 2 in measures:
        print("\nYour median is " +str(median))
    if 3 in measures:
        print("\nYour mode is " +str(mode))
    if 4 in measures:
        print("\nYour range is " +str(rangeofdata))
    if 5 in measures:
        print("\nYour variance is " +str(variance))
    if 6 in measures:
        print("\nYour standard deviation is " +str(standarddev))
    if 7 in measures:
        print("\nYour first quartile is " +str(q1))
    if 8 in measures:
        print("\nYour third quartile is " +str(q3))
    if 9 in measures:
        print("\nYour interquartile range is " +str(iqr))

mainrun()
whichmeasure()

print("\nThanks for using this program!")







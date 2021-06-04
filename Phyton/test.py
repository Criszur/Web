Answer=str(input("Do you orderd delivery? "))
     
if Answer== 'yes' or Answer=='Yes' or  Answer=='YES' or Answer== 'y':
    price=int(input("How much is the order? "))
    people=int(input("How many people splitting the order? "))               
    costPerPerson=price/people
    print("The cost per person is $",float(costPerPerson))
    
elif Answer== 'no' or Answer== 'No' or Answer== 'NO':
    print("No?! So who is cooking? ")

else:
    print("Answer yes or no plz")

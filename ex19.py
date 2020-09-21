def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party")
    print("Get a blacket. \n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("Or we can use variables directly from our script")
amount_of_cheese = int(input("enter no cheese: "))
amount_of_crackers = int(input("enter no of crackers: "))

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too.")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

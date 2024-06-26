marbles_cost = 9.05
football_cost = 4.95
received_amount = 6.52

total_cost = marbles_cost + football_cost + received_amount

# the hypothesis refers to the total cost of toys
if total_cost == 3.7:
    # check if the hypothesis value and the total cost in the premise are equal
    label = "entailment"
else:
    # if the hypothesis value and the total cost in the premise are not equal, it's a contradiction
    label = "contradiction"

print(label)

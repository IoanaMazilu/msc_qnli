premise_amount = float(input("more than 500 and Greg's share is Rs."))
hypothesis_amount = float(input("600 and Greg's share is Rs."))

# check if the hypothesis amount is greater than the premise amount
if hypothesis_amount > premise_amount:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif hypothesis_amount == premise_amount:
    # the hypothesis is neutral as it does not contradict the premise
    label = "neutral"
else:
    # the premise only gives an estimate, so any amount greater than the estimate is consistent with the premise
    label = "neutral"

print(label)
